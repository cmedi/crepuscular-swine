#!/usr/bin/env python3

import pprint
from re import I
import requests
import os
import os.path

url = r'http://linux-instance-external-IP/fruits'
descdir = 'supplier-data/descriptions/'
imgdir = 'supplier-data/images/'

fruits = []
fruit = {'name':'', 'weight':0, 'description':'', 'image_name':''}

descfiles = os.listdir(descdir)
imgfiles = os.listdir(imgdir)
fruit_counter = 0


for description in descfiles:
    print(description)
    path = os.path.join(descdir,description)
    with open(path, 'r') as opened:
        fruity = []
        for line in opened:
           fruity.append(line.strip())
        fruit['name'] = fruity[0]
        fruit['weight'] = fruity[1]
        fruit['description'] = fruity[2]
        fruit['image_name'] = os.path.basename(path.replace('.txt','.jpeg'))
        print(fruit)
        