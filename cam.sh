#!/bin/bash

# Set the date variable to the current date and time
DATE=$(date +"%Y-%m-%d_%H%M")

# Take the picture and save with the date as filename
raspistill --rotation 270 -w 1024 -h 768 -o /home/pi/pics/$DATE.jpg

# Add the date caption
convert /home/pi/pics/$DATE.jpg -pointsize 32 -fill red -annotate +700+700 $DATE /home/pi/pics/$DATE.jpg

# Upload the full size image to dropbox
/home/pi/Dropbox-Uploader/dropbox_uploader.sh upload /home/pi/pics/$DATE.jpg $DATE.jpg

# Convert to a smaller version for web display
convert /home/pi/pics/$DATE.jpg -resize 600 /home/pi/pics/fresh.jpg

