# -*- coding: utf-8 -*-
from collections import *
import os
import pandas as pd
import global_list

source_path = os.path.abspath('.') + '/APT_ApiProb/'
dir_path = os.path.abspath('.') + '/APT_apiCount/'

target_path = os.path.abspath('.') + '/APT_ApiFeature/'
if not os.path.exists(target_path):
	os.makedirs(target_path)

# 取贡献度Top-N
N = global_list.api_Top_N

files = os.listdir(source_path)
apiFeature_Select = {}
for mFile in files:
	with open(source_path + mFile, 'r') as f:
		num = 0
		for line in f:
			if num <= N:
				if line != '\n':
					strs = line.split(' ')
					api = strs[0]
					prob = float(strs[1][:-1])
					apiFeature_Select[api] = prob
					num += 1

dirs = os.listdir(dir_path)
dataframelist = []
for dir in dirs:
	files = os.listdir(dir_path + dir)
	for mFile in files:
		with open(dir_path + dir + '/' + mFile, 'r') as f:
			standard = {}
			standard["Id"] = mFile[:-4]
			apiCount = {}
			for line in f:
				if line != '\n':
					strs = line.split(' ')
					api = strs[0]
					count = int(strs[1][:-1])
					apiCount[api] = count
			for api in apiFeature_Select:
				if api in apiCount:
					#standard[api] = 1
					standard[api] = apiCount[api] + count
				else:
					standard[api] = 0
			print "This item:"
			print standard
			dataframelist.append(standard)
			print "counting the api of the {} ...".format(mFile)

print "%d apis have been selected!" %len(apiFeature_Select)

df = pd.DataFrame(dataframelist)
df.to_csv(target_path + 'APT_apifeature_' + str(N) + '.csv', index=False)