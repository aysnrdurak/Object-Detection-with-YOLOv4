# Object-Detection-with-YOLOv4
With this repostory, we will perform an object recognition project using the YOLOv4 algorithm with our dataset consisting of fruits. 
 We will use Ubuntu 20.04 version for data preparation and testing, We will use Google Colaboratory for training.
 
## Steps
- [x] Preparing Data
- [x] Labeling
- [ ] 
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

### Labeling
From this [link](https://github.com/tzutalin/labelImg), we are installing the LabelImg application, our data labeling tool.

Ubuntu users can directly use my folder [here](https://github.com/aysnrdurak/Object-Detection-with-YOLOv4/tree/main/Labelimg) you should download all files and open the folder.

Find a folder that name is "data" and it include "predefined_classes" file. You should replace the classes there with your own class name. You must be careful about number of claases because they will be classes id and every same claases should has same id. İf you work at different computers you have to add the classes to the file in the same order.

---

<img src="https://github.com/aysnrdurak/Object-Detection-with-YOLOv4/blob/main/images/predefined1.png" width="480"/> <img src="https://github.com/aysnrdurak/Object-Detection-with-YOLOv4/blob/main/images/predefined2.png" width="480"/> 

---

Then you are ready for open the application 

---

<img src="https://github.com/aysnrdurak/Object-Detection-with-YOLOv4/blob/main/images/label1.png" width="480"/> <img src="https://github.com/aysnrdurak/Object-Detection-with-YOLOv4/blob/main/images/label2.png" width="480"/> 


    
 

