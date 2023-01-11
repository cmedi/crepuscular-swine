#!/usr/bin/env python3

import requests
import os
import os.path

dir ='crepuscular-swine/supplier-data/images'
print(os.path.exists(dir))
url = "http://localhost/upload"

for file in os.listdir(dir):
  if file.endswith('.jpeg'):
    print(file)
    with open(os.path.join(dir,file), 'rb') as opened:
      r = requests.post(url, files={'file': opened})
      print(r.status_code)
