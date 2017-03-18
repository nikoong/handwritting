#-*-coding:utf-8-*- 
import numpy as np
from PIL import Image
import os
import cv2

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
#主函数
def main():
    data_path ='/home/nikoong/Algorithm_test/handwritting/data/clean/cut1'
    save_path ='/home/nikoong/Algorithm_test/handwritting/data/finish/data1'
    filelist,files = Makefilelist(data_path)
    #print data2 filelist[11993],"\n",filelist[31056],"\n",filelist[81690]
    for i in range(len(filelist)):
        if i%2000==0:print i
        img = Image.open(filelist[i])
        img = np.array(img)
        h,w = img.shape # nparray.shape返回行数、列数
        if (h*w > 0 and h>w):
            img = binaryzation(img)
            img = Inverse(img)
            if sum(sum(img)) == 0:continue      
            #img = Dilate(img,3,3)
            #img = Close(img,3,3)
            img = Rm_Blackborder(img)
            if sum(sum(img)) == 0:continue      
            img = Resize(img)
            img = MakeBorder(img)
            Save_img(img,os.path.join(save_path,files[i]))


if __name__ == "__main__":
    main()

