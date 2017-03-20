#-*-coding:utf-8-*- 
import numpy as np
from PIL import Image
import os
import cv2
import random


#将多级目录下的所有图片文件,生成一个txt
#txt_name 不是完成路径，是一个标记，比如wrong，会在txt文件下生成一个wrong子目录
#is_random 是 bool类型(True/flase)，决定是否打乱txt
def gen_single_txt(data_path,txt_name,is_random):
    txt_path = os.path.join('/home/nikoong/Algorithm_test/handwritting/data/txt',txt_name)
    #创建目录
    os.mkdir(txt_path)
    txt = os.path.join(txt_path,txt_name+'.txt')
    #生成所有数据名list
    all_files = []
    for root, dirs,files in os.walk(data_path,topdown=False):
        for name in files:
            filename = os.path.join(root,name)
            all_files.append(filename)
    #打乱顺序
    if is_random:
        random.shuffle(all_files)
    #生成TXT
    with open(txt,'w') as f:
        for filename in all_files:
            f.write(filename+' '+filename.split('Value')[1].split('.jpg')[0]+'\n')



#将多级目录下的所有图片文件,生成train\val\test\三个txt,同上
def gen_tri_txt(data_path,txt_name,is_random):
    txt_path = os.path.join('/home/nikoong/Algorithm_test/handwritting/data/txt',txt_name)
    #创建目录
    os.mkdir(txt_path)
    train_txt = os.path.join(txt_path,'train.txt')
    val_txt = os.path.join(txt_path,'val.txt')
    test_txt = os.path.join(txt_path,'test.txt')
    #生成所有数据名list
    all_files = []
    for root, dirs,files in os.walk(data_path,topdown=False):
        for name in files:
            filename = os.path.join(root,name)
            all_files.append(filename)
    #打乱顺序
    if is_random:
        random.shuffle(all_files)
    #生成三部分数据
    leng = len(all_files)
    train_len = int(leng*0.5)
    val_len = int(leng*0.8)
    test_len = leng
 
    train_file =all_files[0:train_len]
    val_file =all_files[train_len+1:val_len]
    test_file =all_files[val_len+1:-1]

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


#解析train.txt文件，返回文件名列表和label列表
def Parsetxt(txt_path):
    file_list=[]
    label_list=[]
    with open(txt_path,'r') as f:
        for line in f:
            file_list.append(line.split(' ')[0])
            label_list.append(int(line.split(' ')[1]))
        return file_list, label_list   
        

#生成文件列表
def Makefilelist(data_path):
    filelist=[]
    files= os.listdir(data_path)
    for filename in files:
        fullfilename = os.path.join(data_path,filename)
        filelist.append(fullfilename)
    return filelist,files

#二值化
def binaryzation(input_image):
    bi_img = input_image
    (thresh, bi_img) = cv2.threshold(bi_img, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    return bi_img

#反色
def Inverse(input_image):
    img = input_image
    inverse_img = 255-img
    return inverse_img
#闭操作
def Close(input_image,kernel_width,kernel_height):
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(kernel_width, kernel_height))
    closed_img = cv2.morphologyEx(input_image, cv2.MORPH_CLOSE, kernel)  
    return closed_img


#膨胀
def Dilate(input_image,kernel_width,kernel_height):
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(kernel_width, kernel_height))
    dilated_img = cv2.dilate(input_image,kernel)
    return dilated_img
     
#去黑边
def Rm_Blackborder(input_image):
    img = input_image
    #上边
    while np.sum(img[0]) == 0:
        img = img[1:]
    #左边
    while np.sum(img[:,0]) == 0:
        img = img[:,1:]
    w,h = img.shape
    if (w==1 or h==1):return img
    #下边
    while np.sum(img[-1]) == 0:
        img = img[:-1]
    #右边
    w,h = img.shape
    if (w==1 or h==1):return img
    while np.sum(img[:,:-1]) == 0:
        img = img[:,:-1]
    return img

        

#resize
def Resize(input_image):
    img = input_image
    h,w = img.shape
    if max(w,h)>20:
        max_ = float(max(w,h))
        ratio = max_/20
        new_w = int(w/ratio)
        new_h = int(h/ratio)
        img = cv2.resize(img,(new_w,new_h))
    return img

#补边函数，补0到20*20，再补到28*28
def MakeBorder (input_image):
    h,w = input_image.shape
    img = input_image
    if((20-h)%2==0):
        top = (20-h)/2;
        bottom = (20-h)/2;
    else:
        top = (20-h)/2+1;
        bottom = (20-h)/2;
    if((20-w)%2==0):
        left = (20-w)/2;
        right = (20-w)/2;
    else:
        left = (20-w)/2+1;
        right = (20-w)/2;
    img_20 = cv2.copyMakeBorder(img, top, bottom, left, right, cv2.BORDER_CONSTANT,value=0)
    img_28 = cv2.copyMakeBorder(img_20, 4, 4, 4, 4, cv2.BORDER_CONSTANT,value=0)
    return img_28
#打印
def Print_img(input_img):
    for i in range(input_img.shape[0]):
        print '\n' 
        for j in  range(input_img.shape[1]):
            print input_img[i][j],' ',
#检测&保存
def Save_img(input_img,save_path):
    input_img = Image.fromarray(input_img)
    input_img.save(save_path)
