#-*- coding:utf-8 -*-
import os
import random
from methods import gen_single_txt


if __name__ == '__main__':
    data_path = '/home/nikoong/dataset/mnist/imgs_test'
    txt_name = 'mnist_test'
    gen_single_txt(data_path,txt_name,False)
