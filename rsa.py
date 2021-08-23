from Crypto.PublicKey import RSA
import base64
import json

randomString = "h847r87y9aus98y*&T22"
message = dict(accessToken="8d4E7k3h0v8q4P")
messageString = json.dumps(message)

a = open("certs/public.pem", "r")
encryptor = RSA.importKey(a.read())
encrypted_msg = encryptor.encrypt(messageString, randomString)
encoded_encrypted_msg = base64.b64encode(encrypted_msg[0])

f = open("certs/private.pem", "r")
encryptor = RSA.importKey(f.read())
decoded_encrypted_msg = base64.b64decode(encoded_encrypted_msg)
decoded_decrypted_msg = encryptor.decrypt(decoded_encrypted_msg)
print(decoded_decrypted_msg)