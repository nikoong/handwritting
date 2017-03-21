#-*- coding:utf-8 -*-
import sys
import methods
import cv2
import os 
from sklearn.metrics import confusion_matrix 
#%matplotlib inline  
caffe_root = '/home/nikoong/Algorithm_test/caffe-master'
sys.path.append(caffe_root+'python')  
import caffe  
 
net_file = '/home/nikoong/Algorithm_test/handwritting/lenet/lenet_deploy.prototxt'
pretrained = '/home/nikoong/Algorithm_test/handwritting/lenet/snapshots/ft_finish_randomdata_2W_lmdb_iter_30000.caffemodel'
txtpath = '/home/nikoong/Algorithm_test/handwritting/data/txt/finish/val.txt'
error_pic_path = '/home/nikoong/Algorithm_test/handwritting/data/wrong_new/'
#os.mkdir(error_pic_path)


net = caffe.Classifier(net_file, pretrained,raw_scale=1, image_dims=(28,28))   
caffe.set_mode_gpu
filelist,labellist = methods.Parsetxt(txtpath)#labellist 是int列表
error_image_list =[]
error_image_new_list =[]
error_num = 0  
true_y = []
pre_y = []
 
for i in range(len(filelist)):
    input_image = caffe.io.load_image(filelist[i], color=False)
    prediction = net.predict([input_image])
    true_y.append(labellist[i])
    pre_y.append(prediction[0].argmax())
    
    if prediction[0].argmax() !=  labellist[i]:
        error_num = error_num+1                
        imagename = filelist[i].split('/')[-1]
        #文件名prediction1_023688214359_20170115143145_y_ID20_Value4.jpg
        error_image_new_name = os.path.join(error_pic_path,"prediction"+str(prediction[0].argmax())+"_"+imagename)
        #保存图片
        #img = cv2.imread(filelist[i])
        #cv2.imwrite(error_image_new_name, img)
    if i%5000 == 0:
        print "error_num/total = ",error_num ,'/',i       
print "error_num/total = ",error_num ,'/',len(filelist)
con_matrix = confusion_matrix(true_y, pre_y, labels=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) 
print "confusion_matrix",con_matrix
#predictions: (N x C)  (1 x 10)ndarray of class probabilities for N images and C classes.


