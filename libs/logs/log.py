import os, datetime

def info(msg):
    message = f'[INFO] { datetime.datetime.now().isoformat() } - {msg}'
    os.system(f'echo "{ message }" >> logs/$(date).log')
    print(message)