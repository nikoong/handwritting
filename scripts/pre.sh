#!/bin/bash

find *.jpg -exec /home/nikoong/Algorithm_test/handwritting/textcleaner  -g -f 25 -o 3 -s 1 {} /home/nikoong/Algorithm_test/handwritting/test_image_clean/{} \;
