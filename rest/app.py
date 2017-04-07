#!flask/bin/python
from flask import Flask, request, abort
import json
import redis
import random
import string


def randomword(length):
    return ''.join(random.choice(string.ascii_letters) for i in range(length))

app = Flask(__name__)
r = redis.StrictRedis(host='redis', port=6379, db=0)


@app.route("/", methods=['POST'])
def register():
    if not request.json:
        abort(400)
    key = randomword(10)
    r.set("zip:%s" % (key), json.dumps(request.json), ex=600)
    return key


if __name__ == "__main__":
    app.run()
