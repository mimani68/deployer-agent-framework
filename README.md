# Deployer Agent Framework

## Installation

```bash
python -m pip install --user virtualenv
python -m venv venv
pip install -r requriments.txt
```
## Run application
```bash
flask run --host=0.0.0.0 --port=27514
```
### Dockerized

#### Build docker image
```bash
docker build -t deployer:1.0.0 .
```
#### usage of dockerfile

```bash
docker run \
--rm \
--name deployer \
-e NEED_ACCESS_TOKEN="false" \
-e SERVER_ACCESS_TOKEN="123" \
-v /home/centos:/home/centos \
-v /usr/bin/docker:/usr/bin/docker:ro \
-v /var/run/docker.sock:/var/run/docker.sock:ro \
-v ${PWD}/scripts:/app/scripts \
-v ${PWD}/certs:/app/certs \
-v ${PWD}/logs:/app/logs \
-p 27514:27514 \
deployer:1.0.0
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
