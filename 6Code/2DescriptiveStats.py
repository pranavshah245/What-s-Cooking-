# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 22:39:28 2018

@author: Pranav
"""


import numpy as np
import pandas as pd
import json



#path_RawData = "C:/My Data/Projects/Kaggle/Whats-Cooking/1RawData/"
#path_ProcessedData = "C:/My Data/Projects/Kaggle/Whats-Cooking/2ProcessedData/"

path_RawData = "/Users/mayur/Documents/GitHub/What-s-Cooking-/1RawData/"
path_ProcessedData = "/Users/mayur/Documents/GitHub/What-s-Cooking-/2ProcessedData/"

filename_Train = "train.json"
filename_Test = "test.json"

df_Train = pd.read_json(path_RawData+filename_Train)
df_Test = pd.read_json(path_RawData+filename_Test)

 

# Resetting the index
# df_Train.set_index("id", inplace=True)
# df_Test.set_index("id", inplace=True)

# Rearrangin the columns
df_Train = df_Train[["id", "ingredients", "cuisine"]]
df_Test = df_Test[["id", "ingredients"]]

y = (df_Train.groupby('cuisine').count())
del y['id']


import matplotlib.pyplot as plt
y.plot.barh()
plt.show()

#d = pd.Series(' '.join(df['col']).split()).value_counts().to_dict()

x = list()
for i in range(10):
    x.append([])
    x[i].append(str(' '.join(df_Train.loc[i]['ingredients'])))
    #x[i].append(str(df_Train.loc[i]['ingredients']))