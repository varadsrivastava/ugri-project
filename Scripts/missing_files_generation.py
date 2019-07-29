# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 08:00:33 2019

@author: Varad Srivastava
"""

import pandas as pd
import os
from os import listdir, getcwd
from os.path import join
import glob
import re
import numpy as np


for filename in glob.glob('*.jpg'):
            filename_without_ext = os.path.splitext(filename)[0]
            extension = os.path.splitext(filename)[1]
            if os.path.isfile(filename_without_ext + '.txt'):
                continue
            else:
                data = np.zeros([1,5]).astype(int)
                dataf = pd.DataFrame(data).astype(int)
               # dataf.iloc[0,0] = int(dataf.iloc[0,0])
                #dataf.iloc[0,0] = dataf.iloc[0,0].astype(int)
                dataf.to_csv(filename_without_ext + '.txt', header=None, index=None ,sep=' ')
                print(filename)
            
                
                
                