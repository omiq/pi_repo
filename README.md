# pi_repo
Raspberry Pi projects

## Install ImageMagick

Conversion is performed using this command line tool:

* sudo apt-get install imagemagick

## Install required modules

If your distro does not include these then they must be installed:

Python 2
* sudo pip install requests
* sudo apt-get install python-pil
* sudo apt-get install python-serial

Python 3
* sudo pip3 install requests
* sudo apt-get install python3-pil
* sudo apt-get install python-serial

## Create directories

* mkdir /home/pi/picam
* chmod +w /home/pi/picam
* mkdir /home/pi/pics
* chmod +w /home/pi/pics


## Install DropBox

* git clone https://github.com/andreafabrizi/Dropbox-Uploader.git

* Get API keys https://www.dropbox.com/developers/apps

* ./dropbox_uploader.sh
 
