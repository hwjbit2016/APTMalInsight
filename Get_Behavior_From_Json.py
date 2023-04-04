# -*- coding: utf-8 -*-
# 本程序功能：
# 1、从json文件中提取API等信息；
# 2、从json文件中提取API和API Category pair序列
# 3、从json文件中提取API、API Category和API分类贡献度Prob Pair序列
#
import json
import os
import re
from time import time
import shutil


PE_Section_Name_List = ['UPX0', 'UPX1', 'UPX2', 'aspack', 'nPack', 'shield', 'SHIELD',
                        'text', 'TEXT', 'itext', 'ITEXT',
                        'data', 'DATA', 'rdata', 'idata', 'edata', 'adata', 'pdata', 'sdata',
                        'rsrc', 'reloc', 'reloc1', 'bss', 'BSS', 'shared', 'CODE', 'code', 'tls', 'TLS',
                        'rlink']
PE_Section_Name_list = []


def PESection_Name_Matching(str):
    SectionName = ''
    if 'UPX0' in str or 'upx0' in str:
        SectionName = 'UPX0'
        print "SectionName:" + SectionName
    elif 'UPX1' in str or 'upx1' in str:
        SectionName = 'UPX1'
        print "SectionName:" + SectionName
    elif 'UPX2' in str or 'upx2' in str:
        SectionName = 'UPX2'
        print "SectionName:" + SectionName
    elif 'aspack' in str or 'ASPACK' in str:
        SectionName = 'aspack'
        print "SectionName:" + SectionName
    elif 'nPack' in str:
        SectionName = 'nPack'
        print "SectionName:" + SectionName
    elif 'shield' in str or 'SHIELD' in str:
        SectionName = 'shield'
        print "SectionName:" + SectionName
    elif (('text' in str) and ('itext' in str)) or (('TEXT' in str) and ('ITEXT' in str)):
        SectionName = 'itext'
        print "SectionName:" + SectionName
    elif 'text' in str or 'TEXT' in str:
        SectionName = 'text'
        print "SectionName:" + SectionName
    elif (('data' in str) and ('adata' in str)) or (('DATA' in str) and ('ADATA' in str)):
        SectionName = 'adata'
        print "SectionName:" + SectionName
    elif (('data' in str) and ('pdata' in str)) or (('DATA' in str) and ('PDATA' in str)):
        SectionName = 'pdata'
        print "SectionName:" + SectionName
    elif (('data' in str) and ('rdata' in str)) or (('DATA' in str) and ('RDATA' in str)):
        SectionName = 'rdata'
        print "SectionName:" + SectionName
    elif (('data' in str) and ('sdata' in str)) or (('DATA' in str) and ('SDATA' in str)):
        SectionName = 'sdata'
        print "SectionName:" + SectionName
    elif (('data' in str) and ('idata' in str)) or (('DATA' in str) and ('IDATA' in str)):
        SectionName = 'idata'
        print "SectionName:" + SectionName
    elif (('data' in str) and ('edata' in str)) or (('DATA' in str) and ('EDATA' in str)):
        SectionName = 'edata'
        print "SectionName:" + SectionName
    elif ('data' in str or 'DATA' in str):
        SectionName = 'data'
        print "SectionName:" + SectionName
    elif 'rsrc' in str or 'RSRC' in str:
        SectionName = 'rsrc'
        print "SectionName:" + SectionName
    elif 'rlink' in str or 'RLINK' in str:
        SectionName = 'rlink'
        print "SectionName:" + SectionName
    elif (('reloc' in str) and ('reloc1' in str)) or (('RELOC' in str) and 'RELOC1' in str):
        SectionName = 'reloc'
        print "SectionName:" + SectionName
    elif 'reloc' in str or 'RELOC' in str:
        SectionName = 'reloc'
        print "SectionName:" + SectionName
    elif 'bss' in str or 'BSS' in str:
        SectionName = 'bss'
        print "SectionName:" + SectionName
    elif 'shared' in str or 'SHARED' in str:
        SectionName = 'shared'
        print "SectionName:" + SectionName
    elif 'code' in str or 'CODE' in str:
        SectionName = 'code'
        print "SectionName:" + SectionName
    elif 'tls' in str or 'TLS' in str:
        SectionName = 'tls'
        print "SectionName:" + SectionName
    elif 'init' in str or 'INIT' in str:
        SectionName = 'init'
        print "SectionName:" + SectionName
    else:
        SectionName = ''
        print "SectionName:" + SectionName

    return SectionName

