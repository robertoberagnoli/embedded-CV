#!/bin/bash

raspivid -hf -o videoMirror.h264 -w 640 -h 480 -br 80 -co 100 -t 10000

MP4Box -add videoMirror.h264 videoMirror.mp4

rm videoMirror.h264

#curl -v --location --request POST 'http://134.122.67.125/v1/media/upload' --form 'file=@"/home/pi/videoMirror.mp4"' --form 'filename="videoMirror.mp4"' --form 'mimetype="video/mp4"'

rm videoMirror.mp4

