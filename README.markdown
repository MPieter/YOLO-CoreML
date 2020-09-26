# YOLO with Core ML

This repository is forked from https://github.com/hollance/YOLO-CoreML-MPSNNGraph, which already implemented the implementation for Tiny Yolo v2. I added the full model Yolo v3. Tested on iPhone XS where I got frame rates usually around 20FPS.

When running the application, double tap to switch between Tiny YOLO and YOLOv3.

![YOLO in action](YOLOv3-1.jpg)
![YOLO in action](YOLOv3-2.jpg)

In this repo you'll find:

- **YOLO-CoreML:** A demo app that runs YOLOv3 neural network on Core ML.
- **Convert:** The scripts needed to convert the your Keras model to Core ML

To run the app, just open the **xcodeproj** file in Xcode 9 or later, and run it on a device with iOS 11 or better installed.

The reported "elapsed" time is how long it takes the YOLO neural net to process a single image. The FPS is the actual throughput achieved by the app.

> **NOTE:** Running these kinds of neural networks eats up a lot of battery power. To measure the maximum speed of the model, the `setUpCamera()` method in ViewController.swift configures the camera to run at 240 FPS, if available. In a real app, you'd use at most 30 FPS and possibly limit the number of times per second it runs the neural net to 15 or less (i.e. only process every other frame).

## Converting the models

To start running the application you need to create first the YOLOv3.mlmodel. I didn't include this in the repository due to its file size. It's done in two steps: first you have to convert the YOLOv3 model in darknet format to Keras, then you convert the keras model to CoreML.

### Keras-yolo3

### coreml.py

The **coreml.py** script takes the `yolov3.h5` model created by YAD2K and converts it to `Yolov3.mlmodel`.

Run the `coreml.py` script to do the conversion (the paths to the model file and the output folder are hardcoded in the script):

```
python coreml.py
```
