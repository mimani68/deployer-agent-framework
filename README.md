# Deployer Agent Framework

Simple and secure deployer and script runner

## Installation

```bash
python -m pip install --user virtualenv
python -m venv venv
pip install -r requirements.txt
```
## Run application

```bash
flask run --host=0.0.0.0 --port=27514
```

## Usage

### A) Simple and Unsecure connection

```bash
curl -XPOST --header "Content-Type: application/json" "http://localhost:27514/?cmd=test"  --data '{"accessToken":"37109860-3c1b-11ee-8265-cba1ae806b41"}'
```

### B) Secure data transportation

> [Create public and private keys](./docs/rsa-encryption.md)

Send request with `cURL`

```bash
msg=`echo "{\"accessToken\":\"76448262-5bef-416a-9c5a-9200c2300e82\"}" | openssl pkeyutl -encrypt -inkey public.pem -pubin -in - | base64 -w 0`
```

> Note: test your payload

```bash
echo "$msg" | base64 -d - | openssl pkeyutl -decrypt -inkey private.pem -in -
```

And the send request
```bash
curl -XPOST --header "Content-Type: application/json" "http://localhost:27514/?cmd=test" --data "$msg"
```
### C) Docker-base

#### C-1) Build docker image

```bash
docker build -t deployer:1.0.0 .
```

#### C-2) Usage of dockerfile

```bash
docker run \
    --name deployer \
    -d \
    -e SECURE_CONNECTION="false" \
    -e RETRY_INTERVAL=10 \
    -e ACCESS_TOKEN="37109860-3c1b-11ee-8265-cba1ae806b41" \
    -v /var/run/docker.sock:/var/run/docker.sock:ro \
    -v ${PWD}/tmp:/app/tmp \
    -v ${PWD}/scripts:/app/scripts \
    -v ${PWD}/certs:/app/certs \
    -v ${PWD}/logs:/app/logs \
    -p 27514:27514 \
    deployer:latest
```