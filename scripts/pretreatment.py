#-*-coding:utf-8-*- 
import numpy as np
from PIL import Image
import os
import cv2

#生成文件列表
def makefilelist(data_path):
    filelist=[]
    files= os.listdir(data_path)
    for filename in files:
        fullfilename = os.path.join(data_path,filename)
        filelist.append(fullfilename)
    return filelist,files


#反色
def inverse(test_image):
    img_ = np.array(test_image)
    inverse_img = 255-img_
    inverse_img = Image.fromarray(inverse_img)
    return inverse_img

#resize
def resize(test_image):
    img = test_image
    w,h = img.size
    if max(w,h)>20:
        max_ = float(max(w,h))
        ratio = max_/20
        new_w = int(w/ratio)
        new_h = int(h/ratio)
        img = img.resize((new_w,new_h), Image.ANTIALIAS)
    return img

#补边函数，补0到20*20，再补到28*28
def MakeBorder (test_image):
    w,h = test_image.size
    img =  np.array(test_image)
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
    img_28 = Image.fromarray(img_28)
    return img_28

#主函数
def main():
    data_path ='/home/nikoong/Algorithm_test/handwritting/data_crop/data2_cut'
    save_path ='/home/nikoong/Algorithm_test/handwritting/data_crop/data2_28*28'
    filelist,files = makefilelist(data_path)
    for i in range(len(filelist)):
        if i%5000==0:print i
        img = Image.open(filelist[i])
        img = inverse(img)
        img = resize(img)
        img = MakeBorder(img)
        img.save(os.path.join(save_path,files[i]))

if __name__ == "__main__":
    main()

