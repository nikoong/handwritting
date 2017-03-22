#-*-coding:utf-8-*-
#从txt生成预测序列
import numpy as np
from sklearn.metrics import confusion_matrix


true_y = []
pre_y = []
with open('/home/nikoong/Algorithm_test/handwritting/data/txt/finish/wrong.txt','r') as f:
    for line in f:  
        value = line.split(' ')[1].split('\n')[0]
        if (value == '0' or value == '1' or value == '2' or value == '3' or value == '4' or\
value == '5' or value == '6' or value == '7' or value == '8' or value == '9' ):
            true_y.append(value)
        else: print 'errror happened in ',line

        prediction = line.split('prediction')[1].split('_')[0]
        if (prediction == '0' or prediction == '1' or prediction == '2' or prediction == '3' or prediction == '4' or\
prediction == '5' or prediction == '6' or prediction == '7' or prediction == '8' or prediction == '9' ):
            pre_y.append(prediction)
        else: print 'errror happened in ',line

    if(len(true_y)==len(pre_y)):
        print 'len(true_y)=len(pre_y) =',len(true_y)
    else:
        print 'true_y',len(true_y)
        print 'pre_y',len(pre_y)

con_matrix = confusion_matrix(true_y, pre_y, labels=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
print con_matrix
        
        


        
 

        
