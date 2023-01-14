#!/usr/bin/env python3

import requests
import os
import os.path

dir ='supplier-data/images'
print(os.path.exists(dir))

url = "http://localhost/upload/"

for file in os.listdir(dir):
  print(file)
  if file.endswith('.jpeg'):
    with open(os.path.join(dir,file), 'rb') as opened:
      r = requests.post(url, files={'file': opened})
      print(r.status_code)
