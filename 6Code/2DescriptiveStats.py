# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 22:39:28 2018

@author: Pranav
"""

# %% Library imports

import numpy as np
import pandas as pd
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

filename_Train = "train.json"
filename_Test = "test.json"

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
