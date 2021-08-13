# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 16:51:44 2021

@author: HP
"""
import matplotlib.pyplot as plt
import seaborn as sns 
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.model_selection import train_test_split
from sklearn import metrics, tree
from sklearn.metrics import confusion_matrix, classification_report


url= 'https://raw.githubusercontent.com/DUanalytics/datasets/master/csv/diabetes.csv'
data= pd.read_csv(url)
data
data.head()
data.columns
data.shape
data.Outcome.value_counts()

data.groupby('Outcome').aggregate({'Glucose':np.mean,'BMI':np.mean,'Age':np.mean})

X= data.drop('Outcome',axis=1)
Y= data['Outcome']
X

#split
X_train, X_test, Y_train, Y_test= train_test_split(X,Y,test_size=0.3, random_state=1)
X_train.shape
X_test
X_train.head()

clf= DecisionTreeClassifier()

#Train decision tree classifier
clf= clf.fit(X_train,Y_train)
Y_train
            
#predict the response for the test dataset  
y_pred = clf.predict(X_test)
y_pred           
        
#accuracy
print('Accuracy:',metrics.accuracy_score(Y_test, y_pred))     
cm= confusion_matrix(Y_test,y_pred)
print(cm)  

print(classification_report(Y_test,y_pred))
           
#prune tree- make tree shorter by cutting the branches
dtree= DecisionTreeClassifier(criterion='entropy', max_depth=2)
dtree.fit(X_train,Y_train)
pred2 = dtree.predict(X_test)
print('Accuracy:',metrics.accuracy_score(Y_test,pred2))
print(classification_report(Y_test,pred2))

text_representation2 = tree.export_text(dtree,feature_names=['Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age'],max_depth=2)
print(text_representation2)


data.columns
text_representation3 = tree.export_text(dtree, feature_names=['Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age'], decimals=0, show_weights= True, max_depth=3)
print(text_representation3)

#import, summary, split, model on train set, prediction of test set, confusion matrix, accuracy, predict on new or unknown data


             
             