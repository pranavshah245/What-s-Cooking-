#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 11:15:44 2018

@author: mayur
"""

import pandas as pd
import numpy as np

df = pd.read_csv('/Users/mayur/Documents/GitHub/What-s-Cooking-/'
                      + '2ProcessedData/Train.csv')
   
"""    
c1 = ['thai', 'cajun_creole', 'greek']
for i in range(len(c1)):
    df1 = df[df['cuisine']== c1[i]]
    df = pd.concat([df,df1,df1,df1],ignore_index = True)
"""

c2 = ['spanish', 'jamaican', 'russian', 'irish', 'moroccan', 'korean' , 
      'filipino' , 'vietnamese' , 'british' , 'brazilian', 'japanese']
for i in range(len(c2)):
    df1 = df[df['cuisine']== c2[i]]
    df = pd.concat([df,df1,df1,df1],ignore_index = True)

"""   
c3 = ['french' , 'chinese' , 'indian' ]
for i in range(len(c3)):
    df1 = df[df['cuisine']== c3[i]]
    df = pd.concat([df,df1],ignore_index = True)
 """   

df = df.sample(frac=1).reset_index(drop=True)

import ast
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score


X = df['ingredients']
y = df['cuisine']

X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                    test_size=0.6, random_state=2)




count_vect = CountVectorizer()
X_counts = count_vect.fit_transform(X_train)
X_counts.shape

count_vect.vocabulary_.get(u'algorithm')

from sklearn.feature_extraction.text import TfidfTransformer 
TF = TfidfTransformer()
X_tf = TF.fit_transform(X_counts)
X_tf.shape


from sklearn.naive_bayes import MultinomialNB
clf = MultinomialNB().fit(X_tf, y_train)

 
Xa = count_vect.transform(X_test)
x1 = TF.transform(Xa)

y_pred = clf.predict(x1)

print(accuracy_score(y_test, y_pred))


y_new = df.groupby(['cuisine']).count()
"""
from sklearn import svm
clf_svc = svm.SVC()
m = clf_svc.fit(X_tf, y_train)

clf4 = svm.SVC(decision_function_shape='ovo')
clf4.fit(X_tf, y_train) 
"""
 
Xa = count_vect.transform(X_test)
x1 = TF.transform(Xa)


#a =pd.Series( v[0] for v in X_test)


from sklearn.linear_model import SGDClassifier
clf = SGDClassifier()
clf.fit(X_tf, y_train) 

y_pred = clf.predict(x1)

print(accuracy_score(y_test, y_pred))

from sklearn.linear_model import LogisticRegression
logisticRegr = LogisticRegression()
logisticRegr.fit(X_tf, y_train)

y_pred = logisticRegr.predict(x1)

print(accuracy_score(y_test, y_pred))


"""
from sklearn.model_selection import GridSearchCV
tuned_parameters = [{ 'alpha' : [0.001, 0.01, 0.1, 1, 10, 100],
                     'class_weight' : [None, 'balanced'],
                     'loss' : ['hinge', 'modified_huber' , 'log'],
                     'max_iter' : [10,20,5],
                     'penalty' : ['l1','l2','elasticnet'],
                     'random_state' : [42],
                     'shuffle' : [True]
                     }]
    
clf1 = SGDClassifier()
clf = GridSearchCV(clf1, tuned_parameters, cv=5)

clf.fit(X_tf, y_train)

clf1.get_params().keys()

#my = X[:3]
#[str(x) for x in my]


"""
