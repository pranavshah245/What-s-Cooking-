#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 17:05:14 2018

@author: mayur
"""


import pandas as pd
import ast
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score
from sklearn.multiclass import OneVsRestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC
import json

df_train = pd.read_json('/Users/mayur/Documents/GitHub/What-s-Cooking-/1RawData/train.json')
df_test = pd.read_json('/Users/mayur/Documents/GitHub/What-s-Cooking-/1RawData/test.json')


df = df_train[["id", "ingredients", "cuisine"]]
df_Test = df_test[["id", "ingredients"]]

c1 = ['thai', 'cajun_creole', 'greek']
for i in range(len(c1)):
    df1 = df[df['cuisine']== c1[i]]
    df = pd.concat([df,df1,df1,df1],ignore_index = True)


c2 = ['spanish', 'jamaican', 'russian', 'irish', 'moroccan', 'korean' , 
      'filipino' , 'vietnamese' , 'british' , 'brazilian', 'japanese']
for i in range(len(c2)):
    df1 = df[df['cuisine']== c2[i]]
    df = pd.concat([df,df1,df1,df1, df1],ignore_index = True)

   
c3 = ['french' , 'chinese' , 'indian' ]
for i in range(len(c3)):
    df1 = df[df['cuisine']== c3[i]]
    df = pd.concat([df,df1],ignore_index = True)

#i = 1
X_train = list()
for i in range(len(df)):
    X_train.append(' '.join(df['ingredients'][i]))
    
y_train = df['cuisine']
    
from sklearn.feature_extraction.text import TfidfVectorizer
tfidf = TfidfVectorizer(binary = True)


#df['ingredients']= df['ingredients'].apply(
 #       lambda x: ast.literal_eval(x))
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
#X_train, X_test, y_train, y_test = train_test_split(df['ingredients'], 
 #                                                   df['cuisine'],  random_state = 0)

#X_train1 = list()
#X_train = list(X_train)

#[X_train1.append(' '.join(X_train[a])) for a in range(len(X_train))] 
#count_vect = CountVectorizer()
#X_train_counts = count_vect.fit_transform(X_train)
#tfidf_transformer = TfidfTransformer()
#X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
X = tfidf.fit_transform(X_train)

type(X)


lb = LabelEncoder()
y_train = lb.fit_transform(y_train)

classifier = SVC(C=100, 
	 			 kernel='rbf', 
	 			 coef0=1, 
	 			 shrinking=True,
	 			 tol=0.001, 
	      		 probability=False, 
	      		 cache_size=200,
	      		 class_weight=None,
	      		 verbose=False, 
	      		 max_iter=-1, 
          		 decision_function_shape=None,  
          		 random_state=None)
model = OneVsRestClassifier(classifier)

from sklearn.preprocessing import MinMaxScaler
scaling = MinMaxScaler(feature_range=(-1,1)).fit(X)
X = scaling.transform(X)



type(y_train)
model.fit(X, y_train)

X_test = scaling.transform(X_test)
y_pred = model.predict(count_vect.transform(X_test))

print(accuracy_score(y_test, y_pred))
