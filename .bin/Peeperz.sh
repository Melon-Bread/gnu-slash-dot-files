#!/usr/bin/env bash

ffmpeg -f x11grab -r 30 -s 1920x1080 -i :0.0+1105,600 -vcodec rawvideo -pix_fmt yuv420p -threads 0 -f v4l2 /dev/video0
