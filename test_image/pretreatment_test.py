#-*-coding:utf-8-*- 
import numpy as np
from PIL import Image
import os
import cv2


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
     
def 

#去黑边
def Rm_Blackborder(input_image):
    img = input_image
    #上边
    while np.sum(img[0]) == 0:
        img = img[1:] 
    #左边
    while np.sum(img[:,0]) == 0:
        img = img[:,1:]
    #下边
    while np.sum(img[-1]) == 0:
        img = img[:-1]
    #右边
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
#检测
def Check_save_img(input_img,save_path):
    h,w = input_img.shape
    if (h*w > 0):
        input_img = Image.fromarray(input_img)
        input_img.save(save_path)
#主函数
def main():
    data_path ='/home/nikoong/Algorithm_test/handwritting/test_image/1.jpg'
    img = Image.open(data_path)
    img = np.array(img)
    img = binaryzation(img)
    img = Inverse(img)
    img = Rm_Blackborder(img)
    img = Resize(img)
    img = Close(img,3,3)
    #img = Dilate(img,3,3)
    img = MakeBorder(img)
    Print_img(img)
    Check_save_img(img,'/home/nikoong/Algorithm_test/handwritting/test_image/1_finish.jpg')

    
if __name__ == "__main__":
    main()

