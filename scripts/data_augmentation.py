#-*- coding:utf-8 -*-
#增加数字“4”的数据量，对每个“4”的样例，生成一个新样例

from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
import Image
import methods
import random
import os

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


    output_path='/home/nikoong/Algorithm_test/handwritting/data/new_four/new_four_train'
    new_list=[]
    sourse_list = methods.txt2list('/home/nikoong/Algorithm_test/handwritting/data/txt/finish/train.txt')

    
    data_path = output_path
    '''
    for i in range(len(sourse_list)):
        if int(sourse_list[i].split(' ')[1])==4:
            imagepath = sourse_list[i].split(' ')[0]
            imagename = imagepath.split('/')[-1].split('.jpg')[0]
            methods.DataAugmentation(imagepath,1,output_path,imagename)
    '''   
    txt_name = 'new_four_train'
    gen_single_txt(data_path,txt_name,True)
    four_list = methods.txt2list('/home/nikoong/Algorithm_test/handwritting/data/txt/new_four_train.txt')
    sourse_list.extend(four_list)
    random.shuffle(sourse_list)
    methods.list2txt(sourse_list,'/home/nikoong/Algorithm_test/handwritting/data/txt/finish/train_withnewfour.txt')
    

    

   