# =========================获取每个样本的api序列 of Part===============================
def get_api(dir_path, mFile):
    tar_path = os.path.abspath(".") + "/Part_Samples_api_set/"
    if not os.path.exists(tar_path):
        os.makedirs(tar_path)

    result = []
    filename = dir_path + mFile
    with open(filename, 'r') as fo:
        jsonObj = json.load(fo)
        if "behavior" in jsonObj:
            if "processes" in jsonObj["behavior"]:
                proNum = len(jsonObj["behavior"]["processes"])
                for i in range(1, proNum):
                    if "calls" in jsonObj["behavior"]["processes"][i]:
                        callNum = len(jsonObj["behavior"]["processes"][i]["calls"])
                        for j in range(0, callNum):
                            s = jsonObj["behavior"]["processes"][i]["calls"][j]["api"]
                            result.append(s)
                    else:
                        print filename + " doesn't has calls"
            else:
                print filename + " doesn't has processes"
        else:
            print filename + " doesn't has behavior"
    newFile = file(tar_path + mFile[:-5] + '.txt', 'w')
    for api in result:
        newFile.write(str(api) + '\n')
    newFile.close

# =========================获取部分样本的api序列===============================
def get_part_api(dir_path, curDir, mFile):
    tar_path = os.path.abspath(".") + "/Part_Samples_api_group/" + curDir + '/'
    if not os.path.exists(tar_path):
        os.makedirs(tar_path)

    result = []
    filename = dir_path + mFile
    with open(filename, 'r') as fo:
        jsonObj = json.load(fo)
        if "behavior" in jsonObj:
            if "processes" in jsonObj["behavior"]:
                proNum = len(jsonObj["behavior"]["processes"])
                for i in range(1, proNum):
                    if "calls" in jsonObj["behavior"]["processes"][i]:
                        callNum = len(jsonObj["behavior"]["processes"][i]["calls"])
                        for j in range(0, callNum):
                            s = jsonObj["behavior"]["processes"][i]["calls"][j]["api"]
                            result.append(s)
                    else:
                        print filename + " doesn't has calls"
            else:
                print filename + " doesn't has processes"
        else:
            print filename + " doesn't has behavior"
    newFile = file(tar_path + mFile[:-5] + '.txt', 'w')
    for api in result:
        newFile.write(str(api) + '\n')
    newFile.close

# =========================获取所有APT样本的api序列===============================
def get_APT_api(dir_path, mFile):
    tar_path = os.path.abspath(".") + "/APT_Samples_api_set/"
    if not os.path.exists(tar_path):
        os.makedirs(tar_path)

    result = []
    filename = dir_path + mFile
    with open(filename, 'r') as fo:
        jsonObj = json.load(fo)
        if "behavior" in jsonObj:
            if "processes" in jsonObj["behavior"]:
                proNum = len(jsonObj["behavior"]["processes"])
                for i in range(1, proNum):
                    if "calls" in jsonObj["behavior"]["processes"][i]:
                        callNum = len(jsonObj["behavior"]["processes"][i]["calls"])
                        for j in range(0, callNum):
                            s = jsonObj["behavior"]["processes"][i]["calls"][j]["api"]
                            result.append(s)
                    else:
                        print filename + " doesn't has calls"
            else:
                print filename + " doesn't has processes"
        else:
            print filename + " doesn't has behavior"
    newFile = file(tar_path + mFile[:-5] + '.txt', 'w')
    for api in result:
        newFile.write(str(api) + '\n')
    newFile.close

# ======================获取每个样本的api种类及个数===========================
def get_category(filename):
    print '----' + filename + '----'

    tar_path = os.path.abspath(".") + "/APT_Samples_apicategory/"
    if not os.path.exists(tar_path):
        os.makedirs(tar_path)

    result = {}
    with open(filename, 'r') as fo:
        jsonObj = json.load(fo)
        if "behavior" in jsonObj:
            if "processes" in jsonObj["behavior"]:
                proNum = len(jsonObj["behavior"]["processes"])
                for i in range(1, proNum):
                    if "calls" in jsonObj["behavior"]["processes"][i]:
                        callNum = len(jsonObj["behavior"]["processes"][i]["calls"])
                        for j in range(0, callNum):
                            s = jsonObj["behavior"]["processes"][i]["calls"][j]["category"]
                            if s not in result:
                                result[s] = 0
                            else:
                                result[s] += 1
                    else:
                        print filename + " doesn't has calls"
            else:
                print filename + " doesn't has processes"
        else:
            print filename + " doesn't has behavior"

    newFile = file(tar_path + mFile[:-5] + '.txt', 'w')
    for cate, v in result.iteritems():
        newFile.write(str(cate) + "-" + str(v) + '\n')
    newFile.close

