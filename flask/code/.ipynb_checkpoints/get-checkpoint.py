import requests
import json
from time import time
from datetime import datetime

s_t = time()
print(datetime.now())

res = requests.get('http://192.168.6.57:5000/')
print(str(res.status_code) + " | " , float(res.text)-s_t)