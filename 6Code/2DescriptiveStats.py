# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 22:39:28 2018

@author: Pranav
"""

# %% Library imports

import pandas as pd


# %% Setup paths

path_RawData = "C:/My Data/Projects/Kaggle/What-s-Cooking-/1RawData/"
path_ProcessedData = ("C:/My Data/Projects/Kaggle/What-s-Cooking-/" +
                      "2ProcessedData/")

# path_RawData = "/Users/mayur/Documents/GitHub/What-s-Cooking-/1RawData/"
# path_ProcessedData = ("/Users/mayur/Documents/GitHub/What-s-Cooking-/" +
#                       "2ProcessedData/")

# %% Setup filenames

# Paths for Pranav
# path_Base = "C:/My Data/Projects/Kaggle/What-s-Cooking-/"
# path_RawData = path_Base+"1RawData/"
# path_ProcessedData = path_Base+"2ProcessedData/"

# Paths for Mayur
path_Base = "/Users/mayur/Documents/GitHub/What-s-Cooking-/"
path_RawData = path_Base+"1RawData/"
path_ProcessedData = path_Base+"2ProcessedData/"

filename_Train = "train.json"
filename_Test = "test.json"

# %%

df_Train = pd.read_json(path_RawData+filename_Train)
df_Test = pd.read_json(path_RawData+filename_Test)

# Rearrangin the columns
df_Train = df_Train[["id", "ingredients", "cuisine"]]
df_Test = df_Test[["id", "ingredients"]]

# visualizing frequency of each cuisine by grouping them together
y = (df_Train.groupby('cuisine').count())
del y['id']


import matplotlib.pyplot as plt
y.plot.barh()
plt.show()

# ....Visualizing most common ingredients among all cuisine
from collections import Counter
counterForIngredients = Counter()
for i in range(len(df_Train)):
    counterForIngredients.update(df_Train.loc[i][1])

counterMostCommon = counterForIngredients.most_common(12)

x, y = zip(*counterMostCommon)

ax = plt.subplot()
ax.barh(x,y)
plt.show()

