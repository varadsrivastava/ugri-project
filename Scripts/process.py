# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 22:03:52 2019

@author: Varad Srivastava
"""

import pandas as pd
import os
from os import listdir, getcwd
from os.path import join
import glob
import pandas as pd
import numpy as np

read_path = 'D:\Datasets\action\Train-Set\Labels\SingleActionLabels\3840x2160'

#for filename in glob.glob('*.csv'):
filename = '1.2.11.csv'
filename_without_ext = os.path.splitext(filename)[0]
extension = os.path.splitext(filename)[1]
x = pd.read_csv(filename, header=None)
x = x.drop([0,7,8,9,10,11], axis = 1)                
for row in range(x.shape[0]) :
    if x.loc[row,6] == 1 :
            x = x.drop([row],axis=0)
x = x.drop([6], axis = 1)    
x.insert(0, 0, 0) 
x = x.sort_values(5)
x = x.reset_index(drop = True)
#i = 0
#j = 1
x.shape[0]
#for row in range(i, x.shape[0],1) :
    #for rowb in range(j, x.shape[0],1):
r1 = range(0, x.shape[0] + 1)
r2 = range(1, x.shape[0] + 1)     
for i in r1:
    for j in r2:
        if j == x.shape[0] :
                y = str(x.iloc[i,5])
                m = x.iloc[i:j ,:-1]
                m.to_csv(filename_without_ext + "." + y + ".csv", index = False, header = False)
                
        elif x.iloc[i,5] == x.iloc[j,5]:
            j = j + 1
        
        else:
            y = str(x.iloc[i,5])
            m = x.iloc[i:j ,:-1]
            i = j
            j = j + 1
            m.to_csv(filename_without_ext + "." + y + ".csv", index = False, header = False)
            
            
            
    #x.index( x.iloc[row,5] ==  x.iloc[rowb,5])
    
#for rows in range(x.shape[0]) where x.iloc[row,5]
    
#y = str(x.iloc[row,5])

    
             
            

        
                   
   
    