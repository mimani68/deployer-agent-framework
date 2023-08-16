#!/usr/bin/env python

import subprocess
import json
import os
from flask import Flask, request
from libs.directory.list import get_sh_files
from libs.logs.log import info
from libs.command.run import run_command

SERVER_ACCESS_TOKEN = os.getenv('SERVER_ACCESS_TOKEN')
NEED_ACCESS_TOKEN = os.getenv('NEED_ACCESS_TOKEN') == 'true'

def encrypt_private_key(message):
  return subprocess.check_output(["bash", "-c", "echo {} | openssl rsautl -encrypt -inkey ./certs/public.pem -pubin -in - | base64 > top_secret.enc".format(message)])

def decrypt_public_key(encrypted_message):
  info(encrypted_message)
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
# @api_token_required
def run_command():
  # 
  # Receive encrypted message
  # 
  if NEED_ACCESS_TOKEN :
    encrypted_base64_payload = request.get_data()
    value = decrypt_public_key(encrypted_base64_payload)
    currentScriptsList = json.loads(value)
    if currentScriptsList["accessToken"] != SERVER_ACCESS_TOKEN :
      return "Unauthorized request"

  # 
  # Run command
  # 
  scriptInputName = request.args.get('cmd')
  info("Request for scrip=" + scriptInputName)
  script = scriptInputName + ".sh"
  currentScriptsList = get_sh_files("./scripts")
  if len(currentScriptsList) == 0:
    info("Script directory is empty")
    return "No script is exists"
  try:
    for executableFile in currentScriptsList:
      if script in executableFile:
        info("About to execute script ./scripts/" + script)
        # os.system("./scripts/" + script)
        result = run_command("./scripts/" + script)
        # return "DONE"
        return result
    return "FAILED"
  except:
    return "FAILED"