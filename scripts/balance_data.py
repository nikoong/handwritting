import numpy as np
import methods
import random 

  

                

txt_path = '/home/nikoong/Algorithm_test/handwritting/data/txt/newfour/train_withnewfour.txt'

balance_txt_path = '/home/nikoong/Algorithm_test/handwritting/data/txt/newfour/balance_trainnewfour.txt'
txt_list = methods.txt2list(txt_path)
txt_list = methods.reduce_samples(txt_list,7000)
methods.list2txt(txt_list,balance_txt_path)
txt_list = methods.txt2list(balance_txt_path)
print 'train'
for i in range(10):
    num = methods.count_list(txt_list,i)
    print num    
print '\n'

'''
txt_path = '/home/nikoong/Algorithm_test/handwritting/data/txt/newfour/val_withnewfour.txt'
balance_txt_path = '/home/nikoong/Algorithm_test/handwritting/data/txt/newfour/balance_valnewfour.txt'
txt_list = methods.txt2list(txt_path)  
print 'test'
txt_list = methods.reduce_samples(txt_list,3000)
methods.list2txt(txt_list,balance_txt_path)
for i in range(10):
    num = methods.count_list(txt_list,i)
    print num  
print '\n' 
'''
