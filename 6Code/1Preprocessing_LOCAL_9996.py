# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 22:17:20 2018

@author: Pranav
"""

# %% Library imports

import pandas as pd
import seaborn as sns
import datetime
import time
import missingno as msno

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

# %% Visualizing the head of the dataframe

df_Train.head()
df_Test.head()

# %% Rearrangin the columns

df_Train = df_Train[["id", "ingredients", "cuisine"]]
df_Test = df_Test[["id", "ingredients"]]

# %% Sorting the dataframe by ID

df_Train.sort_values(by="id", inplace=True)
df_Test.sort_values(by="id", inplace=True)

# %% Preprocessing the dataframes

# Resetting the index
# df_Train.set_index("id", inplace=True)
# df_Test.set_index("id", inplace=True)

# %% Resetting the index

df_Train.reset_index(drop=True, inplace=True)
df_Test.reset_index(drop=True, inplace=True)

# %% Checking for missing values/Imputation if necessarry

# Setup some general style parameters for the plot.
sns.set_style("darkgrid")
sns.set_context({"figure.figsize": (15, 15)})
sns.set(font_scale=2)

# Heatmap to visualize missing values (if any)
sns.heatmap(df_Train.isnull(), cbar=False)

# %% Missing number matrix to visualize missing values (if any)

msno.matrix(df_Train)
msno.matrix(df_Test)

# %% Saving the processed dataframe as a CSV

df_Train.to_csv(path_ProcessedData+"Train.csv", index=False)
df_Test.to_csv(path_ProcessedData+"Test.csv", index=False)

# %%
