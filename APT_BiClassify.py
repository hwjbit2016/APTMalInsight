# -*- coding: utf-8 -*-
from __future__ import division
import random
random.seed(0)
from sklearn.ensemble import RandomForestClassifier as RF
from sklearn import model_selection
from sklearn import tree
from sklearn import metrics
import pandas as pd
import os
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
from matplotlib import mlab
from matplotlib import rcParams

# 取贡献度Top-N
N = global_list.api_Top_N


api_path = os.path.abspath('.') + '/ApiFeature/'
# api_ngram_path = os.path.abspath('.') + '/ApiNgramFeature/'
# pe_path = os.path.abspath('.') + '/PEFeature/'
# network_path = os.path.abspath('.') + '/NetworkFeature/'
# registry_path = os.path.abspath('.') + '/RegistryFeature/'
# file_path = os.path.abspath('.') + '/FileFeature/'
label_path = os.path.abspath('.') + '/Label/'

featureset_path = os.path.abspath('.') + '/FeatureSet/'
if not os.path.exists(featureset_path):
    os.makedirs(featureset_path)

###########################################################################
subtrainLabel = pd.read_csv(label_path + 'PartLabels.csv')
apifeature = pd.read_csv(api_path + 'apifeature_' + str(N) + '.csv')
# apiCatefeature = pd.read_csv(api_path + "apiCate_Feature.csv")
# api3Gramfeature = pd.read_csv(api_ngram_path + "api3gramfeature.csv")
# sectionfeature = pd.read_csv(pe_path + "section_Feature.csv")
# dllfeature = pd.read_csv(pe_path + "dll_Feature.csv")
# importsfeature = pd.read_csv(pe_path + "imports_Feature.csv")
# networkfeature = pd.read_csv(network_path + "NetworkFeature2.csv")
# registryfeature = pd.read_csv(registry_path + "RegistryFeature2.csv")
# filefeature = pd.read_csv(file_path + "FileFeature2.csv")

###########################################################################
# subtrain = pd.merge(subtrainLabel, sectionfeature, on='Id')
subtrain = pd.merge(subtrainLabel, apifeature, on='Id')
# subtrain = pd.merge(subtrain, apiCatefeature, on='Id')
# subtrain = pd.merge(subtrain, api3Gramfeature, on='Id')
# subtrain = pd.merge(subtrain, dllfeature, on='Id')
# subtrain = pd.merge(subtrain, sectionfeature, on='Id')
# # # subtrain = pd.merge(subtrain, importsfeature, on='Id')
# subtrain = pd.merge(subtrain, networkfeature, on="Id")
# subtrain = pd.merge(subtrain, registryfeature, on="Id")
# subtrain = pd.merge(subtrain, filefeature, on="Id")

labels = subtrainLabel.Class
df = pd.DataFrame(subtrain)
print "featureset_path:" + featureset_path
df.to_csv(featureset_path + '/' + 'featureset.csv', index = False)
###########################################################################
###########################################################################
subtrain.drop(["Class", "Id"], axis = 1, inplace = True)
print "The dimensions of train_dataset:", subtrain.shape
train_X,test_X,train_Y,test_Y=cross_validation.train_test_split(subtrain,labels,test_size=0.1)
############################# 1: Randomforest classifier##################
srf = RF(n_estimators=500, n_jobs=-1)
srf.fit(train_X, train_Y)
dr_rf = srf.score(test_X, test_Y)
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
print '\n'


############################ 2: Decision tree classifier ################
dt = DTC(criterion="gini", splitter="best")
dt.fit(train_X, train_Y)
dr_dt = dt.score(test_X, test_Y)
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
print '\n'


# 3: Gaussian Naive Bayes
gnb = GNB()
gnb.fit(train_X, train_Y)
dr_nb = gnb.score(test_X, test_Y)
print("The detection results of NaiveBayes....................")
gnb_y_pred = gnb.predict(test_X)
gnb_accuracy = metrics.accuracy_score(test_Y, gnb_y_pred)
gnb_precision = metrics.precision_score(test_Y, gnb_y_pred, average="macro")
gnb_recall = metrics.recall_score(test_Y, gnb_y_pred, average="macro")
gnb_f_score = metrics.f1_score(test_Y, gnb_y_pred, average="macro")
print "Accuracy: %f" %gnb_accuracy
print "Precision: %f" %gnb_precision
print "Recall: %f" %gnb_recall
print "F1 score: %f" %gnb_f_score
print '\n'


# 4: Support vector machine
# svm_classifer = SVC(kernel= "linear")
# svm_classifer.fit(train_X, train_Y)
# dr_svm = svm_classifer.score(test_X, test_Y)
# print("The detection rate of Support Vector Machine:", dr_svm)