# ======================获取每个文件的PE导入和DLL===========================#
def get_pe_imports(filename):
    # print filename
    import_path = os.path.abspath("..") + "/PE_imports/"
    dll_path = os.path.abspath("..") + "/PE_DLL/"

    if not os.path.exists(import_path):
        os.makedirs(import_path)
    if not os.path.exists(dll_path):
        os.makedirs(dll_path)

    result = {}
    dlls = {}
    with open(filename, 'r') as fo:
        jsonObj = json.load(fo)
        if "static" in jsonObj:
            if "pe_imports" in jsonObj["static"]:
                import_num = len(jsonObj["static"]["pe_imports"])
                if import_num > 0:
                    for x in range(import_num):
                        imports = jsonObj["static"]["pe_imports"][x]
                        if "imports" in imports:
                            proNum = len(imports["imports"])
                            for i in range(proNum):
                                if "name" in imports["imports"][i]:
                                    name = imports["imports"][i]["name"]
                                    if name not in result:
                                        result[name] = 1
                                    else:
                                        result[name] += 1
                                else:
                                    print filename + " doesn't has name"
                        else:
                            print filename + " doesn't has imports"

                        if "dll" in imports:
                            tmpdll = str(imports["dll"]).lower()
                            print "tmpdll = ", tmpdll
                            if re.match('^[a-z]', tmpdll):
                                if tmpdll.startswith("api-ms-win"):
                                    mdll = "api-ms-win*.dll"
                                elif tmpdll.startswith("atl"):
                                    mdll = "atl*.dll"
                                elif tmpdll.startswith("adv"):
                                    mdll = "adv*.dll"
                                elif tmpdll.startswith("atl"):
                                    mdll = "atl*.dll"
                                elif tmpdll.startswith("auth"):
                                    mdll = "auth*.dll"
                                elif tmpdll.startswith("basic"):
                                    mdll = "basic*.dll"
                                elif tmpdll.startswith("cc"):
                                    mdll = "cc*.dll"
                                elif tmpdll.startswith("crash"):
                                    mdll = "crash*.dll"
                                elif tmpdll.startswith("crypt"):
                                    mdll = "crypt*.dll"
                                elif tmpdll.startswith("cyg"):
                                    mdll = "cyg*.dll"
                                elif tmpdll.startswith("d3d"):
                                    mdll = "d3d*.dll"
                                elif tmpdll.startswith("dbg"):
                                    mdll = "dbg*.dll"
                                elif tmpdll.startswith("du"):
                                    mdll = "du*.dll"
                                elif tmpdll.startswith("gdi"):
                                    mdll = "gdi*.dll"
                                elif tmpdll.startswith("ida"):
                                    mdll = "ida*.dll"
                                elif tmpdll.startswith("ime"):
                                    mdll = "ime*.dll"
                                elif tmpdll.startswith("jv"):
                                    mdll = "jv*.dll"
                                elif tmpdll.startswith("kernel"):
                                    mdll = "kernel*.dll"
                                elif tmpdll.startswith("ku"):
                                    mdll = "ku*.dll"
                                elif tmpdll.startswith("kw"):
                                    mdll = "kw*.dll"
                                elif tmpdll.startswith("lib"):
                                    mdll = "lib*.dll"
                                elif tmpdll.startswith("log"):
                                    mdll = "log*.dll"
                                elif tmpdll.startswith("mf"):
                                    mdll = "mf*.dll"
                                elif tmpdll.startswith("mi"):
                                    mdll = "mi*.dll"
                                elif tmpdll.startswith("mp"):
                                    mdll = "mp*.dll"
                                elif tmpdll.startswith("mq"):
                                    mdll = "mq*.dll"
                                elif tmpdll.startswith("ms"):
                                    mdll = "ms*.dll"
                                elif tmpdll.startswith("nc"):
                                    mdll = "nc*.dll"
                                elif tmpdll.startswith("nd"):
                                    mdll = "nd*.dll"
                                elif tmpdll.startswith("net"):
                                    mdll = "net*.dll"
                                elif tmpdll.startswith("nt"):
                                    mdll = "nt*.dll"
                                elif tmpdll.startswith("nv"):
                                    mdll = "nv*.dll"
                                elif tmpdll.startswith("ole"):
                                    mdll = "ole*.dll"
                                elif tmpdll.startswith("one"):
                                    mdll = "one*.dll"
                                elif tmpdll.startswith("qt"):
                                    mdll = "qt*.dll"
                                elif tmpdll.startswith("qu"):
                                    mdll = "qu*.dll"
                                elif tmpdll.startswith("ra"):
                                    mdll = "ra*.dll"
                                elif tmpdll.startswith("re"):
                                    mdll = "re*.dll"
                                elif tmpdll.startswith("rn"):
                                    mdll = "rn*.dll"
                                elif tmpdll.startswith("rs"):
                                    mdll = "rs*.dll"
                                elif tmpdll.startswith("rt"):
                                    mdll = "rt*.dll"
                                elif tmpdll.startswith("sfc"):
                                    mdll = "sfc*.dll"
                                elif tmpdll.startswith("sh"):
                                    mdll = "sh*.dll"
                                elif tmpdll.startswith("spp"):
                                    mdll = "spp*.dll"
                                elif tmpdll.startswith("sq"):
                                    mdll = "sq*.dll"
                                elif tmpdll.startswith("ss"):
                                    mdll = "ss*.dll"
                                elif tmpdll.startswith("un"):
                                    mdll = "un*.dll"
                                elif tmpdll.startswith("user"):
                                    mdll = "user*.dll"
                                elif tmpdll.startswith("vb"):
                                    mdll = "vb*.dll"
                                elif tmpdll.startswith("vc"):
                                    mdll = "vc*.dll"
                                elif tmpdll.startswith("vi"):
                                    mdll = "vi*.dll"
                                elif tmpdll.startswith("vm"):
                                    mdll = "vm*.dll"
                                elif tmpdll.startswith("vs"):
                                    mdll = "vs*.dll"
                                elif tmpdll.startswith("wd"):
                                    mdll = "wd*.dll"
                                elif tmpdll.startswith("we"):
                                    mdll = "we*.dll"
                                elif tmpdll.startswith("win"):
                                    mdll = "win*.dll"
                                elif tmpdll.startswith("wl"):
                                    mdll = "wl*.dll"
                                elif tmpdll.startswith("wm"):
                                    mdll = "wm*.dll"
                                elif tmpdll.startswith("ws"):
                                    mdll = "ws*.dll"
                                elif tmpdll.startswith("x"):
                                    mdll = "x*.dll"
                                elif tmpdll.startswith("zlib"):
                                    mdll = "zlib*.dll"
                                else:
                                    mdll = tmpdll

                                if mdll not in dlls:
                                    dlls[mdll] = 1
                                else:
                                    dlls[mdll] += 1
                                print "mdll = ", mdll
                        else:
                            print filename + " doesn't has dll"
                else:
                    print filename + " doesn't has pe_imports"
            else:
                print filename + " doesn't has pe_imports"
        else:
            print filename + "doesn't has static"

    newFile = file(import_path + mFile[:-5] + '.txt', 'w')
    for cate, v in result.iteritems():
        newFile.write(str(cate) + "-" + str(v) + '\n')
    newFile.close

    newFile = file(dll_path + mFile[:-5] + '.txt', 'w')
    for mdll, v in dlls.iteritems():
        newFile.write(str(mdll) + "-" + str(v) + '\n')
    newFile.close

