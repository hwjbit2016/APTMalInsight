# -*- coding: utf-8 -*-
import os
import csv
import numpy as np
import operator
import string
from sklearn.metrics import confusion_matrix

api_Top_N = 50

family_list = ['BenignPrograms', 'BackDoor', 'Constructor', 'Email-Worm', 'Hoax', 'Rootkit']

#========== 对加壳的API进行处理  ==========#
def Handle_Packed_API(packedAPI):
    if packedAPI.startswith('?'):
        print packedAPI
        if 'exception' in packedAPI:
            getAPI = 'exception'
        elif 'type_info' in packedAPI:
            getAPI = 'type_info'
        elif 'terminate' in packedAPI:
            getAPI = 'terminate'
        elif 'error' in packedAPI:
            getAPI = 'error'
        elif 'out_of_range' in packedAPI:
            getAPI = 'out_of_range'
        elif 'basic_ostream' in packedAPI:
            getAPI = 'basic_ostream'
        elif 'basic_ios' in packedAPI:
            getAPI = 'basic_ios'
        elif 'basic_ostream' in packedAPI:
            getAPI = 'basic_ostream'
        elif 'basic_streambuf' in packedAPI:
            getAPI = 'basic_streambuf'
        elif 'bad_alloc' in packedAPI:
            getAPI = 'bad_alloc'
        elif 'error_map' in packedAPI:
            getAPI = 'error_map'
        elif 'Lockit' in packedAPI:
            getAPI = 'Lockit'
        elif 'basic_string' in packedAPI:
            getAPI = 'basic_string'
        elif 'Container_base' in packedAPI:
            getAPI = 'Container_base'
        elif 'bad_cast' in packedAPI:
            getAPI = 'bad_cast'
        elif 'basic_istream' in packedAPI:
            getAPI = 'basic_istream'
        elif 'locale' in packedAPI:
            getAPI = 'locale'
        elif 'ios_base' in packedAPI:
            getAPI = 'ios_base'
        elif 'bad_function_call' in packedAPI:
            getAPI = 'bad_function_call'
        elif 'basic_ostringstream' in packedAPI:
            getAPI = 'basic_ostringstream'
        elif 'codecvt' in packedAPI:
            getAPI = 'codecvt'
        elif 'iobuf' in packedAPI:
            getAPI = 'iobuf'
        elif 'allocate' in packedAPI:
            getAPI = 'allocate'
        elif 'Locinfo' in packedAPI:
            getAPI = 'Locinfo'
        elif 'Mutex' in packedAPI:
            getAPI = 'Mutex'
        elif 'QEventDispatcherWin32' in packedAPI:
            getAPI = 'QEventDispatcherWin32'
        elif 'setw' in packedAPI:
            getAPI = 'setw'
        elif 'Yarn' in packedAPI:
            getAPI = 'Yarn'
        elif 'DirectUI' in packedAPI:
            getAPI = 'DirectUI'
        elif 'length' in packedAPI:
            getAPI = 'length'
        elif 'Throw' in packedAPI:
            getAPI = 'Throw'
        elif 'QPoint' in packedAPI:
            getAPI = 'QPoint'
        elif 'QByteArray' in packedAPI:
            getAPI = 'QByteArray'
        elif 'QString' in packedAPI:
            getAPI = 'QString'
        elif 'GUID' in packedAPI:
            getAPI = 'GUID'
        elif 'util' in packedAPI:
            getAPI = 'util'
        elif 'slot_base' in packedAPI:
            getAPI = 'slot_base'
        elif 'resource' in packedAPI:
            getAPI = 'resource'
        elif 'trackable' in packedAPI:
            getAPI = 'trackable'
        elif 'QVariant' in packedAPI:
            getAPI = 'QVariant'
        elif 'BULL' in packedAPI:
            getAPI = 'BULL'
        elif 'handler' in packedAPI:
            getAPI = 'handler'
        elif 'ios_base' in packedAPI:
            getAPI = 'ios_base'
        elif 'wui' in packedAPI:
            getAPI = 'wui'
        elif 'cui' in packedAPI:
            getAPI = 'cui'
        elif 'sigc' in packedAPI:
            getAPI = 'sigc'
        elif 'string' in packedAPI:
            getAPI = 'string'
        elif 'Xlen' in packedAPI:
            getAPI = 'Xlen'
        elif 'QT' in packedAPI:
            getAPI = 'QT'
        elif 'Xran' in packedAPI:
            getAPI = 'Xran'
        else:
            getAPI = ''
    else:
        getAPI = packedAPI

    return getAPI


#计算TP、FP、FN、TN等参数
def print_confusion_matrix(y_true, y_pred):
    cm = confusion_matrix(y_true, y_pred)
    print ('Ture positive = ', cm[0][0])
    print ('False positive = ', cm[0][1])
    print ('False negative = ', cm[1][0])
    print ('True negative = ', cm[1][1])