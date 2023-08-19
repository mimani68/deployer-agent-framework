import os, datetime

def info(msg):
    message = f'[INFO] { datetime.datetime.now().isoformat() } - {msg}'
    os.system(f'echo "{ message }" >> logs/$(date --iso-8601).log')
    print(message)