#!/usr/bin/env python

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64
import os
import re
import subprocess
from flask import Flask, request


def encrypt_private_key(a_message, private_key):
  encryptor = PKCS1_OAEP.new(private_key)
  encrypted_msg = encryptor.encrypt(a_message)
  print(encrypted_msg)
  encoded_encrypted_msg = base64.b64encode(encrypted_msg)
  print(encoded_encrypted_msg)
  return encoded_encrypted_msg

def decrypt_public_key(encoded_encrypted_msg, public_key):
  encryptor = PKCS1_OAEP.new(public_key)
  decoded_encrypted_msg = base64.b64decode(encoded_encrypted_msg)
  # print(decoded_encrypted_msg)
  decoded_decrypted_msg = encryptor.decrypt(decoded_encrypted_msg)
  return decoded_decrypted_msg

app = Flask(__name__)

# 
# curl localhost:3000/?cmd=hello
# curl localhost:3000/?cmd=deploy
# 
@app.route("/", methods=['POST'])
def run_command():
  encrypted_base64_payload = request.get_data()
  f = open("certs/private.pem", "r")
  print(f.read())
  # print(encrypted_base64_payload.decode('utf-8'))
  return decrypt_public_key(encrypted_base64_payload, f.read())

  # scriptInpit = request.args.get('cmd')
  # a = subprocess.check_output(['ls', "./scripts"])
  # a = a.split('\n')
  # for executableFile in a:
  #   x = re.search("{}.sh".format(scriptInpit), executableFile)
  #   if x >= 0 :
  #     os.system("./scripts/" + scriptInpit + ".sh")
  #     return "DONE"
  #   else:
  #     return "FILAED"