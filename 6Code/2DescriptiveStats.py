# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 22:39:28 2018

@author: Pranav
"""

# %% Library imports

import numpy as np
import pandas as pd
<<<<<<< HEAD
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
import time
import missingno as msno

# User defined modules
import ssaplot as ssa

# %% Setup paths

path_RawData = "C:/My Data/Projects/Kaggle/What-s-Cooking-/1RawData/"
path_ProcessedData = ("C:/My Data/Projects/Kaggle/What-s-Cooking-/" +
                      "2ProcessedData/")

# path_RawData = "/Users/mayur/Documents/GitHub/What-s-Cooking-/1RawData/"
# path_ProcessedData = ("/Users/mayur/Documents/GitHub/What-s-Cooking-/" +
#                       "2ProcessedData/")

# %% Setup filenames
=======
import json



# Paths for Pranav
# path_Base = "C:/My Data/Projects/Kaggle/What-s-Cooking-/"
# path_RawData = path_Base+"1RawData/"
# path_ProcessedData = path_Base+"2ProcessedData/"

# Paths for Mayur
path_Base = "/Users/mayur/Documents/GitHub/What-s-Cooking-/"
path_RawData = path_Base+"1RawData/"
path_ProcessedData = path_Base+"2ProcessedData/"
>>>>>>> 4649d1ad83c9fe6588ce0c770a8b5aa5f742c597

filename_Train = "train.json"
filename_Test = "test.json"

<<<<<<< HEAD
# %% Load Data

print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
      "Start of Reading the Dataframe")
StartReadTime = time.time()

df_Train = pd.read_json(path_RawData+filename_Train)
df_Test = pd.read_json(path_RawData+filename_Test)

EndReadTime = time.time()
TotalReadTime = round((EndReadTime - StartReadTime), 2)
print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
      "End of Reading the Dataframe")
print("Total Time to Read the DataFrame: "+str(TotalReadTime)+" seconds.")

# %% Descriptive stats to visualize the data











# %%
=======
df_Train = pd.read_json(path_RawData+filename_Train)
df_Test = pd.read_json(path_RawData+filename_Test)



# Resetting the index
# df_Train.set_index("id", inplace=True)
# df_Test.set_index("id", inplace=True)

# Rearrangin the columns
df_Train = df_Train[["id", "ingredients", "cuisine"]]
df_Test = df_Test[["id", "ingredients"]]


#.....visualizing frequency of each cuisine by grouping them together
y = (df_Train.groupby('cuisine').count())
del y['id']


import matplotlib.pyplot as plt
y.plot.barh()
plt.show()


#
###.....Visualizing most common ingredients among all cuisine
from collections import Counter
counterForIngredients = Counter()
for i in range(len(df_Train)):
    counterForIngredients.update(df_Train.loc[i][1])

counterMostCommon= counterForIngredients.most_common(10)

x, y = zip(*counterMostCommon)

ax = plt.subplot()
ax.barh(x,y)
plt.show()

>>>>>>> 4649d1ad83c9fe6588ce0c770a8b5aa5f742c597
