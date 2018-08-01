#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 11:07:42 2018

@author: mayur
"""

import pandas as pd
import ast

df = pd.read_csv('/Users/mayur/Documents/GitHub/What-s-Cooking-/'
                      + '2ProcessedData/Train.csv')



from sklearn.feature_extraction.text import CountVectorizer
count_vect = CountVectorizer()
X_counts = count_vect.fit_transform(df.ingredients)
X_counts.shape

count_vect.vocabulary_.get(u'algorithm')

from sklearn.feature_extraction.text import TfidfTransformer 
TF = TfidfTransformer()
X_tf = TF.fit_transform(X_counts)
X_tf.shape

from sklearn.naive_bayes import MultinomialNB
clf = MultinomialNB().fit(X_tf, df.cuisine)

#docs_new = [str( """ 'pepper', 'oil', 'baking powder', 'onions', 'eggs', 'salt', 'potatoes', 'garlic cloves''"""), str("""'oysters', 'clam juice', 'chopped celery', 'okra', 'medium shrimp', 'bay leaves', 'diced tomatoes', 'hot sauce', 'garlic cloves', 'chopped green bell pepper', 'cajun seasoning', 'all-purpose flour', 'long-grain rice', 'vegetable oil', 'bacon slices', 'chopped onion', 'hot water'""")]

df_test = df = pd.read_csv('/Users/mayur/Documents/GitHub/What-s-Cooking-/'
                      + '2ProcessedData/Test.csv')
 
X = count_vect.transform(df_test.ingredients)
x1 = TF.transform(X)

y = clf.predict(x1)
y1 = list(y)

submission_df = pd.DataFrame(columns = ['id', 'cuisine'])
submission_df['id']=df_test['id']
submission_df['cuisine']=y1

submission_df.to_csv('Result1trial.csv', index = False)