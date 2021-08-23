# Deployer Agent Framework

## Installation

```bash
pip install Flask
```
## Run application
```bash
export FLASK_APP=hello
export FLASK_ENV=development
flask run --host=0.0.0.0 --port=3000
```

## Usage

```bash
curl localhost:3000/?cmd=hello
curl localhost:3000/?cmd=deploy&param=12&password=123
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
echo "salam" | openssl rsautl -encrypt -inkey public.pem -pubin -in - -out top_secret.enc
```

### Decrypt the file using a private key

```bash
openssl rsautl -decrypt -inkey private.pem -in top_secret.enc > decrypted_message.txt
```
