# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 22:17:20 2018

@author: Pranav
"""

# %% Library imports

import numpy as np
import pandas as pd
import json

# %% Setup path and file names

#path_RawData = "C:/My Data/Projects/Kaggle/Whats-Cooking/1RawData/"
#path_ProcessedData = "C:/My Data/Projects/Kaggle/Whats-Cooking/2ProcessedData/"

path_RawData = "/Users/mayur/Documents/GitHub/What-s-Cooking-/1RawData/"
path_ProcessedData = "/Users/mayur/Documents/GitHub/What-s-Cooking-/2ProcessedData/"

filename_Train = "train.json"
filename_Test = "test.json"

# %% Load Data

df_Train = pd.read_json(path_RawData+filename_Train)
df_Test = pd.read_json(path_RawData+filename_Test)

# %% Preprocessing the dataframes

# Resetting the index
# df_Train.set_index("id", inplace=True)
# df_Test.set_index("id", inplace=True)

# Rearrangin the columns
df_Train = df_Train[["id", "ingredients", "cuisine"]]
df_Test = df_Test[["id", "ingredients"]]

# Sorting the dataframe by ID
df_Train = df_Train.sort_values(by="id")
df_Test = df_Test.sort_values(by="id")

df_Train.head()

# Checking for missing values/Imputation if necessarry

# %%
