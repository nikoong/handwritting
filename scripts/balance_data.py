import numpy as np
import methods
import random 

  

                

txt_path = '/home/nikoong/Algorithm_test/handwritting/data/txt/finish/train.txt'
sourse_path = '/home/nikoong/Algorithm_test/handwritting/data/txt/mnist/mnist_train.txt'
balance_txt_path = '/home/nikoong/Algorithm_test/handwritting/data/txt/finish/balance_train.txt'
txt_list = methods.txt2list(txt_path)
txt_list = methods.increase_samples(txt_list,6000,sourse_path)
txt_list = methods.reduce_samples(txt_list,7000)
methods.list2txt(txt_list,balance_txt_path)
print 'train'
for i in range(10):
    num = methods.count_list(txt_list,i)
    print num    
print '\n'


txt_path = '/home/nikoong/Algorithm_test/handwritting/data/txt/finish/test.txt'
sourse_path = '/home/nikoong/Algorithm_test/handwritting/data/txt/mnist/mnist_test.txt'
balance_txt_path = '/home/nikoong/Algorithm_test/handwritting/data/txt/finish/balance_test.txt'
txt_list = methods.txt2list(txt_path)  
print 'test'
txt_list = methods.increase_samples(txt_list,2000,sourse_path)
txt_list = methods.reduce_samples(txt_list,2000)
methods.list2txt(txt_list,balance_txt_path)
for i in range(10):
    num = methods.count_list(txt_list,i)
    print num  
print '\n' 
