#!/bin/bash

mkdir -p $1/output

for f in $1/*
do
    echo "Processing file: "$f
    ffmpeg -i $f -ac 1 -ar 22050 $1/output/"${f##*/}"
done
