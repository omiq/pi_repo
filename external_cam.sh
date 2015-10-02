#!/bin/bash
while :;
do
	#fswebcam -d /dev/video0 -r 640x480 /home/pi/www/webcam.jpg
	fswebcam -c /home/pi/.fswebcam.conf
	sleep 0.10;
done;

