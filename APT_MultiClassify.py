# encoding: utf-8
from __future__ import division
import random
random.seed(0)
from sklearn.ensemble import RandomForestClassifier as RF
from sklearn import model_selection
from sklearn import tree
from sklearn import metrics
import pandas as pd
import os
import operator
import numpy as np
from collections import *
import xgboost as xgb
from xgboost import plot_importance
from xgboost import plot_tree
import pydotplus
import matplotlib.pyplot as plt
import binascii
import csv
import time
import re
import global_list
from sklearn.ensemble import AdaBoostClassifier as ABC
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier as DTC
from sklearn.naive_bayes import GaussianNB as GNB
from sklearn.svm import SVC as SVM
from sklearn.neighbors import KNeighborsClassifier as KNC
from sklearn import cross_validation
from sklearn.metrics import confusion_matrix

# 取贡献度Top-N
N = global_list.api_Top_N

api_path = os.path.abspath('.') + '/APT_ApiFeature/'
# api_ngram_path = os.path.abspath('.') + '/ApiNgramFeature/'
# pe_path = os.path.abspath('.') + '/PEFeature/'
# network_path = os.path.abspath('.') + '/NetworkFeature/'
# registry_path = os.path.abspath('.') + '/RegistryFeature/'
# file_path = os.path.abspath('.') + '/FileFeature/'
label_path = os.path.abspath('.') + '/Label/'

###########################################################################
subtrainLabel = pd.read_csv(label_path + 'APTLabels.csv')
apifeature = pd.read_csv(api_path + 'APT_apifeature_' + str(N) + '.csv')
# apiCatefeature = pd.read_csv(api_path + "apiCate_Feature.csv")
# api3Gramfeature = pd.read_csv(api_ngram_path + "api3gramfeature.csv")
# sectionfeature = pd.read_csv(pe_path + "section_Feature.csv")
# dllfeature = pd.read_csv(pe_path + "dll_Feature.csv")
# networkfeature = pd.read_csv(network_path + "NetworkFeature.csv")
# registryfeature = pd.read_csv(registry_path + "RegistryFeature.csv")
# filefeature = pd.read_csv(file_path + "FileFeature.csv")
###########################################################################
subtrain = pd.merge(subtrainLabel, apifeature, on='Id')
# subtrain = pd.merge(subtrain, apiCatefeature, on='Id')
# subtrain = pd.merge(subtrain, api3Gramfeature, on='Id')
# subtrain = pd.merge(subtrain, dllfeature, on='Id')
# subtrain = pd.merge(subtrain, sectionfeature, on='Id')
# subtrain = pd.merge(subtrain, networkfeature, on="Id")
# subtrain = pd.merge(subtrain, registryfeature, on="Id")
# subtrain = pd.merge(subtrain, filefeature, on="Id")
###########################################################################
featureset_path = os.path.abspath('.') + '/FeatureSet/'
if not os.path.exists(featureset_path):
    os.makedirs(featureset_path)

df = pd.DataFrame(subtrain)
print "APT_featureset_path:" + featureset_path
df.to_csv(featureset_path + '/' + 'APT_featureset.csv', index = False)
###########################################################################

###########################################################################
labels = subtrainLabel.Class
subtrain.drop(["Class", "Id"], axis = 1, inplace = True)
print "The dimensions of train_dataset:", subtrain.shape
train_X,test_X,train_Y,test_Y=cross_validation.train_test_split(subtrain,labels,test_size=0.1)
############################# 1: Randomforest classifier##################
srf = RF(n_estimators=500, n_jobs=-1)
srf.fit(train_X, train_Y)
print ("The detection results of RandomForest................")
rf_y_pred = srf.predict(test_X)
rf_accuracy = metrics.accuracy_score(test_Y, rf_y_pred)
rf_precision = metrics.precision_score(test_Y, rf_y_pred, average="macro")
rf_recall = metrics.recall_score(test_Y, rf_y_pred, average="macro")
rf_f_score = metrics.f1_score(test_Y, rf_y_pred, average="macro")
print "Accuracy: %f" %rf_accuracy
print "Precision: %f" %rf_precision
print "Recall: %f" %rf_recall
print "F1 score: %f" %rf_f_score

############################ 2: Decision tree classifier ################
dt = DTC(criterion="gini", splitter="best")
dt.fit(train_X, train_Y)
print("The detection results of DecisionTree..................")
dt_y_pred = dt.predict(test_X)
dt_accuracy = metrics.accuracy_score(test_Y, dt_y_pred)
dt_precision = metrics.precision_score(test_Y, dt_y_pred, average="macro")
dt_recall = metrics.recall_score(test_Y, dt_y_pred, average="macro")
dt_f_score = metrics.f1_score(test_Y, dt_y_pred, average="macro")
print "Accuracy: %f" %dt_accuracy
print "Precision: %f" %dt_precision
print "Recall: %f" %dt_recall
print "F1 score: %f" %dt_f_score

############################ 3: KNeighborsClassifier $$$$$$$$$$$$$$$$$$$$$$
knc = KNC()
knc.fit(train_X, train_Y)
print("The detection results of KNN....................")
knc_y_pred = knc.predict(test_X)
knc_accuracy = metrics.accuracy_score(test_Y, knc_y_pred)
knc_precision = metrics.precision_score(test_Y, knc_y_pred, average="macro")
knc_recall = metrics.recall_score(test_Y, knc_y_pred, average="macro")
knc_f_score = metrics.f1_score(test_Y, knc_y_pred, average="macro")
print "Accuracy: %f" %knc_accuracy
print "Precision: %f" %knc_precision
print "Recall: %f" %knc_recall
print "F1 score: %f" %knc_f_score

######################################## 4: XGBoost ########################################
xg_train = xgb.DMatrix(train_X, label=train_Y)
xg_test = xgb.DMatrix(test_X, label=test_Y)
# setup parameters for xgboost
param = {}
# use softmax multi-class classification
param['objective'] = 'multi:softmax'
# scale weight of positive examples
param['eta'] = 0.1
param['max_depth'] = 15
param['silent'] = 1
param['nthread'] = 4
param['num_class'] = 6
param['colsample_bytree'] = 1
param['subsample'] = 1
watchlist = [(xg_train, 'train'), (xg_test, 'test')]
num_round = 20
bst = xgb.train(param, xg_train, num_round, watchlist)
xgbst_y_pred = bst.predict(xg_test)
xgbst_accuracy = metrics.accuracy_score(test_Y, xgbst_y_pred)
xgbst_precision = metrics.precision_score(test_Y, xgbst_y_pred, average="macro")
xgbst_recall = metrics.recall_score(test_Y, xgbst_y_pred, average="macro")
xgbst_f_score = metrics.f1_score(test_Y, xgbst_y_pred, average="macro")
print "Accuracy: %f" %xgbst_accuracy
print "Precision: %f" %xgbst_precision
print "Recall: %f" %xgbst_recall
print "F1 score: %f" %xgbst_f_score