# node-opencv-yolo
YOLO Object detection with OpenCV and Node.js

## Overview
A simple proof-of-concept for using OpenCV to detect objects in images using Python and Node.js

Here's a demo of the project in action.
![](demo.gif)

## Why
My goal for this project was to create a simple proof-of-concept and to explore object detection/image processing using OpenCV.

In the future, I hope to use what I've learned here to process live video streams from IP cameras. This would allow for a high amount of control over motion events(e.g. only being notified when a person is detected in a frame).

I've faced some challenges with the performance of OpenCV when processing video; likely due to code structure and the fact that it's being run on a CPU, however, I believe I can achieve acceptable performance by utilizing multi-threading.

## Installation & Usage

In order to use this project you'll need to have the following dependencies installed.
- Python 3.7(Your version of python must be accessible from your environment variables)
- opencv-python
- numpy
- yolov3.weights file

[**Here's a link to download the yolov3 pretrained model weights**](https://pjreddie.com/media/files/yolov3.weights)

Run the following to install the NPM packages:
```
npm install
```

Once you've installed the required dependencies, add some JPEG images to the 'original_images' directory within the project.

Run the following command to start the project:
```
npm start
```
