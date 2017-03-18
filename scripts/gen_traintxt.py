#-*- coding:utf-8 -*-
import os
import random
#�༶Ŀ¼�µ��ļ�,����txt
def gen_txt(data_path,txt_name,random_):
    txt_path = os.path.join('/home/nikoong/Algorithm_test/handwritting/data/txt',txt_name)
    #����Ŀ¼
    os.mkdir(txt_path)
    train_txt = os.path.join(txt_path,'train.txt')
    val_txt = os.path.join(txt_path,'val.txt')
    test_txt = os.path.join(txt_path,'test.txt')
    #��������������list
    all_files = []
    for root, dirs,files in os.walk(data_path,topdown=False):
        for name in files:
            filename = os.path.join(root,name)
            all_files.append(filename)
    #����˳��
    if random_:
        random.shuffle(all_files)
    #��������������
    leng = len(all_files)
    train_len = int(leng*0.5)
    val_len = int(leng*0.8)
    test_len = leng
 
    train_file =all_files[0:train_len]
    val_file =all_files[train_len+1:val_len]
    test_file =all_files[val_len+1:-1]

    #����txt�ļ�

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
    gen_txt(data_path,txt_name,True)