# ======================获取每个文件的PE节名称和大小===========================
def get_pe_section(filename):
    # print filename
    section_path = os.path.abspath("..") + "/PE_section/"

    if not os.path.exists(section_path):
        os.makedirs(section_path)

    result = {}
    with open(filename, 'r') as fo:
        jsonObj = json.load(fo)
        if "static" in jsonObj:
            if "pe_sections" in jsonObj["static"]:
                pe_sections_num = len(jsonObj["static"]["pe_sections"])
                if pe_sections_num > 0:
                    for x in range(pe_sections_num):
                        pe_sections = jsonObj["static"]["pe_sections"][x]
                        if "name" in pe_sections:
                            name = pe_sections["name"]
                            size = int(pe_sections["virtual_size"], 16)
                            if name not in PE_Section_Name_list:
                                PE_Section_Name_list.append(name)
                            print "name:%s" % name
                            print "size:%d" % size
                            strTemp = PESection_Name_Matching(name)
                            if strTemp.strip():
                                result[strTemp] = size
                                print "SectionName:%s" % strTemp + '  ' + "Size:%d" % size
                        else:
                            print filename + " doesn't has name"
                else:
                    print filename + " doesn't has pe_sections"
            else:
                print filename + " doesn't has pe_sections"
        else:
            print filename + "doesn't has static"

    newFile = file(section_path + mFile[:-5] + '.txt', 'w')
    for cate, v in result.iteritems():
        newFile.write(str(cate) + "-" + str(v) + '\n')
    newFile.close

