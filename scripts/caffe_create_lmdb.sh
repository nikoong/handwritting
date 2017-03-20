#!/usr/bin/env sh
# Set RESIZE=true to resize the images to 256x256. Leave as false if images have
# already been resized using another tool.

TOOLS=/home/nikoong/Algorithm_test/caffe-master/build/tools

TRAIN_TXT=/home/nikoong/Algorithm_test/handwritting/data/txt/finish/train.txt
VAL_TXT=/home/nikoong/Algorithm_test/handwritting/data/txt/finish/val.txt
TEST_TXT=/home/nikoong/Algorithm_test/handwritting/data/txt/finish/test.txt

TRAIN_LMDB=/home/nikoong/Algorithm_test/handwritting/data/lmdb/finish/train_lmdb
VAL_LMDB=/home/nikoong/Algorithm_test/handwritting/data/lmdb/finish/val_lmdb
ROOT=/

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
