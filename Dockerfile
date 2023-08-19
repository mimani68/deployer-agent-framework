FROM python:3.11

WORKDIR /app

RUN apt update && apt install -y git curl

ADD requirements.txt /app

RUN pip install -r requirements.txt

ADD . /app

RUN mkdir /app/certs \
    && cd /app/certs \
    && openssl genrsa -out private.pem 4096 \
    && openssl rsa -in private.pem -outform PEM -pubout -out public.pem

EXPOSE 27514

CMD [ "flask", "run", "--host=0.0.0.0", "--port=27514" ]