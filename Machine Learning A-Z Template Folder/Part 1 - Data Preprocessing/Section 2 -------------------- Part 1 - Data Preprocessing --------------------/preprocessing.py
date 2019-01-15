# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 00:07:22 2018

@author: Anurag
"""
#importing the libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#acquiring the dataset
dataset=pd.read_csv('Data.csv') #read the dataset
X=dataset.iloc[:,:-1].values
y=dataset.iloc[:,3].values   #before comma indicates all the lines and after comma indicated last colomn is not included


#Deal with missing values
from sklearn.preprocessing import Imputer
#missing_value specifies NaN bcaz it is in csv file
imputer=Imputer(missing_values='NaN',strategy='mean',axis=0)

#identify which colomns contain missing colomns 
imputer=imputer.fit(X[:,1:3])
#replace missing colomn data by mean
X[:,1:3]=imputer.transform(X[:,1:3])


#Encoding categorical data
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
labelencoder_X=LabelEncoder()
X[:,0]=labelencoder_X.fit_transform(X[:,0])
onehotencoder=OneHotEncoder(categorical_features=[0])
X=onehotencoder.fit_transform(X).toarray() 

labelencoder_y=LabelEncoder()
y=labelencoder_y.fit_transform(y)


#splitting into training and test data set
from sklearn.cross_validation import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=0) 
