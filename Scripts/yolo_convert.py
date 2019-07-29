# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 03:15:21 2019

@author: Varad Srivastava
"""

import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join
import pandas as pd
import numpy as np


def convert(xmin, ymin, xmax, ymax):
    w = 1280
    h = 720
    dw = 1./w
    dh = 1./h
    x = (xmin + xmax)/2.0
    y = (ymin + ymax)/2.0
    w = xmax - xmin
    h = ymax - ymin
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)


#for filename in glob.glob('*.csv'):
filename = '1.1.1.0.csv'
filename_without_ext = os.path.splitext(filename)[0]
extension = os.path.splitext(filename)[1]
df = pd.read_csv(filename, header=None)
clas = df.iloc[0,0]
shap = df.shape[0]
for i in range(0,shap):
    xmin = df.iloc[i,1]
    ymin = df.iloc[i,2]
    xmax = df.iloc[i,3]
    ymax = df.iloc[i,4]
    x,y,w,h = convert(xmin, ymin, xmax, ymax)
    data = {0 : [clas], 1 : [x], 2 : [y], 3 : [w], 4 : [h]} 
    dataf = pd.DataFrame(data)
    dataf.to_csv(filename_without_ext + '.txt', header=None, index=None, mode='a',sep=' ')
