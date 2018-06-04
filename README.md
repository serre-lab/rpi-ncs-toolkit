# rpi-ncs-toolkit

This is a nice tutorial that steps through the process of installing the Neural Compute Stick (NCS) SDK in <b>API-only</b> mode 
(note that this is important as the Pi CPU/Memory is underpowered for the full installation). <a href="https://www.pyimagesearch.com/2018/02/12/getting-started-with-the-intel-movidius-neural-compute-stick/"> Installation Tutorial </a>

Dependencies:
1. Raspberry Pi 3b <b>only</b>
2. Raspbian Stetch OS: You can find the desktop image here <a href="https://www.raspberrypi.org/downloads/raspbian/"> Stretch OS </a> and the instructions to flash the SD card <a href="https://www.raspberrypi.org/documentation/installation/installing-images/README.md"> here </a>

Usage: <br>
Get a live feed from the camera for 30 seconds
<pre>python camera_preview.py</pre>

Record a video from the PiCamera in .h264 format. By default the recording duration is for 2 minutes @30FPS and a resolution of 1080p
<pre>python camera.py</pre>
