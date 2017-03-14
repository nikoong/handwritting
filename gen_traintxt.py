#-*- coding:utf-8 -*-
import os


data_path ='/home/nikoong/Algorithm_test/handwritting/data_crop/data2_28*28'
filelist=[]
files= os.listdir(data_path)
for filename in files:
    fullfilename = os.path.join(data_path,filename)
    filelist.append(fullfilename)
with open('/home/nikoong/Algorithm_test/handwritting/data_crop/txt/data2_28*28.txt','w') as f:
    for i in filelist: 
        f.write(str(i)+' '+str(i).split('Value')[1].split('.jpg')[0]+'\n')



