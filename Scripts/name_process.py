# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 15:29:27 2019

@author: Varad Srivastava
"""

import os

#for root, dirs, files in os.walk("D:\\Datasets\\action\\Train-Set\\Drone1\\Morning\\Extracted-Frames-1280x720"):
 #   if not files:
  #      continue
   # prefix = os.path.basename(root)
    #for f in files:
     #   os.rename(os.path.join(root,f), os.path.join(root, "{}.{}".format(prefix, f))
     
from os import walk, path, rename

for dirpath, _, files in walk("D:\\Datasets\\action\\Train-Set\\Drone2\\Noon\\Extracted-Frames-1280x720"):
    for f in files:
        rename(path.join(dirpath, f), path.join(dirpath, path.split(dirpath)[-1] + '.' + f))