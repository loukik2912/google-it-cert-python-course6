#! /usr/bin/env python3

import os
import requests
import glob

for fileName in glob.glob('supplier-data/descriptions/*.txt'):
 img_name = fileName.split('/')[-1].split('.')[0] + '.jpeg'
 #print(img_name, os.path.exists('supplier-data/images/'+img_name))

 with open(fileName, 'r') as fp:
  file_content = fp.read().splitlines()
  #print(file_content)

 content_dict = dict()
 content_dict['name'] = file_content[0]
 content_dict['weight'] = int(file_content[1].split()[0])
 content_dict['description'] = file_content[2]
 content_dict['image_name'] = img_name
 print(content_dict)

 url = "http://localhost/fruits/"
 r = requests.post(url, data=content_dict)
