#!/bin/bash
:<<USAGE
Usage:
    ./plot_training_log.py chart_type[0-7] /where/to/save.png /path/to/first.log ...
Notes:
    1. Supporting multiple logs.
    2. Log file name must end with the lower-cased ".log".
Supported chart types:
    0: Test accuracy  vs. Iters
    1: Test accuracy  vs. Seconds
    2: Test loss  vs. Iters
    3: Test loss  vs. Seconds
    4: Train learning rate  vs. Iters
    5: Train learning rate  vs. Seconds
    6: Train loss  vs. Iters
    7: Train loss  vs. Seconds
blank
USAGE

log_name=new_four_continue_continue-2017-03-25-20-47.log
pic_name=new_four_continue_continue_acc
num=0 #0 acc/6 train_loss/2 test_loss
./plot_training_log.py ${num} ${pic_name}.png ${log_name}
