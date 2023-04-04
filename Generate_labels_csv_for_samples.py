# coding=utf-8
import sys
reload(sys)
import json
import os
import csv
import pickle


if __name__ =="__main__":
    source_json_path = os.path.abspath('.') + '/Json/'
    BenignPrograms_json_path = source_json_path + 'BenignPrograms-json/'

    BaiXiang_json_path = source_json_path + 'BaiXiang-json/'
    DarkHotel_json_path = source_json_path + 'DarkHotel-json/'
    Mirage_json_path = source_json_path + 'Mirage-json/'
    NormanShark_json_path = source_json_path + 'NormanShark-json/'
    SinDigoo_json_path = source_json_path + 'SinDigoo-json/'

    BaiXiang_part_json_path = source_json_path + 'BaiXiang-Part-json/'
    DarkHotel_part_json_path = source_json_path + 'DarkHotel-Part-json/'
    NormanShark_part_json_path = source_json_path + 'NormanShark-Part-json/'
    SinDigoo_part_json_path = source_json_path + 'SinDigoo-Part-json/'


    Csv_path = os.path.abspath('.') + '/Label/'
    # 分别为正常样本+部分APT样本、所有APT样本建立label表
    firstline = ['Id', 'Class']

    Benign_Part_APT_Label_Csv = open(Csv_path + 'PartLabels.csv', 'wb')
    PartWriter = csv.writer(Benign_Part_APT_Label_Csv)  # 写入csv文件的初始化
    PartWriter.writerow(firstline)  # 按行写入

    APT_Label_Csv = open(Csv_path + 'APTLabels.csv', 'wb')
    AllWriter = csv.writer(APT_Label_Csv)
    AllWriter.writerow(firstline)

    # 首先为“正常样本+部分APT样本”生成label表，以模拟样本平衡的情况下的APT检测
    dirs = os.listdir(source_json_path)
    for dir in dirs:
        if dir == 'BenignPrograms-json':
            files = os.listdir(source_json_path + dir)
            count = 0
            for mFile in files:
                fileName = mFile[:-5]
                curRow = [fileName, '0']
                PartWriter.writerow(curRow)
                count += 1
            print 'BenignPrograms共计 %d 个！' %count
        if dir == 'BaiXiang-Part-json':
            files = os.listdir(source_json_path + dir)
            count = 0
            for mFile in files:
                fileName = mFile[:-5]
                curRow = [fileName, '1']
                PartWriter.writerow(curRow)
                count += 1
            print 'BaiXiang Part共计 %d 个！' %count
        if dir == 'DarkHotel-Part-json':
            files = os.listdir(source_json_path + dir)
            count = 0
            for mFile in files:
                fileName = mFile[:-5]
                curRow = [fileName, '1']
                PartWriter.writerow(curRow)
                count += 1
            print 'DarkHotel Part共计 %d 个！' % count
        if dir == 'Mirage-json':
            files = os.listdir(source_json_path + dir)
            count = 0
            for mFile in files:
                fileName = mFile[:-5]
                curRow = [fileName, '1']
                PartWriter.writerow(curRow)
                count += 1
            print 'Mirage Part共计 %d 个！' % count
        if dir == 'NormanShark-Part-json':
            files = os.listdir(source_json_path + dir)
            count = 0
            for mFile in files:
                fileName = mFile[:-5]
                curRow = [fileName, '1']
                PartWriter.writerow(curRow)
                count += 1
            print 'NormanShark Part共计 %d 个！' % count
        if dir == 'SinDigoo-Part-json':
            files = os.listdir(source_json_path + dir)
            count = 0
            for mFile in files:
                fileName = mFile[:-5]
                curRow = [fileName, '1']
                PartWriter.writerow(curRow)
                count += 1
            print 'SinDigoo Part共计 %d 个！' % count

        # 下面，将所有的APT样本标签写入到一个csv表格中，每一类APT赋予一个标签，开展分类实验
        if dir == 'BaiXiang-json':
            files = os.listdir(source_json_path + dir)
            count = 0
            for mFile in files:
                fileName = mFile[:-5]
                curRow = [fileName, '1']
                AllWriter.writerow(curRow)
                count += 1
            print 'BaiXiang共计 %d 个！' % count
        if dir == 'DarkHotel-json':
            files = os.listdir(source_json_path + dir)
            count = 0
            for mFile in files:
                fileName = mFile[:-5]
                curRow = [fileName, '2']
                AllWriter.writerow(curRow)
                count += 1
            print 'DarkHotel共计 %d 个！' % count
        if dir == 'Mirage-json':
            files = os.listdir(source_json_path + dir)
            count = 0
            for mFile in files:
                fileName = mFile[:-5]
                curRow = [fileName, '3']
                AllWriter.writerow(curRow)
                count += 1
            print 'Mirage共计 %d 个！' % count
        if dir == 'NormanShark-json':
            files = os.listdir(source_json_path + dir)
            count = 0
            for mFile in files:
                fileName = mFile[:-5]
                curRow = [fileName, '4']
                AllWriter.writerow(curRow)
                count += 1
            print 'NormanShark共计 %d 个！' % count
        if dir == 'SinDigoo-json':
            files = os.listdir(source_json_path + dir)
            count = 0
            for mFile in files:
                fileName = mFile[:-5]
                curRow = [fileName, '5']
                AllWriter.writerow(curRow)
                count += 1
            print 'SinDigoo共计 %d 个！' % count

    Benign_Part_APT_Label_Csv.close()
    APT_Label_Csv.close()
    print "done"