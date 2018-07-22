# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 22:17:20 2018

@author: Pranav
"""

# %% Library imports

import pandas as pd
<<<<<<< HEAD
import seaborn as sns
import datetime
import time
=======
import time
import datetime
import seaborn as sns
>>>>>>> 4649d1ad83c9fe6588ce0c770a8b5aa5f742c597
import missingno as msno

# %% Setup paths

<<<<<<< HEAD
path_RawData = "C:/My Data/Projects/Kaggle/What-s-Cooking-/1RawData/"
path_ProcessedData = ("C:/My Data/Projects/Kaggle/What-s-Cooking-/" +
                      "2ProcessedData/")

# path_RawData = "/Users/mayur/Documents/GitHub/What-s-Cooking-/1RawData/"
# path_ProcessedData = ("/Users/mayur/Documents/GitHub/What-s-Cooking-/" +
#                       "2ProcessedData/")

# %% Setup filenames
=======
# Paths for Pranav
path_Base = "C:/My Data/Projects/Kaggle/What-s-Cooking-/"
path_RawData = path_Base+"1RawData/"
path_ProcessedData = path_Base+"2ProcessedData/"

# Paths for Mayur
# path_Base = "/Users/mayur/Documents/GitHub/What-s-Cooking-/"
# path_RawData = path_Base+"1RawData/"
# path_ProcessedData = path_Base+"2ProcessedData/"
>>>>>>> 4649d1ad83c9fe6588ce0c770a8b5aa5f742c597

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
<<<<<<< HEAD
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
=======

print("Total Time to Read the DataFrames: "+str(TotalReadTime)+" seconds.")

# %% Getting the info of the dataframes
>>>>>>> 4649d1ad83c9fe6588ce0c770a8b5aa5f742c597

df_Train.info()
df_Test.info()

# %% Rearranging the columns

<<<<<<< HEAD
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
=======
df_Train = df_Train[["id", "ingredients", "cuisine"]]
df_Test = df_Test[["id", "ingredients"]]

# %% Sorting the dataframe by ID

df_Train.sort_values(by="id", inplace=True)
df_Test.sort_values(by="id", inplace=True)

# %% Resetting the index

df_Train.reset_index(inplace=True, drop=True)
df_Test.reset_index(inplace=True, drop=True)

# %% Checking for missing values

null_ID = df_Train['id'].isnull().sum()
null_Cuisine = df_Train['cuisine'].isnull().sum()
null_Ingredients = df_Train['ingredients'].isnull().sum()

# %% Missing Values Test Case

if(null_ID == null_Cuisine == null_Ingredients and null_Cuisine == 0):
    print("Test Case for Null Values passed")
else:
    print("Null values are supposed to be treated")
    # If Cuisine column is having NaN values more than 30% of the column length
    if null_Cuisine > 0.3*len(df_Train['Cuisine']):
        # Replace it with most frequently occuring cuisine
        df_Train.filna(df_Train['cuisine'].value_counts().idxmax())
    else:
        # Drop those rows
        df_Train.dropna(inplace=True)

# %% Visualizing the NaN presence with plots

sns.set_style("darkgrid")
sns.set_context({"figure.figsize": (15, 8)})
sns.set(font_scale=1.5)
sns.heatmap(df_Train.isnull(), cbar=False)

# %% Other way of visualizing missing values

msno.matrix(df_Train)

# %% Dropping NaNs form Test Data for prediction purpose

length_original = len(df_Test['id'])
df_Test.dropna(inplace=True)
length_treated = len(df_Test['id'])

if(length_original == length_treated):
    print("No Null values removed.")
else:
    print(abs(length_original - length_treated)+" Null values are removed.")

# %% Writing the processed dataframes as a CSV
>>>>>>> 4649d1ad83c9fe6588ce0c770a8b5aa5f742c597

df_Train.to_csv(path_ProcessedData+"Train.csv", index=False)
df_Test.to_csv(path_ProcessedData+"Test.csv", index=False)

# %%
