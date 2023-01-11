#!/usr/bin/env python3

import requests
import os
import os.path

url = r'http://linux-instance-external-IP/fruits'
dir = 'supplier-data/descriptions/'

fruits = []
fruit = {'name':'', 'weight':'', 'description':0, 'image_name':''}

files = os.listdir(dir)

for description in files:
 path = os.path.join(dir,description)
 with open(path, 'r') as opened:
   print(len(opened.readlines()))
