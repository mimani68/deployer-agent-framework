# Encryption

## 1) Generate RSA Private Key
You can generate a public and private RSA key pair like this:
```bash
openssl genpkey -algorithm RSA -out private.pem -pkeyopt rsa_keygen_bits:4096
```

## 2) Export the RSA Public Key to a File

This is a command that is
```bash
openssl rsa -in private.pem -outform PEM -pubout -out public.pem
```

## 3) Check the certificate

```bash
openssl rsa -in private.pem -text -noout
```

## 4) Encrypt message with public key

```bash
echo "{\"accessToken\":\"8X20xd23-X2-l0P5g5\"}" | openssl pkeyutl -encrypt -inkey public.pem -pubin -in - | base64 > encoded_text.enc
```

## 5) Decrypt the file using a private key

```bash
cat encoded_text.enc | base64 --decode - | openssl pkeyutl -decrypt -inkey private.pem -in -
```