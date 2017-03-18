#!/bin/bash
solver=/home/nikoong/Algorithm_test/handwritting/lenet/lenet_solver_my.prototxt
pretrained_model=/home/nikoong/Algorithm_test/handwritting/lenet/snapshots/finish_random_iter_30000.caffemodel
log_name=finish_randomdata_2W
log=/home/nikoong/Algorithm_test/handwritting/lenet/log/${log_name}-`date +%Y-%m-%d-%H-%M`.log

finetune=1

if [ $finetune -eq 1 ];then 
    /home/nikoong/Algorithm_test/caffe-master/build/tools/caffe train \
      -solver ${solver} -weights ${pretrained_model} -gpu 0 2>&1 | tee ${log} 
else

    /home/nikoong/Algorithm_test/caffe-master/build/tools/caffe train \
      -solver ${solver} -gpu 0 2>&1 | tee ${log}
fi
