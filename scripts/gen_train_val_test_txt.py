#-*- coding:utf-8 -*-
import os
import random
from methods import gen_tri_txt

    #生成txt文件

    with open(train_txt,'w') as f:
        for filename in train_file:
            f.write(filename+' '+filename.split('Value')[1].split('.jpg')[0]+'\n')

    with open(val_txt,'w') as f:
        for filename in val_file:
            f.write(filename+' '+filename.split('Value')[1].split('.jpg')[0]+'\n')

    with open(test_txt,'w') as f:
        for filename in test_file:
            f.write(filename+' '+filename.split('Value')[1].split('.jpg')[0]+'\n')
if __name__ == '__main__':
    data_path = '/home/nikoong/Algorithm_test/handwritting/data/finish'
    txt_name = 'finish'
    gen_tri_txt(data_path,txt_name,True)

