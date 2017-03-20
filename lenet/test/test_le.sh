#!/bin/bash
pretrained_model=/home/nikoong/Algorithm_test/handwritting/lenet/snapshots/finish_random_2W_iter_30000.caffemodel

net=/home/nikoong/Algorithm_test/handwritting/lenet/test/test_lenet_lmdb.prototxt

/home/nikoong/Algorithm_test/caffe-master/build/tools/caffe test  \
      -model ${net}\
      -weights ${pretrained_model}  -gpu 0 -iterations 3

