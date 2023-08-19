import subprocess
from libs.logs.log import info

# def encrypt_private_key(message):
#   return subprocess.check_output(["bash", "-c", "echo {} | openssl pkeyutl -encrypt -inkey ./certs/public.pem -pubin -in - | base64 > tmp/encoded_text.enc".format(message)])

def decrypt_public_key(encrypted_message):
  info(encrypted_message)
  try:
    subprocess.check_output(["bash", "-c", "echo '{}' > tmp/encoded_text.enc".format(encrypted_message)])
    result = subprocess.check_output(["bash", "-c", "cat tmp/encoded_text.enc | base64 --decode - | openssl pkeyutl -decrypt -inkey ./certs/private.pem -in -"])
    return {
      "status": "SUCCESS",
      "payload": result
    }
  except:
    return {
      "status": "FAILED",
    }