# Headpose Detection
---
### Referenced Code
* https://www.learnopencv.com/head-pose-estimation-using-opencv-and-dlib
* https://www.pyimagesearch.com/2017/04/03/facial-landmarks-dlib-opencv-python
* https://github.com/lincolnhard/head-pose-estimation
* https://www.pyimagesearch.com/2015/12/28/increasing-raspberry-pi-fps-with-python-and-opencv/

### Requirements
* Python 3.6
  * dlib
  * opencv-python
  * numpy

Please check Dockerfile for more information.

### Setup
* `./setup.sh`

### Usage
* Headpose detection for images
  * `python3 hpd.py -i <input_dir> -o <output_dir>`
* Headpose detection for videos
  * `python3 videoCapture.py -i <input_video> -o <output_file>`
* Headpose detection for webcam
  * `python3 videoCapture.py -d 1`
---
