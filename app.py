#!/usr/bin/env python

import subprocess
import json
import re
import os
from flask import Flask, request

SERVER_ACCESS_TOKEN = os.getenv('SERVER_ACCESS_TOKEN')
NEED_ACCESS_TOKEN = os.getenv('NEED_ACCESS_TOKEN') == 'true'

def encrypt_private_key(message):
  return subprocess.check_output(["bash", "-c", "echo {} | openssl rsautl -encrypt -inkey ./certs/public.pem -pubin -in - | base64 > top_secret.enc".format(message)])

def decrypt_public_key(encrypted_message):
  print(encrypted_message)
  subprocess.check_output(["bash", "-c", "echo '{}' > top_secret.enc".format(encrypted_message)])
  return subprocess.check_output(["bash", "-c", "cat top_secret.enc | base64 --decode - | openssl rsautl -decrypt -inkey ./certs/private.pem -in -"])

app = Flask(__name__)

# 
# must send "SERVER_ACCESS_TOKEN" that encypted with rsa pair keys
# 
# curl localhost:3000/?cmd=hello --data "fjfdfighfey8gynhe8rt87eyt"
# curl localhost:3000/?cmd=deploy --data "fjfdfighfey8gynhe8rt87eyt"
# 
@app.route("/", methods=['POST'])
def run_command():
  # 
  # Recive encrypted message
  # 
  if NEED_ACCESS_TOKEN :
    encrypted_base64_payload = request.get_data()
    value = decrypt_public_key(encrypted_base64_payload)
    a = json.loads(value)
    if a["accessToken"] != SERVER_ACCESS_TOKEN :
      return "Unauthorized request"

  # 
  # Run command
  # 
  scriptInpit = request.args.get('cmd')
  a = subprocess.check_output(['ls', "./scripts"])
  a = a.split('\n')
  for executableFile in a:
    x = re.search("{}.sh".format(scriptInpit), executableFile)
    if x >= 0 :
      os.system("./scripts/" + scriptInpit + ".sh")
      return "DONE"
    else:
      return "FILAED"