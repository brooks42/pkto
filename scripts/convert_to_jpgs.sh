#!/bin/bash
for image in *;
do 
    convert "$image" -quality 30 JPEG:"jpgs/${image%.*}.jpg" 
done