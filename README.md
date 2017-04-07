# s3zipper
Microservice that Servers Streaming Zip file from S3 Securely

## Read the blog here
[Original Blog Post](http://engineroom.teamwork.com/how-to-securely-provide-a-zip-download-of-a-s3-file-bundle/)

## Docker-compose
running:
```
AWS_S3_BUCKET_NAME=<bucket> AWS_REGION=<region> AWS_ACCESS_KEY_ID=<key> AWS_SECRET_ACCESS_KEY=<secret> docker-compose  -f docker-compose.yml -f docker-compose.development.yml up
```

you will have zipper server running on port 8123
and a rest client to register jsons on port 8124

```
 curl -X POST -H "Content-Type: application/json" -d@./files.json http://localhost:8124/
```

will return a string

browse to http://localhost:8123?ref=<that string>


