FROM public.ecr.aws/docker/library/python:3.13.5-bullseye

ADD . /opt/flaskapp/

WORKDIR /opt/flaskapp/

RUN pip install -r requirements.txt

CMD flask run --host 0.0.0.0