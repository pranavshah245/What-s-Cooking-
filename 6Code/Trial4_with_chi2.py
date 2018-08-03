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

df = pd.read_csv('/Users/mayur/Documents/GitHub/What-s-Cooking-/'
                      + '2ProcessedData/Train.csv')

def generate_text(data):
	text_data = [" ".join(doc['ingredients']).lower() for doc in data]
	return text_data 

X_train = generate_text(df)
X_test = generate_text(X_test)
  
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
   
from sklearn.feature_extraction.text import TfidfVectorizer
tfidf = TfidfVectorizer(binary = True)
features = tfidf.fit_transform(df.ingredients).toarray()
labels = df.cuisine
features.shape


from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
X_train, X_test, y_train, y_test = train_test_split(df['ingredients'], 
                                                    df['cuisine'],  random_state = 0)


#count_vect = CountVectorizer()
#X_train_counts = count_vect.fit_transform(X_train)
#tfidf_transformer = TfidfTransformer()
#X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
X = tfidf.fit_transform(X_train)

"""
clf = MultinomialNB(alpha = 1).fit(X_train_tfidf, y_train)

print('size of train data : ' + str(len(X_train)))

y_pred = clf.predict(count_vect.transform(X_test))

print(accuracy_score(y_test, y_pred))

from sklearn.svm import SVC
clf_svm = SVC()
clf_svm.fit(X_train_tfidf, y_train)

y_pred = clf_svm.predict(count_vect.transform(X_test))

print(accuracy_score(y_test, y_pred))



from sklearn.model_selection import cross_val_score
scores = cross_val_score(clf, X_train_tfidf, y_train, cv=18)
scores 

from sklearn.model_selection import StratifiedKFold
skf = StratifiedKFold(n_splits=3)
"""
lb = LabelEncoder()
y_train = lb.fit_transform(y_train)

classifier = SVC(C=100, # penalty parameter, setting it to a larger value 
	 			 kernel='rbf', # kernel type, rbf working fine here
	 			 degree=3, # default value, not tuned yet
	 			 gamma=1, # kernel coefficient, not tuned yet
	 			 coef0=1, # change to 1 from default value of 0.0
	 			 shrinking=True, # using shrinking heuristics
	 			 tol=0.001, # stopping criterion tolerance 
	      		 probability=False, # no need to enable probability estimates
	      		 cache_size=200, # 200 MB cache size
	      		 class_weight=None, # all classes are treated equally 
	      		 verbose=False, # print the logs 
	      		 max_iter=-1, # no limit, let it run
          		 decision_function_shape=None, # will use one vs rest explicitly 
          		 random_state=None)
model = OneVsRestClassifier(classifier, n_jobs=4)
type(y_train)
model.fit(X, y_train)


y_pred = model.predict(count_vect.transform(X_test))

print(accuracy_score(y_test, y_pred))
