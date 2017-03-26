#-*- coding:utf-8 -*-
import os
import random
#from methods import gen_single_txt


def gen_single_txt(data_path,txt_name,is_random = True):
    txt_path = os.path.join('/home/nikoong/Algorithm_test/handwritting/data/txt')
    txt = os.path.join(txt_path,txt_name+'.txt')
    all_files = []
    for root, dirs,files in os.walk(data_path,topdown=False):
        for name in files:
            filename = os.path.join(root,name)
            all_files.append(filename)
    if is_random:
        random.shuffle(all_files)
    with open(txt,'w') as f:
        for filename in all_files:
            f.write(filename+' '+'4'+'\n')

if __name__ == '__main__':
    data_path = '/home/nikoong/Algorithm_test/handwritting/data/finish/new_four'
    txt_name = 'new_four'
    gen_single_txt(data_path,txt_name,True)

