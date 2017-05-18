from django.http import StreamingHttpResponse, HttpResponseBadRequest
from zipstream import ZIP_DEFLATED, ZipFile
from django.core.files.storage import get_storage_class
import redis
import json


redis_client = redis.StrictRedis(host='redis', port=6379, db=0)

def read_in_chunks(file_object, chunk_size=1024):
    """Lazy function (generator) to read a file piece by piece.
    Default chunk size: 1k."""
    while True:
        data = file_object.read(chunk_size)
        if not data:
            file_object.close()
            break
        yield data


def zipball(request, token):
    zip_content = redis_client.get("zip:%s" % (token))
    if not(zip_content):
        return HttpResponseBadRequest()
    zip_content = json.loads(zip_content.decode('utf-8'))
    zip_filename = zip_content['zip_filename']
    z = ZipFile(mode='w', compression=ZIP_DEFLATED)
    for file_def in zip_content['files']:
        filepath = file_def.get("path", None)
        file_content = file_def.get("content", None)
        filename = file_def.get("filename", None)
        backend = file_def.get("backend", None)
        if filepath:
            storage = get_storage_class(backend)()
            f = storage.open(filepath, 'r')
            z.write_iter(filename, read_in_chunks(f))
        elif file_content:
            z.writestr(filename, file_content.encode("utf-8"))
    response = StreamingHttpResponse(z, content_type='application/zip')
    response['Content-Disposition'] = 'attachment; filename={}'.format(zip_filename)
    return response
