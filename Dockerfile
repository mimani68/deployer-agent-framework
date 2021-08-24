FROM python:2.7-slim

WORKDIR /app

ADD requriments.txt /app

RUN pip install -r requriments.txt

ADD . /app

RUN cd /app/certs; \
openssl genrsa -out private.pem 4096; \
openssl rsa -in private.pem -outform PEM -pubout -out public.pem

EXPOSE 27514

CMD [ "flask", "run", "--host=0.0.0.0", "--port=27514" ]