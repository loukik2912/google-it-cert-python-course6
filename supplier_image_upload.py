#!/usr/bin/env python3
import requests
import glob

# This example shows how a file can be uploaded using
# The Python Requests module

url = "http://localhost/upload/"

for fileName in glob.glob('supplier-data/images/*.jpeg'):
 print(fileName)
 with open(fileName, 'rb') as opened:
   r = requests.post(url, files={'file': opened})
