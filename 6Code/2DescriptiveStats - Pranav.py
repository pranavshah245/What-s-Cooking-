# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 22:39:28 2018

@author: Pranav
"""

#  Library imports

import pandas as pd
import time
import datetime
import seaborn as sns
import matplotlib.pyplot as plt
import ast

# User defined modules
import ssaplot as ssa

#  Setup path and file names

# Paths for Pranav
#path_Base = "C:/My Data/Projects/Kaggle/What-s-Cooking-/"
#path_ProcessedData = path_Base+"2ProcessedData/"
"""
path_Base = "C:/My Data/Projects/Kaggle/What-s-Cooking-/"
path_ProcessedData = ("C:/My Data/Projects/Kaggle/What-s-Cooking-/" +
                      "2ProcessedData/")


path_Insights = path_Base+"3Insights/"
"""
# Paths for Mayur
path_Base = "/Users/mayur/Documents/GitHub/What-s-Cooking-/"
path_ProcessedData = path_Base+"2ProcessedData/"
path_Insights = path_Base+"3Insights/"

filename_Train = "Train.csv"
filename_Test = "Test.csv"

#  Load Data

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

#  Checking the column fetaures

list_cusinies = list(df_Train['cuisine'].unique())
freq_cuisines = df_Train['cuisine'].value_counts()

#  Visualizing the column features

sns.set_style("darkgrid")
sns.set_context({"figure.figsize": (15, 8)})
sns.set(font_scale=2)
ax = sns.countplot(df_Train['cuisine'])
ax.set_xlabel("Cuisines", fontsize=18)
ax.set_ylabel("Number of Records", fontsize=18)
ax.set_xticklabels(labels=list_cusinies, rotation=90)
ax.legend(loc="upper right")
ax.text(.75, .9, "Total Records: "+str(len(df_Train)), fontsize=16,
        horizontalalignment='left', verticalalignment='center',
        transform=ax.transAxes)
ssa.annotate(ax, location='Top', message='Count', fontsize=12)
ssa.annotate(ax, location='Middle', message='Percentage', fontsize=12)
plt.title("Number of Records for each Cuisine", fontsize=18)
plt.tight_layout()
plt.savefig(path_Insights+"Number of Records for each Cuisine.png")
plt.show()
plt.clf()

#  Refactoring 'ingredients' column

df_Train['ingredients'] = df_Train['ingredients'].apply(
        lambda x: ast.literal_eval(x))

df_Train['NumberOfIngredients'] = df_Train['ingredients'].apply(
        lambda x: len(x))


#  Function to slice the dataframe by cuisine type

def sliceByCuisine(df, cuisine='indian'):
    """
    This function slices dataframe by the type of cuisine mentioned
    as an argument.

    Arguments:
        df (pandas.DataFrame): The dataframe to be sliced.
                               Normally it would be the training data.

        cuisine (str): The type of the cuisine to be sliced from the
                       dataframe 'df'. Default value is set to 'indian'.

    Returns:
        df_return (pandas.DataFrame): The dataframe containing records only
                                      for that particular cuisine.

    Examples:
        sliceByCuisine(df_Train, cuisine='italian')
    """
    # Slice it by cuisine type and process the indices.
    df_return = df[df['cuisine'] == cuisine]
    df_return.sort_values(by="id", inplace=True)
    df_return.reset_index(inplace=True, drop=True)

    # Return the dataframe
    return(df_return)


#  Function to create a dataframe with these Ingredients & their counts.

def ingredients(df):
    """
    This function will generate a dataframe having information about
    the ingredients and their frequencies in the passed dataframe.

     Arguments:
        df (pandas.DataFrame): The dataframe for extraction of
                               ingredients information.

    Returns:
        df_ingredients (pandas.DataFrame): The dataframe of 2 columns.
                                           'Ingredient': Column of unique
                                                         ingredients.
                                            'Count': Their respective counts.

    Examples:
        ingredients(df_Train)
        ingredients(df_Mexican)
    """
    # Creating an empty list to store ingredients
    list_ingredients = list()

    # Iterating to combine all ingredients in one list
    for idx, val in enumerate(df['ingredients']):
        list_ingredients.extend(df.loc[idx, 'ingredients'])

    # Unique elements of the above list
    set_ingredients = set(list_ingredients)

    # Setting up the dataframe to return
    df_ingredients = pd.DataFrame(columns=['Ingredient', 'Count'])
    df_ingredients['Ingredient'] = list(set(list_ingredients))
    df_ingredients.sort_values(by="Ingredient", inplace=True)

    # Iterating to get the ingredient count
    for item in list(set_ingredients):
        index = df_ingredients[df_ingredients['Ingredient'] == item].index[0]
        df_ingredients.loc[index, 'Count'] = list_ingredients.count(item)

    # Sorting the dataframe in descending order of Counts
    df_ingredients.sort_values(by="Count", ascending=False, inplace=True)
    df_ingredients.reset_index(inplace=True, drop=True)

    # Return the dataframe
    return(df_ingredients)


#  Function to visualize Top-10 ingredients of a given cuisine

def top10plot(df, cuisine):
    """
    This function plots the Counts of Top-10 ingredients for a given cuisine.

    Arguments:
        df (pandas.DataFrame): The dataframe whose plot is to be made.

        cuisine (str): The type of the cuisine to be visualized.
                       Used for plot title and saving the image.

    Returns: None

    Examples:
        top10plot(df_Italian, cuisine='italian')
        top10plot(df_Train, cuisine='all')
    """
    sns.set_style("darkgrid")
    sns.set_context({"figure.figsize": (15, 8)})
    sns.set(font_scale=2)
    ax = sns.barplot(x='Ingredient', y='Count', data=df[:10])
    ax.set_xlabel("Ingredients", fontsize=18)
    ax.set_ylabel("Frequency", fontsize=18)
    ax.set_xticklabels(labels=list(df['Ingredient'][:10]), rotation=90)
    ax.legend(loc="upper right")
    ax.text(.75, .9, "Total Ingredients: "+str(len(df)), fontsize=16,
            horizontalalignment='left', verticalalignment='center',
            transform=ax.transAxes)
    ax.text(.75, .8, "Total Occurrences: "+str(sum(df['Count'])), fontsize=16,
            horizontalalignment='left', verticalalignment='center',
            transform=ax.transAxes)
    ssa.annotate(ax, location='Top', message='Count', fontsize=12)
    ssa.annotate(ax, location='Middle', message='Percentage', fontsize=12)
    plt.title("Number of Records for Top-10 Ingredients for " +
              cuisine+" cuisine.", fontsize=18)
    plt.tight_layout()
    plt.savefig(path_Insights+"Number of Records for Top-10 Ingredients for " +
                cuisine+" cuisine.png")
    plt.show()
    plt.clf()

#  Visualizing the Top-10 ingredients for the different dataframes

top10plot(ingredients(df_Train), cuisine='all')
top10plot(ingredients(sliceByCuisine(df_Train)), cuisine='indian')
top10plot(ingredients(sliceByCuisine(df_Train, cuisine='mexican')),
          cuisine='mexican')
top10plot(ingredients(sliceByCuisine(df_Train, cuisine='italian')),
          cuisine='italian')

#  Saving the dataframe of individual ingredients for all cuisines as a CSV

#ingredients(df_Train).to_csv(path_ProcessedData+"Ingredients.csv", index=False)

# 
