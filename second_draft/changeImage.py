#!/usr/bin/env python3

from PIL import Image
import os
import os.path
#directory
#supplier/data/images/

dir = 'supplier-data/images/'
size = (600,400)

for file in os.listdir(dir):
  if file.endswith(".tiff"):
    im=Image.open(os.path.join(dir,file))
    im = im.convert("RGB")
    im = im.resize(size)
    im.save(os.path.join(dir,file.replace('.tiff','.jpeg')),'JPEG')
    print(im.format, im.size, im.mode)
    



