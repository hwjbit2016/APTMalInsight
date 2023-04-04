# coding: utf-8
import os
import shutil

##
def read_ontop_list_txt():
    ontop_txt = os.path.abspath(".") + "/tmp/0328.txt"
    ontop_target_path = os.path.abspath('.') + '/tmp/0328-bak.txt'

    sub_str_list = []
    str_list = []

    with open(ontop_txt, 'r') as fo:
        line = fo.readline()
        string = line.strip()
        api = string.split(':')[0]
        cate = string.split(':')[1]
        prob = string.split(':')[2]

        sub_str_list.append(api)

        for line in fo:
            string2 = line.strip()
            api2 = string2.split(':')[0]
            cate2 = string2.split(':')[1]
            prob2 = string2.split(':')[2]

            if cate2 == cate:
                sub_str_list.append(api2)
                continue
            else:
                cate = cate2
                if len(sub_str_list) > 1:
                    str_list.append(sub_str_list)
                sub_str_list = []
                sub_str_list.append(api2)
    fo.close()

    # print(str_list)
    with open(ontop_target_path, 'w') as ro:
        for i in range(len(str_list)):
            onto_str = str_list[i]
            str_tmp = []
            for j in range(len(onto_str)):
                str_tmp.append(onto_str[j])
                str_tmp.append(' ')
            ro.writelines(str_tmp)
    ro.close()

##
def read_ontop_list_from_txt_withinset(ontop_dir_path, ontop_target_path):
    cate_set = ['file', 'process', 'registry', 'network']

    # ontop_txt = os.path.abspath(".") + "/tmp/0328.txt"
    # ontop_target_path = os.path.abspath('.') + '/tmp/0328-bak1.txt'

    sub_str_list = []
    str_list = []

    with open(ontop_dir_path, 'r') as fo:
        first_line = fo.readline()
        first_string = first_line.strip()
        first_api = first_string.split(':')[0]
        first_cate = first_string.split(':')[1]
        first_prob = first_string.split(':')[2]

        if first_cate in cate_set:
            sub_str_list.append(first_api)

        for line in fo:
            string = line.strip()
            api = string.split(':')[0]
            cate = string.split(':')[1]
            prob = string.split(':')[2]

            if cate in cate_set:
                sub_str_list.append(api)
                continue
            else:
                if len(sub_str_list) > 1:
                    str_list.append(sub_str_list)
                sub_str_list = []
        fo.close()


    with open(ontop_target_path, 'w') as ro:
        for i in range(len(str_list)):
            onto_str = str_list[i]
            j = 0
            str_tmp = []
            while j < len(onto_str):
                str_tmp.append(onto_str[j])
                str_tmp.append(' ')
                j += 1
            ro.writelines(str_tmp)
            ro.writelines('\n')
    ro.close()

##
def read_ontop_list_from_txt_withinset_test():
    cate_set = ['file', 'process', 'registry', 'network']

    ontop_txt = os.path.abspath(".") + "/tmp/0329-1.txt"
    ontop_target_path = os.path.abspath('.') + '/tmp/0329-bak1.txt'

    sub_str_list = []
    str_list = []

    with open(ontop_txt, 'r') as fo:
        first_line = fo.readline()
        first_string = first_line.strip()
        first_api = first_string.split(':')[0]
        first_cate = first_string.split(':')[1]
        first_prob = first_string.split(':')[2]

        if first_cate in cate_set:
            sub_str_list.append(first_api)

        for line in fo:
            string = line.strip()
            print(string)
            api = string.split(':')[0]
            cate = string.split(':')[1]
            prob = string.split(':')[2]

            if cate in cate_set:
                sub_str_list.append(api)
                continue
            else:
                if len(sub_str_list) > 1:
                    str_list.append(sub_str_list)
                sub_str_list = []
        fo.close()


    with open(ontop_target_path, 'w') as ro:
        for i in range(len(str_list)):
            onto_str = str_list[i]
            j = 0
            str_tmp = []
            while j < len(onto_str):
                str_tmp.append(onto_str[j])
                str_tmp.append(' ')
                j += 1
            ro.writelines(str_tmp)
            ro.writelines('\n')
    ro.close()

##
def generate_ontop_list_into_file(dir_path, dest_path):
    infiles = os.listdir(dir_path)
    for mFile in infiles:
        infilename = dir_path + mFile
        outfilename = dest_path + mFile

        if os.path.getsize(infilename) > 0:
            read_ontop_list_from_txt_withinset(infilename, outfilename)
            print('%s will be handled!' %(infilename))
        else:
            print('--------------------------')
            print('%s is empty!' %(infilename))
            print('--------------------------')


####-----------####
def main():
    APT_Array = ['BaiXiang', 'DarkHotel', 'Mirage', 'NormanShark', 'SinDigoo']
    Root_Path = os.path.abspath('.') + '/APT_Samples_ApiCategory_To_TXT_With_Prob/'
    Dest_Path = os.path.abspath('.') + '/APT_Ontop_List_WithinSet/'

    for i in range(len(APT_Array)):
        curDir = APT_Array[i]
        dir_path = Root_Path + curDir + '/'
        dest_path = Dest_Path + curDir + '/'
        if not os.path.exists(dest_path):
            os.mkdir(dest_path)

        generate_ontop_list_into_file(dir_path, dest_path)

    # read_ontop_list_txt()
    # read_ontop_list_from_txt_withinset()
    # read_ontop_list_from_txt_withinset_test()

    print 'Well done!'


if __name__ == '__main__':
    main()