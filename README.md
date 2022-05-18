# Object-Detection-with-YOLOv4
With this repostory, we will perform an object recognition project using the YOLOv4 algorithm with our dataset consisting of fruits. 
 We will use Ubuntu 20.04 version for data preparation and testing, We will use Google Colaboratory for training.
 
## Steps
- [x] Preparing Data
- [x] Labeling
- [x] Preparing Files
- [x] Darknet
- [ ] Train
- Complated all prepation steps.

## Requirements
Ubuntu 20.04


## What is YOLO 
YOLO(“You Only Look Once”) is an algorithm that uses neural networks to provide real-time object detection. 

YOLO algorithm is important because of the following reasons:

- Speed: This algorithm improves the speed of detection because it can predict objects in real-time.
- High accuracy: YOLO is a predictive technique that provides accurate results with minimal background errors.
- Learning capabilities: The algorithm has excellent learning capabilities that enable it to learn the representations of objects and apply them in object detection.

YOLO algorithm works using the following three techniques:

1. Residual blocks
2. Bounding box regression
3. Intersection Over Union (IOU) 
 <br>  
 <p align="center">
  <img width="483" height="324" src="https://github.com/aysnrdurak/Object-Detection-with-YOLOv4/blob/main/images/YOLO.png">
</p>

## Preparation Dataset and Data Labeling

I got a fruit dataset from kaggle. You can find the dataset I used [here](https://www.kaggle.com/chrisfilo/fruit-recognition).

IMPORTANT! In yolo you can not use every size photos. You should resize your photos. You can find the resize code [here](https://github.com/aysnrdurak/Object-Detection-with-YOLOv4/blob/main/tiny-useful-codes/resize.py)

### Labeling
From this [link](https://github.com/tzutalin/labelImg), we are installing the LabelImg application, our data labeling tool.

Ubuntu users can directly use my folder [here](https://github.com/aysnrdurak/Object-Detection-with-YOLOv4/tree/main/Labelimg) you should download all files and open the folder.

Find a folder that name is "data" and it include "predefined_classes" file. You should replace the classes there with your own class name. You must be careful about number of claases because they will be classes id and every same claases should has same id. İf you work at different computers you have to add the classes to the file in the same order.

You can find all steps following pictures.

---

<img src="https://github.com/aysnrdurak/Object-Detection-with-YOLOv4/blob/main/images/predefined1.png" width="360"/> <img src="https://github.com/aysnrdurak/Object-Detection-with-YOLOv4/blob/main/images/predefined2.png" width="360"/> 

---

Then you are ready for open the application 

---

<img src="https://github.com/aysnrdurak/Object-Detection-with-YOLOv4/blob/main/images/labell.png" width="360"/> <img src="https://github.com/aysnrdurak/Object-Detection-with-YOLOv4/blob/main/images/label2.png" width="360"/> 

---
<img src="https://github.com/aysnrdurak/Object-Detection-with-YOLOv4/blob/main/images/label4.png" width="360"/> <img src="https://github.com/aysnrdurak/Object-Detection-with-YOLOv4/blob/main/images/label5.png" width="360"/> 

---

We need to create 2 folders and 4 files for preparing datas. You can see that files here:

  <br>  
 <p align="center">
  <img width="600" height="400" src="https://github.com/aysnrdurak/Object-Detection-with-YOLOv4/blob/main/images/preparing_folders.png">
</p>

- data_images: This folder include our all data images and all labels
- data_label: This folder include our all labels
- data_fruit.names: This file contains data classes names (it is same with pre-defined classes)
- fruit.data: This file contains number of classes, paths etc. 
- test.txt and train.txt: These files contain the path of the photos to be used as test and train.
 ### You can find all files [here](https://github.com/aysnrdurak/Object-Detection-with-YOLOv4/tree/main/data_fruit)
 
 ---
 
 Then we need to download and edit darknet files.
 
 1. Create a new folder that name is 'yolov4' in the next step you will download the file to this location.
 2. We have pre-trained yolo models. Instead of starting from scratch, we will start our training by using the weight of these models. We can call this method transfer learning. You can find weights same repostory. We will use [yolov4.conv.137](https://drive.google.com/file/d/1JKF-bdIklxOOVy-2Cr5qdvjgGpmGfcbp/view)
 3. Go to inside darknet file and find 'makefile'. Replace GPU, CUDNN and OPENCV with 1 instead of 0.
 4. Then find cfg > yolov4.cfg and change some values and copy file then paste to darknet folder (you should change the name):
     - subdivision: 8 -> 64
     - width and height: replace with your image size (mine is 640x640)
     - max_batches: number of classes * 2000 (mine is 3*2000 = 6000)
     - steps: 80% of max_batches, 90% of max_batches
     - classes: replace with your number of classes (it has 3 classes value you should change all of them)
     - filters: (classes+5)*3 (three of them)
5. Download this darknet repostory (https://github.com/AlexeyAB/darknet) and paste into darknet folder.
6. Paste your data file into darknet file then convert the file to zip format
7. Upload your zip file into the Google Drive

---

### Train


 
 



    
 

