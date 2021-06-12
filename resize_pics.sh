#!/bin/bash

# Script to resize images in current directory to a dir named "resized"

mkdir -p resized
for f in *.{JPG,JPEG,PNG,jpg,jpeg,png}; do
    # resize if match is found (first char is not "*")
    if [[ ${f:0:1} != "*" ]]; then
        mogrify -path resized -resize 50% $f
    fi
done
