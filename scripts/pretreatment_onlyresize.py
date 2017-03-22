#-*-coding:utf-8-*- 
import numpy as np
from PIL import Image
import os
import cv2
import methods

#主函数
def main():
    data_path ='/home/nikoong/Algorithm_test/handwritting/data/origin_data/clean/cut2'
    save_path ='/home/nikoong/Algorithm_test/handwritting/data/onlyresize/data2'
    if (not os.path.isdir(save_path)):
        os.makedirs(save_path)
    filelist,files = methods.Makefilelist(data_path)
    for i in range(len(filelist)):
        if i%2000==0:print i
        img = Image.open(filelist[i])
        img = np.array(img)
        h,w = img.shape # nparray.shape返回行数、列数
        if (h*w > 0 and h>w):
            img = methods.Binaryzation(img)
            img = methods.Inverse(img)
            if sum(sum(img)) == 0:continue           
            img = methods.Resize(img,28)
            methods.Save_img(img,os.path.join(save_path,files[i]))


if __name__ == "__main__":
    main()

