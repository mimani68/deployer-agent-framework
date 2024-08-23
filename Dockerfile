FROM docker:27-cli

WORKDIR /app

RUN apk add --no-cache python3 py3-pip git curl

ADD requirements.txt /app

RUN pip install -r requirements.txt --break-system-packages

ADD . /app

RUN mkdir /app/certs \
    && cd /app/certs \
    && openssl genrsa -out private.pem 4096 \
    && openssl rsa -in private.pem -outform PEM -pubout -out public.pem

EXPOSE 27514

CMD [ "flask", "run", "--host=0.0.0.0", "--port=27514" ]