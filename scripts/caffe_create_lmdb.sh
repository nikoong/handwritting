#!/usr/bin/env sh
# Set RESIZE=true to resize the images to 256x256. Leave as false if images have
# already been resized using another tool.



TRAIN_TXT=/home/nikoong/Algorithm_test/handwritting/data/txt/newfour/train.txt
VAL_TXT=/home/nikoong/Algorithm_test/handwritting/data/txt/newfour/val.txt

TRAIN_LMDB=/home/nikoong/Algorithm_test/handwritting/data/lmdb/newfour/train_withnewfour_lmdb
VAL_LMDB=/home/nikoong/Algorithm_test/handwritting/data/lmdb/newfour/val_withnewfour_lmdb


ROOT=/
TOOLS=/home/nikoong/Algorithm_test/caffe-master/build/tools
RESIZE=false
if $RESIZE; then
  RESIZE_HEIGHT=28
  RESIZE_WIDTH=28
else
  RESIZE_HEIGHT=0
  RESIZE_WIDTH=0
fi

if [ ! -d "$ROOT" ]; then
  echo "Error: ROOT is not a path to a directory: $ROOT"
  echo "Set the ROOT variable to the path" \
       "where the data is stored."
  exit 1
fi


echo "Creating train lmdb..."
GLOG_logtostderr=1 $TOOLS/convert_imageset \
    --gray \
    --shuffle \
    ${ROOT} \
    ${TRAIN_TXT} \
    ${TRAIN_LMDB}


echo "Creating val lmdb..."
GLOG_logtostderr=1 $TOOLS/convert_imageset \
    --gray \
    --shuffle \
    ${ROOT} \
    ${VAL_TXT} \
    ${VAL_LMDB}

echo "Done."
