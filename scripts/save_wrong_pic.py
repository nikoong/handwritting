#-*- coding:utf-8 -*-
import sys
import methods
import cv2
import os  
#%matplotlib inline  
caffe_root = '/home/nikoong/Algorithm_test/caffe-master'
sys.path.append(caffe_root+'python')  
import caffe  
 
net_file = '/home/nikoong/Algorithm_test/handwritting/lenet/lenet_deploy.prototxt'
pretrained = '/home/nikoong/Algorithm_test/handwritting/lenet/snapshots/finish_random_2W_iter_30000.caffemodel'
txtpath = '/home/nikoong/Algorithm_test/handwritting/data/txt/finish/val.txt'
error_pic_path = '/home/nikoong/Algorithm_test/handwritting/data/wrong/'
os.mkdir(error_pic_path)

print "new net"
net = caffe.Classifier(net_file, pretrained,raw_scale=1, image_dims=(28,28))   
print "net set OK"
caffe.set_mode_gpu

print "start"
filelist,labellist = methods.Parsetxt(txtpath)
error_image_list =[]
error_image_new_list =[]
error_num = 0  
 
for i in range(len(filelist)):
    input_image = caffe.io.load_image(filelist[i], color=False)
    prediction = net.predict([input_image])
    if prediction[0].argmax() !=  labellist[i]:
        error_num = error_num+1                
        imagename = filelist[i].split('/')[-1]
        #prediction1_023688214359_20170115143145_y_ID20_Value4.jpg
        error_image_new_name = os.path.join(error_pic_path,"prediction"+str(prediction[0].argmax())+"_"+imagename)
        #print error_image_new_name
        img = cv2.imread(filelist[i])
        cv2.imwrite(error_image_new_name, img)
    if i%5000 == 0: print "error_num/total = ",error_num ,'/',i

        
print "error_num/total = ",error_num ,'/',len(filelist)
      
#predictions: (N x C)  e.x.(1 x 10) ndarray of class probabilities for N images and C classes.


