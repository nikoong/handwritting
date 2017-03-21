#!/bin/bash
solver=/home/nikoong/Algorithm_test/handwritting/lenet/solver.prototxt
pretrained_model=/home/nikoong/Algorithm_test/handwritting/lenet/snapshots/history_snap/mnist_10000.caffemodel
log_name=ft_mnist_balance_lmdb
log=/home/nikoong/Algorithm_test/handwritting/lenet/log/${log_name}-`date +%Y-%m-%d-%H-%M`.log

finetune=1

if [ $finetune -eq 1 ];then 
    /home/nikoong/Algorithm_test/caffe-master/build/tools/caffe train \
      -solver ${solver} -weights ${pretrained_model} -gpu 0 2>&1 | tee ${log} 
else

    /home/nikoong/Algorithm_test/caffe-master/build/tools/caffe train \
      -solver ${solver} -gpu 0 2>&1 | tee ${log}
fi


#Resume Training
#snapshot=
#/home/nikoong/Algorithm_test/caffe-master/build/tools/caffe train --solver=${solver} --snapshot=${snapshot}
