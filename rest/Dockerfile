FROM python:3.6.1-alpine

ADD requirements.txt /app/requirements.txt

WORKDIR /app/

RUN pip install -r requirements.txt

ADD ./ /app/

EXPOSE 8000

CMD gunicorn -w 2 -b :8000 app:app
