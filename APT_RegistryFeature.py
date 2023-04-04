# -*- coding: utf-8 -*-
# Has not finished!
import json
import os
import pandas as pd
import hashlib
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from time import time

if __name__ =="__main__":
    start = time()

    registry_path = os.path.abspath(".") + "/APT_RegistryFeature/"
    if not os.path.exists(registry_path):
        os.makedirs(registry_path)

    dataframelist = []

    def get_md5_value(str):
        md5obj = hashlib.md5()
        md5obj.update(str)
        md5_value = md5obj.hexdigest()
        return  md5_value


    All_APT_json_array = ['BaiXiang-json', 'DarkHotel-json', 'Mirage-json', 'NormanShark-json', 'SinDigoo-json']
    for i in range(len(All_APT_json_array)):
        curDir = All_APT_json_array[i]
        dir_path = os.path.abspath('.') + '/Json/' + curDir + '/'
        files = os.listdir(dir_path)
        num = 1
        for mFile in files:
            with open(dir_path + '/' + mFile, 'r') as fo:
                print "Analysing the registry operations of the {} ...".format(mFile)
                print "Analysing the %d file" %num
                standard = {}
                standard["Id"] = mFile[:-5]

                regkey_read_num = 0
                regkey_opened_num = 0
                regkey_written_num = 0
                regkey_deleted_num = 0

                regkey_read_list = []
                regkey_opened_list = []
                regkey_written_list = []
                regkey_deleted_list = []

                jsonObj = json.load(fo)
                if "behavior" in jsonObj:
                    if "generic" in jsonObj["behavior"]:
                        generic_num = len(jsonObj["behavior"]["generic"])
                        if generic_num > 0:
                            for x in range(generic_num):
                                generic = jsonObj["behavior"]["generic"][x]
                                if "summary" in generic:
                                    if "regkey_opened" in jsonObj["behavior"]["generic"][x]["summary"]:
                                        open_num = len(jsonObj["behavior"]["generic"][x]["summary"]["regkey_opened"])
                                        if open_num > 0:
                                            # print mFile + " regkey_opened: %d" %open_num
                                            for y in range(open_num):
                                                key_open_tmp = jsonObj["behavior"]["generic"][x]["summary"]["regkey_opened"][y]
                                                # print key_open_tmp
                                                reg_open_md5 = get_md5_value(key_open_tmp)
                                                # print "MD5 value: %s" %reg_md5
                                                if reg_open_md5 not in regkey_opened_list:
                                                    regkey_opened_list.append(reg_open_md5)
                                                    regkey_opened_num += 1

                                    if "regkey_read" in jsonObj["behavior"]["generic"][x]["summary"]:
                                        read_num = len(jsonObj["behavior"]["generic"][x]["summary"]["regkey_read"])
                                        if read_num > 0:
                                            for y in range(read_num):
                                                key_read_tmp = jsonObj["behavior"]["generic"][x]["summary"]["regkey_read"][y]
                                                reg_read_md5 = get_md5_value(key_read_tmp)
                                                if reg_read_md5 not in regkey_read_list:
                                                    regkey_read_list.append(reg_read_md5)
                                                    regkey_read_num += 1

                                    if "regkey_written" in jsonObj["behavior"]["generic"][x]["summary"]:
                                        written_num = len(jsonObj["behavior"]["generic"][x]["summary"]["regkey_written"])
                                        if written_num > 0:
                                            for y in range(written_num):
                                                key_written_tmp = jsonObj["behavior"]["generic"][x]["summary"]["regkey_written"][
                                                    y]
                                                reg_written_md5 = get_md5_value(key_written_tmp)
                                                if reg_written_md5 not in regkey_written_list:
                                                    regkey_written_list.append(reg_written_md5)
                                                    regkey_written_num += 1

                                    if "regkey_deleted" in jsonObj["behavior"]["generic"][x]["summary"]:
                                        deleted_num = len(jsonObj["behavior"]["generic"][x]["summary"]["regkey_deleted"])
                                        if deleted_num > 0:
                                            for y in range(deleted_num):
                                                key_deleted_tmp = jsonObj["behavior"]["generic"][x]["summary"]["regkey_deleted"][
                                                    y]
                                                reg_deleted_md5 = get_md5_value(key_deleted_tmp)
                                                if reg_deleted_md5 not in regkey_deleted_list:
                                                    regkey_deleted_list.append(reg_deleted_md5)
                                                    regkey_deleted_num += 1
                        else:
                            print mFile + " doesn't has registry behavior!"
                    else:
                        print mFile + " doesn't has registry behavior!"
                else:
                    print mFile + " doesn't has behavior"

                print "regkey_read: %d" %regkey_read_num
                print "regkey_opened: %d" %regkey_opened_num
                print "regkey_written: %d" %regkey_written_num
                print "regkey_deleted: %d" %regkey_deleted_num

                standard["regkey_read"] = regkey_read_num
                standard["regkey_opened"] = regkey_opened_num
                standard["regkey_written"] = regkey_written_num
                # standard["regkey_deleted"] = regkey_deleted_num
                dataframelist.append(standard)
                num += 1

    df = pd.DataFrame(dataframelist)
    df.to_csv(registry_path + 'APT_RegistryFeature.csv', index = False)

    end = time()
    print '\n'
    print '运行时间： %s 秒' % str(end - start)
    print 'Done successfully......'