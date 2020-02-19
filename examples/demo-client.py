import requests
import _init_path
import feature
from record import record

server = "http://192.168.99.100:5000/recognize"

record("record.wav", time=5)  # modify time to how long you want

f = open("record.wav", "rb")

files = {"file": f}

r = requests.post(server, files=files)

print("")
print("识别结果:")
print(r.text)
