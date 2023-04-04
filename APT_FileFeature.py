# -*- coding: utf-8 -*-
# Has not finished!
import json
import os
import pandas as pd
import hashlib
import sys
from time import time
reload(sys)
sys.setdefaultencoding('utf8')


if __name__ =="__main__":
    start = time()

    file_path = os.path.abspath(".") + "/APT_FileFeature/"
    if not os.path.exists(file_path):
        os.makedirs(file_path)

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
                print "Analysing the file operations of the {} ...".format(mFile)
                print "Analysing the %d file" %num
                standard = {}
                standard["Id"] = mFile[:-5]

                file_created_num = 0
                file_recreated_num = 0
                file_opened_num = 0
                file_read_num = 0
                file_written_num = 0
                file_deleted_num = 0
                file_failed_num = 0
                file_moved_num = 0
                file_exists_num = 0
                directory_created_num = 0
                directory_removed_num = 0
                directory_enumerated_num = 0

                file_created_list = []
                file_recreated_list = []
                file_opened_list = []
                file_read_list = []
                file_written_list = []
                file_deleted_list = []
                file_failed_list = []
                directory_created_list = []
                directory_removed_list = []
                directory_enumerated_list = []

                jsonObj = json.load(fo)
                if "behavior" in jsonObj:
                    if "generic" in jsonObj["behavior"]:
                        generic_num = len(jsonObj["behavior"]["generic"])
                        if generic_num > 0:
                            for x in range(generic_num):
                                generic = jsonObj["behavior"]["generic"][x]
                                if "summary" in generic:
                                    if "file_created" in jsonObj["behavior"]["generic"][x]["summary"]:
                                        created_num = len(jsonObj["behavior"]["generic"][x]["summary"]["file_created"])
                                        if created_num > 0:
                                            # print mFile + " created_num: %d" %created_num
                                            for y in range(created_num):
                                                file_created_tmp = jsonObj["behavior"]["generic"][x]["summary"]["file_created"][y]
                                                # print key_open_tmp
                                                file_created_md5 = get_md5_value(file_created_tmp)
                                                # print "MD5 value: %s" %reg_md5
                                                if file_created_md5 not in file_created_list:
                                                    file_created_list.append(file_created_md5)
                                                    file_created_num += 1

                                    if "file_recreated" in jsonObj["behavior"]["generic"][x]["summary"]:
                                        recreated_num = len(jsonObj["behavior"]["generic"][x]["summary"]["file_recreated"])
                                        if recreated_num > 0:
                                            for y in range(recreated_num):
                                                file_recreated_tmp = jsonObj["behavior"]["generic"][x]["summary"]["file_recreated"][y]
                                                file_recreated_md5 = get_md5_value(file_recreated_tmp)
                                                if file_recreated_md5 not in file_recreated_list:
                                                    file_recreated_list.append(file_recreated_md5)
                                                    file_recreated_num += 1

                                    if "file_opened" in jsonObj["behavior"]["generic"][x]["summary"]:
                                        opened_num = len(jsonObj["behavior"]["generic"][x]["summary"]["file_opened"])
                                        if opened_num > 0:
                                            for y in range(opened_num):
                                                file_opened_tmp = jsonObj["behavior"]["generic"][x]["summary"]["file_opened"][y]
                                                file_opened_md5 = get_md5_value(file_opened_tmp)
                                                if file_opened_md5 not in file_opened_list:
                                                    file_opened_list.append(file_opened_md5)
                                                    file_opened_num += 1

                                    if "file_read" in jsonObj["behavior"]["generic"][x]["summary"]:
                                        read_num = len(jsonObj["behavior"]["generic"][x]["summary"]["file_read"])
                                        if read_num > 0:
                                            for y in range(read_num):
                                                file_read_tmp = jsonObj["behavior"]["generic"][x]["summary"]["file_read"][y]
                                                file_read_md5 = get_md5_value(file_read_tmp)
                                                if file_read_md5 not in file_read_list:
                                                    file_read_list.append(file_read_md5)
                                                    file_read_num += 1

                                    if "file_written" in jsonObj["behavior"]["generic"][x]["summary"]:
                                        written_num = len(jsonObj["behavior"]["generic"][x]["summary"]["file_written"])
                                        if written_num > 0:
                                            for y in range(written_num):
                                                file_written_tmp = jsonObj["behavior"]["generic"][x]["summary"]["file_written"][y]
                                                file_written_md5 = get_md5_value(file_written_tmp)
                                                if file_written_md5 not in file_written_list:
                                                    file_written_list.append(file_written_md5)
                                                    file_written_num += 1

                                    if "file_deleted" in jsonObj["behavior"]["generic"][x]["summary"]:
                                        deleted_num = len(jsonObj["behavior"]["generic"][x]["summary"]["file_deleted"])
                                        if deleted_num > 0:
                                            for y in range(deleted_num):
                                                file_deleted_tmp = jsonObj["behavior"]["generic"][x]["summary"]["file_deleted"][y]
                                                file_deleted_md5 = get_md5_value(file_deleted_tmp)
                                                if file_deleted_md5 not in file_deleted_list:
                                                    file_deleted_list.append(file_deleted_md5)
                                                    file_deleted_num += 1

                                    if "file_failed" in jsonObj["behavior"]["generic"][x]["summary"]:
                                        failed_num = len(jsonObj["behavior"]["generic"][x]["summary"]["file_failed"])
                                        if failed_num > 0:
                                            for y in range(failed_num):
                                                file_failed_tmp = jsonObj["behavior"]["generic"][x]["summary"]["file_failed"][y]
                                                file_failed_md5 = get_md5_value(file_failed_tmp)
                                                if file_failed_md5 not in file_failed_list:
                                                    file_failed_list.append(file_failed_md5)
                                                    file_failed_num += 1

                                    if "file_moved" in jsonObj["behavior"]["generic"][x]["summary"]:
                                        moved_num = len(jsonObj["behavior"]["generic"][x]["summary"]["file_moved"])
                                        if moved_num > 0:
                                            file_moved_num = moved_num

                                    if "file_exists" in jsonObj["behavior"]["generic"][x]["summary"]:
                                        exists_num = len(jsonObj["behavior"]["generic"][x]["summary"]["file_exists"])
                                        if exists_num > 0:
                                            file_exists_num = exists_num

                                    if "directory_created" in jsonObj["behavior"]["generic"][x]["summary"]:
                                        dir_created_num = len(jsonObj["behavior"]["generic"][x]["summary"]["directory_created"])
                                        if dir_created_num > 0:
                                            for y in range(dir_created_num):
                                                dir_created_tmp = jsonObj["behavior"]["generic"][x]["summary"]["directory_created"][y]
                                                dir_created_md5 = get_md5_value(dir_created_tmp)
                                                if dir_created_md5 not in directory_created_list:
                                                    directory_created_list.append(dir_created_md5)
                                                    directory_created_num += 1

                                    if "directory_removed" in jsonObj["behavior"]["generic"][x]["summary"]:
                                        dir_removed_num = len(jsonObj["behavior"]["generic"][x]["summary"]["directory_removed"])
                                        if dir_removed_num > 0:
                                            for y in range(dir_removed_num):
                                                dir_removed_tmp = jsonObj["behavior"]["generic"][x]["summary"]["directory_removed"][y]
                                                dir_removed_md5 = get_md5_value(dir_removed_tmp)
                                                if dir_removed_md5 not in directory_removed_list:
                                                    directory_removed_list.append(dir_removed_md5)
                                                    directory_removed_num += 1

                                    if "directory_enumerated" in jsonObj["behavior"]["generic"][x]["summary"]:
                                        dir_enumerated_num = len(jsonObj["behavior"]["generic"][x]["summary"]["directory_enumerated"])
                                        if dir_enumerated_num > 0:
                                            for y in range(dir_enumerated_num):
                                                dir_enumerated_tmp = jsonObj["behavior"]["generic"][x]["summary"]["directory_enumerated"][y]
                                                dir_enumerated_md5 = get_md5_value(dir_enumerated_tmp)
                                                if dir_enumerated_md5 not in directory_enumerated_list:
                                                    directory_enumerated_list.append(dir_enumerated_md5)
                                                    directory_enumerated_num += 1
                        else:
                            print mFile + " doesn't has file operation!"
                    else:
                        print mFile + " doesn't has file operation!"
                else:
                    print mFile + " doesn't has behavior!"

                print "file_created: %d" %file_created_num
                print "file_recreated: %d" %file_recreated_num
                print "file_opened: %d" %file_opened_num
                print "file_read: %d" %file_read_num
                print "file_written: %d" % file_written_num
                print "file_deleted: %d" % file_deleted_num
                print "file_failed: %d" % file_failed_num
                print "file_moved: %d" % file_moved_num
                print "file_exists: %d" % file_exists_num
                print "directory_created: %d" % directory_created_num
                print "directory_removed: %d" % directory_removed_num
                print "directory_enumerated: %d" % directory_enumerated_num

                standard["file_created"] = file_created_num
                standard["file_recreated"] = file_recreated_num
                standard["file_opened"] = file_opened_num
                standard["file_read"] = file_read_num
                standard["file_written"] = file_written_num
                standard["file_deleted"] = file_deleted_num
                standard["file_failed"] = file_failed_num
                standard["file_moved"] = file_moved_num
                standard["file_exists"] = file_exists_num
                # standard["directory_created"] = directory_created_num
                # standard["directory_removed"] = directory_removed_num
                # standard["directory_enumerated"] = directory_enumerated_num
                dataframelist.append(standard)
                num += 1

    df = pd.DataFrame(dataframelist)
    df.to_csv(file_path + 'APT_FileFeature.csv', index = False)

    end = time()
    print '\n'
    print '运行时间： %s 秒' % str(end - start)
    print 'Done successfully......'