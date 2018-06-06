# rpi-ncs-toolkit

With this project, we ship the disk image of a fully functional Pi OS running Raspbian Stretch on a Pi3B+, with Movidius and PiCamera related libraries, demos etc. The image can be downloaded <a href=" "> here </a>. Please follow <a href="https://thepihut.com/blogs/raspberry-pi-tutorials/17789160-backing-up-and-restoring-your-raspberry-pis-sd-card"> these </a> instructions to clone this on to your microSD card. <br>

This is a nice tutorial that steps through the process of installing the Neural Compute Stick (NCS) SDK in <b>API-only</b> mode 
(note that this is important as the Pi CPU/Memory is underpowered for the full installation). <a href="https://www.pyimagesearch.com/2018/02/12/getting-started-with-the-intel-movidius-neural-compute-stick/"> Installation Tutorial </a>. This also has installation instructions for other key libraries such as OpenCV, libusb etc.

Dependencies:
1. Raspberry Pi 3b or 3b+ <b>only</b>
2. Raspbian Stretch OS: You can find the desktop image here <a href="https://www.raspberrypi.org/downloads/raspbian/"> Stretch OS </a> and the instructions to flash the SD card <a href="https://www.raspberrypi.org/documentation/installation/installing-images/README.md"> here </a>
3. To use a full SDK on a linux machine, you would need Ubuntu 16.04! Follow these instructions to install:
<pre>
mkdir -p ~/workspace
cd ~/workspace
git clone https://github.com/movidius/ncsdk.git
cd ~/workspace/ncsdk
make install
make examples
</pre>

Usage: <br>
Get a live feed from the camera for 60 seconds
<pre>python camera_preview.py</pre>

Record a video from the PiCamera in .h264 format. By default the recording duration is for 2 minutes @30FPS and a resolution of 1080p
<pre>python camera.py</pre>

Example projects <br>
<pre>
# Zebrafish detector using a SSD MobileNet Implementation
cd ~/rpi-ncs-tooolkit/ssdmobilenet
python run.py

# Face Detector live demo
# Note that this implementation requires two neural sticks
cd ~/rpi-ncs-toolkit/mtcnn
python live_demo.py

# Age Detector live demo
cd ~/rpi-ncs-tooolkit/gender_age
python live_demo.py
</pre>