# =========================获取所有APT样本的api序列===============================
def get_all_APT_api(dir_path, curDir, mFile):
    tar_path = os.path.abspath(".") + "/APT_Samples_api_group/" + curDir + '/'
    if not os.path.exists(tar_path):
        os.makedirs(tar_path)

    result = []
    filename = dir_path + mFile
    with open(filename, 'r') as fo:
        jsonObj = json.load(fo)
        if "behavior" in jsonObj:
            if "processes" in jsonObj["behavior"]:
                proNum = len(jsonObj["behavior"]["processes"])
                for i in range(1, proNum):
                    if "calls" in jsonObj["behavior"]["processes"][i]:
                        callNum = len(jsonObj["behavior"]["processes"][i]["calls"])
                        for j in range(0, callNum):
                            s = jsonObj["behavior"]["processes"][i]["calls"][j]["api"]
                            result.append(s)
                    else:
                        print filename + " doesn't has calls"
            else:
                print filename + " doesn't has processes"
        else:
            print filename + " doesn't has behavior"
    newFile = file(tar_path + mFile[:-5] + '.txt', 'w')
    for api in result:
        newFile.write(str(api) + '\n')
    newFile.close

# ======================获取每个样本的api种类 of each family to txt===========================
def get_category_to_dict_txt(dir_path, curDir, mFile):
    tar_path = os.path.abspath(".") + "/APT_Samples_ApiCategory_To_TXT/" + curDir + '/'
    # if os.path.exists(tar_path):
    #     shutil.rmtree(tar_path)
    if not os.path.exists(tar_path):
        os.makedirs(tar_path)

    result = {}
    filename = dir_path + mFile
    with open(filename, 'r') as fo:
        jsonObj = json.load(fo)
        if "behavior" in jsonObj:
            if "processes" in jsonObj["behavior"]:
                proNum = len(jsonObj["behavior"]["processes"])
                for i in range(1, proNum):
                    if "calls" in jsonObj["behavior"]["processes"][i]:
                        callNum = len(jsonObj["behavior"]["processes"][i]["calls"])
                        for j in range(0, callNum):
                            category = jsonObj["behavior"]["processes"][i]["calls"][j]["category"]
                            api = jsonObj["behavior"]["processes"][i]["calls"][j]["api"]
                            result[api] = category
                    else:
                        print filename + " doesn't has calls"
            else:
                print filename + " doesn't has processes"
        else:
            print filename + " doesn't has behavior"

    newFile = file(tar_path + mFile[:-5] + '.txt', 'w')
    # if the file has existed, then remove it.
    if os.path.exists(newFile):
        os.remove(newFile)
    for api, cate in result.iteritems():
        newFile.write(str(api) + ":" + str(cate) + '\n')
    newFile.close


#读取API和API Category Pair文本文件，并将这些Pair存入到一个Dict中
def convert_txt_to_dict(txtFilePath):
    api_prob_dict = {}
    with open(txtFilePath, 'r') as fo:
        for line in fo:
            string = line.strip()
            api = string.split(' ')[0]
            prob = string.split(' ')[1]
            api_prob_dict[api] = prob
    return api_prob_dict


