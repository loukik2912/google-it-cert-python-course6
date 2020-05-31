#!/usr/bin/env python3

import os
import PIL
from PIL import Image
import glob

for fileName in glob.glob('supplier-data/images/*.tiff'):
 file_name = fileName.split('.')[0]
 print(file_name)

 img = Image.open(fileName).convert('RGB').resize((600, 400))
 img.save(file_name+'.jpeg', 'JPEG')
