#!/usr/bin/env python

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64
import os
import re
import subprocess
import json
from flask import Flask, request

SERVER_ACCESS_TOKEN = "8X-i2x2t3M-X2-l0P5g5"

def encrypt_private_key(message):
  return subprocess.check_output(["bash", "-c", "echo {} | openssl rsautl -encrypt -inkey ./certs/public.pem -pubin -in - | base64 > top_secret.enc".format(message)])

def decrypt_public_key(encrypted_message):
  print(encrypted_message)
  subprocess.check_output(["bash", "-c", "echo '{}' > top_secret.enc".format(encrypted_message)])
  return subprocess.check_output(["bash", "-c", "cat top_secret.enc | base64 --decode - | openssl rsautl -decrypt -inkey ./certs/private.pem -in -"])

app = Flask(__name__)

# 
# curl localhost:3000/?cmd=hello
# curl localhost:3000/?cmd=deploy
# 
@app.route("/", methods=['POST'])
def run_command():
  # 
  # Recive encrypted message
  # 
  encrypted_base64_payload = request.get_data()
  value = decrypt_public_key(encrypted_base64_payload)
  a = json.loads(value)
  if a["accessToken"] != SERVER_ACCESS_TOKEN :
    return "Unauthorized request"
  return "Welcome"

  # 
  # Run command
  # 
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