# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 22:39:28 2018

@author: Pranav
"""

# %% Library imports

import pandas as pd
import time
import datetime
import seaborn as sns
import ssaplot as ssa
import matplotlib.pyplot as plt

# %% Setup path and file names

# Paths for Pranav
path_Base = "C:/My Data/Projects/Kaggle/What-s-Cooking-/"
path_ProcessedData = path_Base+"2ProcessedData/"
path_Insights = path_Base+"3Insights/"

# Paths for Mayur
# path_Base = "/Users/mayur/Documents/GitHub/What-s-Cooking-/"
# path_ProcessedData = path_Base+"2ProcessedData/"
# path_Insights = path_Base+"3Insights/"

filename_Train = "Train.csv"
filename_Test = "Test.csv"

# %% Load Data

print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
      "Start of Reading the Dataframe")
StartReadTime = time.time()

df_Train = pd.read_csv(path_ProcessedData+filename_Train)
df_Test = pd.read_csv(path_ProcessedData+filename_Test)

EndReadTime = time.time()
TotalReadTime = round((EndReadTime - StartReadTime), 2)
print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
      "End of Reading the Dataframe")

print("Total Time to Read the DataFrames: "+str(TotalReadTime)+" seconds.")

# %% Checking the column fetaures

list_cusinies = list(df_Train['cuisine'].unique())
freq_cuisines = df_Train['cuisine'].value_counts()

# %% Visualizing the column features

sns.set_style("darkgrid")
sns.set_context({"figure.figsize": (15, 8)})
sns.set(font_scale=2)
ax = sns.countplot(df_Train['cuisine'])
ax.set_xlabel("Cuisines", fontsize=18)
ax.set_ylabel("Number of Records", fontsize=18)
ax.set_xticklabels(labels=list_cusinies, rotation=90)
ax.legend(loc="upper right")
ssa.annotate(ax, location='Top', message='Count', fontsize=12)
ssa.annotate(ax, location='Middle', message='Percentage', fontsize=12)
plt.title("Number of Records for each Cuisine", fontsize=18)
plt.tight_layout()
plt.savefig(path_Insights+"Number of Records for each Cuisine.png")
plt.show()
plt.clf()

# %% Refactoring 'ingredients' column

df_Train['NumberOfIngredients'] = df_Train['ingredients'].apply(
        lambda x: len(x))


