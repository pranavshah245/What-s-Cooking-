#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 16:16:30 2018

@author: mayur
"""


# Import the required libraries 
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.multiclass import OneVsRestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC
import pandas as pd
import json


print ("Read Dataset ... ")
def read_dataset(path):
	return json.load(open(path)) 
train = read_dataset('/Users/mayur/Documents/GitHub/What-s-Cooking-/1RawData/train.json')
test = read_dataset('/Users/mayur/Documents/GitHub/What-s-Cooking-/1RawData/test.json')

print ("Prepare text data of Train and Test ... ")
def generate_text(data):
	text_data = [" ".join(doc['ingredients']).lower() for doc in data]
	return text_data 




train_text = generate_text(train)
test_text = generate_text(test)
target = [doc['cuisine'] for doc in train]

# Feature Engineering 
print ("TF-IDF on text data ... ")
tfidf = TfidfVectorizer(binary=True)
def tfidf_features(txt, flag):
    if flag == "train":
    	x = tfidf.fit_transform(txt)
    else:
	    x = tfidf.transform(txt)
    x = x.astype('float16')
    return x 

X = tfidf_features(train_text, flag="train")
X_test = tfidf_features(test_text, flag="test")
type(X)
# Label Encoding - Target 
print ("Label Encode the Target Variable ... ")
lb = LabelEncoder()
y = lb.fit_transform(target)
type(y)
# Model Training 
print ("Train the model ... ")
"""
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
"""

import xgboost as xgb

params = {
    # Parameters that we are going to tune.
    'max_depth': 8, #Result of tuning with CV
    'eta':.03, #Result of tuning with CV
    'subsample': 1, #Result of tuning with CV
    'colsample_bytree': 0.8, #Result of tuning with CV
    # Other parameters
    'objective':'reg:linear',
    'eval_metric':'rmse',
    'silent': 1
}
# params by Jesús Ros XGBoost'ing Taxi Fares
from xgboost import XGBClassifier
model = XGBClassifier()
model=XGBClassifier(learning_rate=0.1,n_estimators=100)






model.fit(X, y)

# Predictions 
print ("Predict on test data ... ")
y_test = model.predict(X_test)
y_pred = lb.inverse_transform(y_test)

# Submission
print ("Generate Submission File ... ")
test_id = [doc['id'] for doc in test]
sub = pd.DataFrame({'id': test_id, 'cuisine': y_pred}, columns=['id', 'cuisine'])
sub.to_csv('svm_output.csv', index=False)