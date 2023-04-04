# -*- coding: utf-8 -*-
import os
import numpy as np


#======================计算所有样本中每个API出现的次数=======================
def api_of_all_classes():
	dir_path = os.path.abspath(".") + '/APT_Samples_api_set/'

	target_path = os.path.abspath(".") + '/APT_ApiStat/'
	if not os.path.exists(target_path):
		os.makedirs(target_path)

	apilist= {}
	files = os.listdir(dir_path)
	for mFile in files:
		print mFile
		with open(dir_path + mFile, 'r') as f:
			for line in f:
				if line != '\n':
					if line[:-1] in apilist:
						apilist[line[:-1]] += 1
					else:
						apilist[line[:-1]] = 1

	newFile = file(target_path + 'apiStat.txt','w')
	for i,v in apilist.iteritems():
		newFile.write(i + " " + str(v) + "\n")
	newFile.close()


#======================计算每一类样本中每个API出现的次数=======================
def api_of_one_class():
	dir_path = os.path.abspath(".") + '/APT_Samples_api_group/'

	target_path = os.path.abspath(".") + '/APT_ApiStat/'
	if not os.path.exists(target_path):
		os.makedirs(target_path)

	dirs = os.listdir(dir_path)
	for dir in dirs:
		files = os.listdir(dir_path + dir)
		apilist = {}
		for mFile in files:
			print mFile
			with open(dir_path + dir + '/' + mFile,'r') as f:
				for line in f:
					if line != '\n':
						if line[:-1] in apilist:
							apilist[line[:-1]] += 1
						else:
							apilist[line[:-1]] = 1

		newFile = file(target_path + dir + '.txt','w')
		for i, v in apilist.iteritems():
			newFile.write(i + " " + str(v) + "\n")
		newFile.close()


#======================计算每个样本中每个API出现的次数=======================
def api_of_one_file():
	dir_path = os.path.abspath(".") + '/APT_Samples_api_group/'

	target_path = os.path.abspath(".") + '/APT_apiCount/'
	if not os.path.exists(target_path):
		os.makedirs(target_path)

	dirs = os.listdir(dir_path)
	for dir in dirs:
		print "dir:" + dir
		dirPath1 = os.path.join(target_path, dir)
		print "dirPath1:" + dirPath1
		if not os.path.exists(dirPath1):
			os.makedirs(dirPath1)

		files = os.listdir(dir_path + dir)
		for mFile in files:
			print dir, mFile
			apilist = {}
			with open(dir_path + dir + '/' + mFile,'r') as f:
				for line in f:
					if line != '\n':
						if line[:-1] in apilist:
							apilist[line[:-1]] += 1
						else:
							apilist[line[:-1]] = 1

			newFile = file(target_path + dir + "/" + mFile,'w')
			for i,v in apilist.iteritems():
				newFile.write(i + " " + str(v) + "\n")
			newFile.close()
				
				
#==============计算每类Malware中每个API在每个文件中出现次数的方差================
def api_of_var_in_one_class():
	source_path = os.path.abspath(".") + '/APT_apiCount/'

	target_path = os.path.abspath(".") + '/APT_ApiVar/'
	if not os.path.exists(target_path):
		os.makedirs(target_path)

	dir_path = os.path.abspath(".") + '/APT_ApiStat/'
	dirs = os.listdir(source_path)
	for dir in dirs:
		apiNumOfEachFile = {} #每个api在每个文件中出现的次数
		with open(dir_path + dir + ".txt", "r") as f:
			for line in f:
				if line != '\n':
					strs = line.split(' ')
					api = strs[0]
					apiNum = []
					apiNumOfEachFile[api] = apiNum

		files = os.listdir(source_path + dir)
		for mFile in files:
			print dir, mFile
			apiCount = {}
			with open(source_path + dir + '/' + mFile,'r') as f:
				for line in f:
					if line != '\n':
						strs = line.split(' ')
						api = strs[0]
						count = float(strs[1][:-1])
						apiCount[api] = count
			for api in apiNumOfEachFile:
				if api in apiCount:
					apiNumOfEachFile[api].append(apiCount[api])
				else:
					apiNumOfEachFile[api].append(0.0)

		newFile = file(target_path + dir + ".txt", 'w')
		apiVar = {}
		for api in apiNumOfEachFile:
			data = np.array(apiNumOfEachFile[api])
			score = np.var(data)
			apiVar[api] = score
		sorted_api = sorted(apiVar.items(), key = lambda x: x[1], reverse=True)
		for api,var in sorted_api:
			newFile.write(api + " " + str(var) + str(sorted(apiNumOfEachFile[api])) + "\n")
		newFile.close()


if __name__ =="__main__":
	api_of_all_classes()
	api_of_one_class()
	api_of_one_file()
	api_of_var_in_one_class()