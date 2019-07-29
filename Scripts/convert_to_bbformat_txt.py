# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 23:42:57 2019

@author: Varad Srivastava
"""

import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join
import pandas as pd
import numpy as np
import glob


for filename in glob.glob('*.csv'):
#filename = '1.1.1.0.csv'
    filename_without_ext = os.path.splitext(filename)[0]
    extension = os.path.splitext(filename)[1]
    df = pd.read_csv(filename, header=None)
    #clas = df.iloc[0,0]
    clas = pd.DataFrame([df.iloc[0,0]])
    shap = df.shape[0]
    dataf = df.iloc[:,1:]
    clas.to_csv(filename_without_ext + '.txt', header=None, index=None, mode='a',sep=' ')
    dataf.to_csv(filename_without_ext + '.txt', header=None, index=None, mode='a',sep=' ')