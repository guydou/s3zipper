FROM python:3.5.2

ADD requirements.txt /app/requirements.txt

WORKDIR /app/

RUN pip install -r requirements.txt

ADD ./ /app/

EXPOSE 8000

CMD gunicorn -c zipper/gunicorn_conf.py zipper.wsgi
