# -*- coding: utf-8 -*-
import os
import math
import shutil
from collections import *

def tf(word, count):
	return float(count[word]) * 100000/sum(count.values())

def n_containing(word, count_list):
	return sum(1 for count in count_list.values() if word in count)

def idf(word, count_list):
	containing = n_containing(word, count_list)
	if containing == 0.0:
		return math.log(len(count_list) / 1)
	else:
		return math.log(len(count_list) / containing)

def tfidf(word, count, count_list):
	return tf(word, count) * idf(word, count_list)
	
def idf_my(api,TrojanNum,subContainApiNumStat,subFileNum):
	ContainApiNum = contain_api(api,subContainApiNumStat)
	# print ContainApiNum
	if ContainApiNum == 0.0:
		return math.log((TrojanNum - subFileNum)/ 1)
	else:
		return math.log((TrojanNum -subFileNum) / ContainApiNum)

def contain_api(api, subContainApiNumStat):
	ContainApiNum = 0.0
	for i,j in enumerate(subContainApiNumStat):
		if api in subContainApiNumStat[j]:
			ContainApiNum = ContainApiNum + float(subContainApiNumStat[j][api])
	return ContainApiNum

def cf(api,subContainApiNum,subApiNum,subFileNum):
	# return float(subContainApiNum[api]) * (subApiNum[api]/subFileNum)
	return float(subContainApiNum[api])  / subFileNum
	
def cfidf(api,subContainApiNum,subApiNum,subFileNum,TrojanNum,subContainApiNumStat):
	return cf(api,subContainApiNum,subApiNum,subFileNum) * idf_my(api,TrojanNum,subContainApiNumStat,subFileNum)


#=========================计算每个API的类贡献度&& with sorted===========================
def get_apiProb():
	source_path = os.path.abspath(".") + "/APT_apiCount/"
	target_path = os.path.abspath(".") + "/APT_ApiProb/"

	if not os._exists(target_path):
		os.makedirs(target_path)
	
	dirs = os.listdir(source_path)
	subFileNumStat = {}  #每一Family包含的总样本数
	subContainApiNumStat = {} #每一Family中包含某API的样本个数
	subApiNumStat = {} #某个API在每一Family中出现的总次数
	
	for dir in dirs:
		files = os.listdir(source_path + dir)
		apiList = []
		subApiNum = {} #某个API在一类木马中出现的总次数
		for mFile in files:
			with open(source_path + dir + '/' + mFile,'r') as f:
				for line in f:
					if line != '\n':
						strs = line.split(' ')
						api = strs[0]
						apiCount = float(strs[1][:-1])
						apiList.append(api)
						if api in subApiNum:
							subApiNum[api] = subApiNum[api] + apiCount
						else:
							subApiNum[api] = apiCount
		subApiNumStat[dir] = subApiNum
		subContainApiNumStat[dir] = Counter(apiList)
		subFileNumStat[dir] = float(len(files))
	
	TrojanNum = float(sum(subFileNumStat.values()))
	for dir in dirs:
		print dir
		subContainApiNum = subContainApiNumStat[dir]
		subApiNum = subApiNumStat[dir]
		subFileNum = float(subFileNumStat[dir])
		scores = {api:cfidf(api,subContainApiNum,subApiNum,subFileNum,TrojanNum,subContainApiNumStat) for api in subApiNumStat[dir]}
		sorted_api = sorted(scores.items(), key=lambda x: x[1], reverse=True)
		newFile = file(target_path + dir + '.txt','w')
		for api, score in sorted_api:
			newFile.write(api + " " + str(round(score,5)) + '\n')
		newFile.close()


# =========================计算每个API的类贡献度&& not sorted===========================
def get_apiProb_unsorted():
	source_path = os.path.abspath(".") + "/APT_apiCount/"
	target_path = os.path.abspath(".") + "/APT_ApiProb_Unsorted/"

	if os.path.exists(target_path):
		shutil.rmtree(target_path)

	if not os.path.exists(target_path):
		os.makedirs(target_path)

	dirs = os.listdir(source_path)
	subFileNumStat = {}  # 每一Family包含的总样本数
	subContainApiNumStat = {}  # 每一Family中包含某API的样本个数
	subApiNumStat = {}  # 某个API在每一Family中出现的总次数

	for dir in dirs:
		files = os.listdir(source_path + dir)
		apiList = []
		subApiNum = {}  # 某个API在一类木马中出现的总次数
		for mFile in files:
			with open(source_path + dir + '/' + mFile, 'r') as f:
				for line in f:
					if line != '\n':
						strs = line.split(' ')
						api = strs[0]
						apiCount = float(strs[1][:-1])
						apiList.append(api)
						if api in subApiNum:
							subApiNum[api] = subApiNum[api] + apiCount
						else:
							subApiNum[api] = apiCount
		subApiNumStat[dir] = subApiNum
		subContainApiNumStat[dir] = Counter(apiList)
		subFileNumStat[dir] = float(len(files))

	TrojanNum = float(sum(subFileNumStat.values()))
	scores = {}
	for dir in dirs:
		print dir
		subContainApiNum = subContainApiNumStat[dir]
		subApiNum = subApiNumStat[dir]
		subFileNum = float(subFileNumStat[dir])
		# scores = {api: cfidf(api, subContainApiNum, subApiNum, subFileNum, TrojanNum, subContainApiNumStat) for api in
		# 		  subApiNumStat[dir]}

		for api in subApiNumStat[dir]:
			scores[api] = cfidf(api, subContainApiNum, subApiNum, subFileNum, TrojanNum, subContainApiNumStat)

			# print(type(scores))
			# print(scores)

			# sorted_api = sorted(scores.items(), key=lambda x: x[1], reverse=True)
			# print(sorted_api)
			newFile = file(target_path + dir + '.txt', 'w')
			for api, score in scores.items():
				newFile.write(api + " " + str(round(score, 5)) + '\n')
			newFile.close()

if __name__ =="__main__":
	# get_apiProb()
    get_apiProb_unsorted()