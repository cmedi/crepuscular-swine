#!/usr/bin/env python3


import re
import os
import requests
import os.path
import pprint

url = r"http://linux-instance-external-IP/fruits"
descdir = (
    r"C:\Users\writi\source\repos\cmedi\crepuscular-swine\supplier-data\descriptions"
)


fruits = []

descfiles = os.listdir(descdir)

def normalize(weight):
    normalized = re.sub(r"\D", "", weight)
    return normalized


def frutify():
    return fruit


for description in descfiles:
    # 'supplier-data/descriptions/'
    path = os.path.join(descdir, description)
    print(path)
    with open(path, "r") as opened:

        line_counter = 3
        fruit = {"name": "", "weight": 0, "description": "", "image_name": ""}
        for line in opened:
            fruit["image_name"] = os.path.basename(path.replace(".txt", ".jpeg"))
            if line_counter == 3:
                fruit["name"] = line
                line_counter -= 1
            elif line_counter == 2:
                fruit["weight"] = normalize(line)
                line_counter -= 1
            elif line_counter == 1:
                fruit["description"] = line
                line_counter -= 1
        line_counter = 3

        fruits.append(fruit)

for fruit in fruits:
    r = requests.post(url, data=fruit)
    print(r.status_code)
