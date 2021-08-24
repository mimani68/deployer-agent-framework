# Deployer Agent Framework

## Installation

```bash
pip install Flask
```
## Run application
```bash
export FLASK_APP=hello
export FLASK_ENV=development
flask run --host=0.0.0.0 --port=27514
```

## Certs

### Generate a 2048 bit RSA Key
You can generate a public and private RSA key pair like this:
```bash
openssl genrsa -out private.pem 4096
```
or 
```bash
openssl genrsa -des3 -passout pass:me498yw98ry94ytrio -out private.pem 4096
```
or 
```bash
pwgen -N 1 -y 50 | openssl genrsa -des3 -passout stdin -out private.pem 4096
```
### Export the RSA Public Key to a File

This is a command that is

```bash
openssl rsa -in private.pem -outform PEM -pubout -out public.pem
```
### Encrypt message with public key

```bash
echo "{\"accessToken\":\"8X20xd23-X2-l0P5g5\"}" | openssl rsautl -encrypt -inkey public.pem -pubin -in - | base64 > top_secret.enc
```

### Decrypt the file using a private key

```bash
cat top_secret.enc | base64 --decode - | openssl rsautl -decrypt -inkey private.pem -in -
```

## Usage

### Standalone

Send request with `cURL`

```bash
msg=`echo "{\"accessToken\":\"8X-i2x2t3M-X2-l0P5g5\"}" | openssl rsautl -encrypt -inkey public.pem -pubin -in - | base64`
```
And the send request
```bash
curl -XPOST localhost:27514/?cmd=hello --data "$msg"
```

### Dockerized

```bash
docker run --rm \
--name dep \
-e NEED_ACCESS_TOKEN="false" \
-e SERVER_ACCESS_TOKEN="123" \
-v ${PWD}/scripts:/app/scripts \
-v ${PWD}/certs:/app/certs \
-v ${PWD}/logs:/app/logs \
-p 27514:27514 \
deployer:1.0.0
```