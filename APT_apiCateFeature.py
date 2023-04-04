# -*- coding: utf-8 -*-
from collections import *
import os
import pandas as pd


# ======================获取所有样本的api种类及个数===========================
def get_category_count():
    source_path = os.path.abspath(".") + "/APT_Samples_apicategory/"

    tar_path = os.path.abspath('.') + '/APT_apicategoryCount/'
    if not os.path.exists(tar_path):
		os.makedirs(tar_path)

    apiCatelist = []
    result = {}
    for mFile in os.listdir(source_path):
        with open(source_path + mFile, 'r') as f:
            for line in f:
                if line != '\n':
                    strs = line.split('-')
                    apiCate = strs[0]
                    count = int(strs[1][:-1])
                    if apiCate not in apiCatelist:
                        apiCatelist.append(apiCate)
                        result[apiCate] = count
    newFile = file(tar_path + 'APT_apiCateCount.txt', 'w')
    for cate, v in result.iteritems():
        newFile.write(str(cate) + "-" + str(v) + '\n')
    newFile.close


# ======================以api种类为FeatureVector，获取所有样本的api种类======================
def getapiCate_Feature():
    source_path = os.path.abspath('.') + '/APT_apicategoryCount/'
    dir_path = os.path.abspath('.') + '/APT_Samples_apicategory/'

    apiCateFeature = []
    numCate = 0
    index = 0
    print "The length of the dir:%d" %len(os.listdir(source_path))


    for mFile in os.listdir(source_path):
        with open(source_path + mFile, 'r') as f:
            for line in f:
                if line != '\n':
                    strs = line.split('-')
                    print strs
                    apiCateFeature.append(strs[0])
                    numCate += 1
        index += 1
    print "index=%d" %index

    print "%d apiCategories!" %numCate
    print apiCateFeature

    dirs = os.listdir(dir_path)
    dataframelist = []
    files = os.listdir(dir_path)
    num = 1
    for mFile in files:
        with open(dir_path + '/' + mFile, 'r') as f:
            standard = {}
            standard["Id"] = mFile[:-4]
            apicCount = {}
            for line in f:
                strs = line.split('-')
                apic = strs[0]
                count = strs[1]
                apicCount[apic] = count
            for api in apiCateFeature:
                if api in apicCount:
                    standard[api] = apicCount[api]
                else:
                    standard[api] = 0
            dataframelist.append(standard)
            print "Counting the %d file" %num
            print "counting the apiCate_Feature of the {} ...".format(mFile)
            num += 1

    df = pd.DataFrame(dataframelist)
    target_path = os.path.abspath('.') + '/APT_ApicateFeature/'
    if not os.path.exists(target_path):
        os.makedirs(target_path)
    df.to_csv(target_path + 'APT_apiCate_Feature' + '.csv', index = False)


if __name__ =="__main__":
    get_category_count()
    getapiCate_Feature()