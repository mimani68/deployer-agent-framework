import json
import os
from dotenv import load_dotenv
from flask import Flask, request

load_dotenv() 

from libs.directory.list import get_sh_files
from libs.logs.log import info
from libs.command.run import run_command
from libs.encryption.secure import decrypt_public_key

ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
SECURE_CONNECTION = os.getenv('SECURE_CONNECTION') == 'true'

info("Bootstrap")

if SECURE_CONNECTION :
  info("Encryption mode activate.")

app = Flask(__name__)

@app.route("/", methods=['POST'])
# @api_token_required
def remote_command_handler():
  payload = {}

  if request.content_length in [0, None]:
    info("Payload is empty")
    return { "message": "Payload is empty" }

  # 
  # Receive encrypted message
  # 
  if SECURE_CONNECTION :
    value = decrypt_public_key(request.get_data().decode('utf-8'))
    if value['status'] == 'FAILED':
      info("Encrypted payload is invalid")
      return { "message": "Encrypted request needed." }
    payload = json.loads(value['payload'].decode('utf-8').replace('\n', ''))
  else:
    payload = request.get_json()

  if not 'accessToken' in payload or payload["accessToken"] != ACCESS_TOKEN :
    info("Server Token ID is invalid")
    return { "message": "Server Token is unrecognized." }
    
  scriptInputName = request.args.get('cmd')
  info("Request for scrip=" + scriptInputName)
  script = scriptInputName + ".sh"
  currentScriptsList = get_sh_files("./scripts")
  if len(currentScriptsList) == 0:
    info("Script directory is empty")
    return { "message": "No script is exists" }
  try:
    for executableFile in currentScriptsList:
      if script in executableFile:
        info("About to execute script ./scripts/" + script)
        result = run_command("./scripts/" + script)
        info(f"Response={ result }")
        return {
          "status": "DONE",
          "result": result
        }
    return { "status": "FAILED" }
  except:
    return { "status": "FAILED" }