############################ 4: KNeighborsClassifier $$$$$$$$$$$$$$$$$$$$$$
knc = KNC()
knc.fit(train_X, train_Y)
dr_knc = knc.score(test_X, test_Y)
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
print '\n'


#################################### 5: AdaBoostClassifier ###############################
abc = ABC()
abc.fit(train_X, train_Y)
dr_abc = abc.score(test_X, test_Y)
print("The detection results of AdaBoost....................")
abc_y_pred = abc.predict(test_X)
abc_accuracy = metrics.accuracy_score(test_Y, abc_y_pred)
abc_precision = metrics.precision_score(test_Y, abc_y_pred, average="macro")
abc_recall = metrics.recall_score(test_Y, abc_y_pred, average="macro")
abc_f_score = metrics.f1_score(test_Y, abc_y_pred, average="macro")
print "Accuracy: %f" %abc_accuracy
print "Precision: %f" %abc_precision
print "Recall: %f" %abc_recall
print "F1 score: %f" %abc_f_score
print '\n'
# ==================================================================================================


######################################## 6: XGBoost ########################################
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
param['num_class'] = 2
param['colsample_bytree'] = 1
param['subsample'] = 1

watchlist = [(xg_train, 'train'), (xg_test, 'test')]
num_round = 10
bst = xgb.train(param, xg_train, num_round, watchlist)
# #########################Computing the importances of the features##########################
# def get_importance(model, feature_names):
#     importances = model.get_fscore()
#     # print importances
#
#     subtrain1 = pd.merge(subtrainLabel, apifeature, on='Id')
#     subtrain1 = pd.merge(subtrain1, apiCatefeature, on='Id')
#     subtrain1 = pd.merge(subtrain1, dllfeature, on='Id')
#     subtrain2 = pd.merge(subtrainLabel, networkfeature, on='Id')
#     subtrain2 = pd.merge(subtrain2, registryfeature, on='Id')
#     subtrain2 = pd.merge(subtrain2, filefeature, on='Id')
#     section_feature_names = list(sectionfeature)[1:]
#     # print "section_feature_names:", section_feature_names
#     basic_behavior_feature_names = list(subtrain1)[2:]
#     # print "basic_behavior_feature_names:", basic_behavior_feature_names
#     high_behavior_feature_names = list(subtrain2)[2:]
#     # print "high_behavior_feature_names:", high_behavior_feature_names
#
#     section_values = 0
#     basic_behavior_values = 0
#     high_behavior_values = 0
#     for section_index in section_feature_names:
#         # print "section_index:", section_index
#         if section_index in importances:
#             # print "importances[section_index]:", importances[section_index]
#             section_values += importances[section_index]
#     print "section_values:", section_values
#
#     for basic_behavior_index in basic_behavior_feature_names:
#         # print "basic_behavior_index:", basic_behavior_index
#         if basic_behavior_index in importances:
#             # print "importances[basic_behavior_index]", importances[basic_behavior_index]
#             basic_behavior_values += importances[basic_behavior_index]
#     print "basic_behavior_values:", basic_behavior_values
#
#     for high_behavior_index in high_behavior_feature_names:
#         # print "high_behavior_index:", high_behavior_index
#         if high_behavior_index in importances:
#             # print "importances[high_behavior_index]:", importances[high_behavior_index]
#             high_behavior_values += importances[high_behavior_index]
#     print "high_behavior_values:", high_behavior_values
#
#     values = section_values + basic_behavior_values + high_behavior_values
#     section_importance = section_values / values
#     basic_importances = basic_behavior_values / values
#     high_importances = high_behavior_values / values
#     print "section_importance:", section_importance
#     print "basic_importances:", basic_importances
#     print "high_importances:", high_importances
# ###########################################################################
# feature_path = os.path.abspath('.') + '/FeatureSet/' + 'featureset.csv'
# features = pd.read_csv(feature_path)
# feature_names = list(features)[2:]
# # print "feature_names:", feature_names
# get_importance(bst, feature_names)
###########################################################################
xgbst_y_pred = bst.predict(xg_test)
xgbst_accuracy = metrics.accuracy_score(test_Y, xgbst_y_pred)
xgbst_precision = metrics.precision_score(test_Y, xgbst_y_pred, average="macro")
xgbst_recall = metrics.recall_score(test_Y, xgbst_y_pred, average="macro")
xgbst_f_score = metrics.f1_score(test_Y, xgbst_y_pred, average="macro")
print "Accuracy: %f" %xgbst_accuracy
print "Precision: %f" %xgbst_precision
print "Recall: %f" %xgbst_recall
print "F1 score: %f" %xgbst_f_score