# ======================获取每个样本的api种类 of each family to txt with prob value===========================
def get_category_to_dict_txt_with_prob(dir_path, curDir, mFile, mDict):
    tar_path = os.path.abspath(".") + "/APT_Samples_ApiCategory_To_TXT_With_Prob/" + curDir + '/'
    # if os.path.exists(tar_path):
    #     shutil.rmtree(tar_path)
    if not os.path.exists(tar_path):
        os.makedirs(tar_path)

    result = {}
    filename = dir_path + mFile

    with open(filename, 'r') as fo:
        jsonObj = json.load(fo)
        if "behavior" in jsonObj:
            if "processes" in jsonObj["behavior"]:
                proNum = len(jsonObj["behavior"]["processes"])
                for i in range(1, proNum):
                    if "calls" in jsonObj["behavior"]["processes"][i]:
                        callNum = len(jsonObj["behavior"]["processes"][i]["calls"])
                        for j in range(0, callNum):
                            val_list = []
                            category = jsonObj["behavior"]["processes"][i]["calls"][j]["category"]
                            api = jsonObj["behavior"]["processes"][i]["calls"][j]["api"]
                            val_list.append(category)
                            prob = mDict[api]
                            val_list.append(prob)
                            # result[api] = category
                            result.setdefault(api, []).append(category)
                            result.setdefault(api, []).append(prob)
                    else:
                        print filename + " doesn't has calls"
            else:
                print filename + " doesn't has processes"
        else:
            print filename + " doesn't has behavior"

    newFile = file(tar_path + mFile[:-5] + '.txt', 'w')
    # if the file has existed, then remove it.
    # if os.path.exists(newFile):
    #     shutil.rmtree(newFile)
    for api, list_v in result.iteritems():
        newFile.write(str(api) + ":" + list_v[0] + ":" + list_v[1] + '\n')
    newFile.close

if __name__ =="__main__":
    Part_json_array = ['BenignPrograms-json', 'BaiXiang-Part-json', 'DarkHotel-Part-json', 'Mirage-json', 'NormanShark-Part-json', 'SinDigoo-Part-json']

    All_APT_json_array = ['BaiXiang-json', 'DarkHotel-json', 'Mirage-json', 'NormanShark-json', 'SinDigoo-json']

    start = time()

    # 针对Part样本，提取api序列。1.将所有的api文件保存到一个文件夹下；2.将每一类的api分开保存
    # for i in range(len(Part_json_array)):
    #     curDir = Part_json_array[i]
    #     dir_path = os.path.abspath('.') + '/Json/' + curDir + '/'
    #     files = os.listdir(dir_path)
    #     num = 1
    #     for mFile in files:
    #         num += 1
    #         filename = dir_path + mFile
    #
    #         #从part json中提取api序列，并且按照不同类别分别保存起api文件，每一个api文件以其json文件名命名
    #         get_part_api(dir_path, curDir[:-5], mFile)
    #
    #         #从json中提取api序列，并将所有的api文件保存到一个文件夹下
    #         get_api(dir_path, mFile)
    #
    #         # get_category(filename)
    #         #  get_pe_section(filename)
    #         #  get_pe_imports(filename)
    #     print '%s 共计有 %d 个文件被解析！' %(curDir, num)


    # 针对APT样本，提取api序列。1.将所有的api文件保存到一个文件夹下；2.将每一类APT的api分开保存
    for i in range(len(All_APT_json_array)):
        curDir = All_APT_json_array[i]
        dir_path = os.path.abspath('.') + '/Json/' + curDir + '/'

        prob_dict = {}
        prob_path = os.path.abspath('.') + '/APT_ApiProb_Unsorted/' + curDir[:-5] + '.txt'
        prob_dict = convert_txt_to_dict(prob_path)

        files = os.listdir(dir_path)
        num = 1
        for mFile in files:
            num += 1
            filename = dir_path + mFile
            print(filename)
            # # 从所有的APT json中提取api序列，并分类保存到对应的api文件夹下
            # get_all_APT_api(dir_path, curDir[:-5], mFile)

            # #从所有APT json中提取api序列，并将所有APT样本的api文件保存到一个文件夹下
            # get_APT_api(dir_path, mFile)

            # get_category(filename)
            #  get_pe_section(filename)
            #  get_pe_imports(filename)
            # get_category_to_dict_txt(dir_path, curDir[:-5], mFile)
            get_category_to_dict_txt_with_prob(dir_path, curDir[:-5], mFile, prob_dict)

        print '%s 共计有 %d 个文件被解析！' %(curDir, num-1)


    end = time()
    print '\n'
    print '运行时间： %s 秒' % str(end - start)
    print 'Done successfully......'