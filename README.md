# zipper
Microservice that Servers Streaming Zip file from a storgae


## Read the blog here
[Original Blog Post](http://engineroom.teamwork.com/how-to-securely-provide-a-zip-download-of-a-s3-file-bundle/)

## features:
- uses django-storages so can be backend with any storage supported by this library, the current implementation is s3
- writes a content of file using string directly without using a storage 
- dynamically sets the name of the file

## Known issues
- streaming works between files and not in a file, which means that the service first download the file from s3 and only later streams it



## schema:
  ```
  {
 "zip_filename": <filename>,
 "files":  
  [{"content":<the content of a file>,"filename":<filename>},
   {"path":"<path of the file using django storages>","filename":"filename"}
  ]
 }
```

## public docker images:
- https://hub.docker.com/r/guydou/zipper-python/
- https://hub.docker.com/r/guydou/zipper-rest/


## Docker-compose
running:
```
AWS_STORAGE_BUCKET_NAME=<bucket> AWS_REGION=<region> AWS_ACCESS_KEY_ID=<key> AWS_SECRET_ACCESS_KEY=<secret> docker-compose  -f docker-compose.yml  up
```

you will have zipper server running on port 8123
and a rest client to register jsons on port 8124

assuming you have a *file.json* with the schema

```
 curl -X POST -H "Content-Type: application/json" -d@./files.json http://localhost:8124/
```

will return a string

browse to http://localhost:8123/zip/<that_string>


