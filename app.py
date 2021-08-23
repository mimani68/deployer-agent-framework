from flask import Flask, request
import os
import re
import subprocess

app = Flask(__name__)

# 
# curl localhost:3000/?cmd=hello
# curl localhost:3000/?cmd=deploy
# 
@app.route("/", methods=['GET'])
def run_command():
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