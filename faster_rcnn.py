# -*- coding: utf-8 -*-
"""Faster_RCNN.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1wns_QCWNRmHpRw_5X5NMzU3_3tixmYVC
"""

!pip install torchvision

import torch
import torchvision

print(torch.__version__)
print(torchvision.__version__)

from torchvision import transforms as T

from PIL import Image
import cv2
from google.colab.patches import  cv2_imshow

model = torchvision.models.detection.fasterrcnn_resnet50_fpn(pretrained = True)

model.eval()

!wget '/content/8017130856_1b46b5f5fc_z.jpg'

Ig = Image.open("/content/8017130856_1b46b5f5fc_z.jpg")

transform = T.ToTensor() #T.ToTensor() fonksiyonu, bir görüntüyü NumPy dizisinden PyTorch tensoruna dönüştürmek için kullanılır

img = transform(Ig)

with torch.no_grad():
  pred = model([img])

pred[0].keys()

boxes , labels ,scores = pred[0]["boxes"] , pred[0]["labels"] , pred[0]["scores"]

scores

num = torch.argwhere(scores > 0.9).shape[0]

coco_names = ["person" , "bicycle" , "car" , "motorcycle" , "airplane" , "bus" , "train" , "truck" , "boat" , "traffic light" , "fire hydrant" , "street sign" , "stop sign" , "parking meter" , "bench" , "bird" , "cat" , "dog" , "horse" , "sheep" , "cow" , "elephant" , "bear" , "zebra" , "giraffe" , "hat" , "backpack" , "umbrella" , "shoe" , "eye glasses" , "handbag" , "tie" , "suitcase" ,
"frisbee" , "skis" , "snowboard" , "sports ball" , "kite" , "baseball bat" ,
"baseball glove" , "skateboard" , "surfboard" , "tennis racket" , "bottle" ,
"plate" , "wine glass" , "cup" , "fork" , "knife" , "spoon" , "bowl" ,
"banana" , "apple" , "sandwich" , "orange" , "broccoli" , "carrot" , "hot dog" ,
"pizza" , "donut" , "cake" , "chair" , "couch" , "potted plant" , "bed" ,
"mirror" , "dining table" , "window" , "desk" , "toilet" , "door" , "tv" ,
"laptop" , "mouse" , "remote" , "keyboard" , "cell phone" , "microwave" ,
"oven" , "toaster" , "sink" , "refrigerator" , "blender" , "book" ,
"clock" , "vase" , "scissors" , "teddy bear" , "hair drier" , "toothbrush" , "hair brush"]

igg = cv2.imread("/content/8017130856_1b46b5f5fc_z.jpg")
for i in range(num):
  x1 , y1 , x2 ,y2 = boxes[i].numpy().astype("int")
  class_name = coco_names[labels.numpy()[i] - 1]
  igg = cv2.rectangle(igg , (x1,y1) , (x2,y2),(0,255,0),1)
  igg = cv2.putText(igg, class_name, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1, cv2.LINE_AA)

boxes

cv2_imshow(igg)