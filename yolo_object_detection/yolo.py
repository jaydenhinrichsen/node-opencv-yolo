import cv2 
import numpy as np
import sys
import imutils
import os

# Args
input_path = sys.argv[1]
output_path = sys.argv[2]
cwd = os.path.dirname(os.path.realpath(__file__)) + "\\"

WEIGHTS_FILE = cwd + "yolov3.weights"
CONFIG_FILE = cwd + "yolov3.cfg"
CLASSES_FILE = cwd + "coco.names"

net = cv2.dnn.readNet(WEIGHTS_FILE,CONFIG_FILE)
classes = []
with open(CLASSES_FILE,"r") as f:
    classes = [line.strip() for line in f.readlines()]

colors= np.random.uniform(0,255,size=(len(classes),3))
layer_names = net.getLayerNames()
outputlayers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]


img = cv2.imread(input_path)
height,width,channels = img.shape
blob = cv2.dnn.blobFromImage(img,0.00392,(416,416),(0,0,0),True,crop=False)
net.setInput(blob)
outs = net.forward(outputlayers)
class_ids=[]
confidences=[]
boxes=[]
for out in outs:
    for detection in out:
        scores = detection[5:]
        class_id = np.argmax(scores)
        confidence = scores[class_id]
        if confidence > 0.5:
            center_x= int(detection[0]*width)
            center_y= int(detection[1]*height)
            w = int(detection[2]*width)
            h = int(detection[3]*height)

            
            x=int(center_x - w/2)
            y=int(center_y - h/2)

            boxes.append([x,y,w,h]) 
            confidences.append(float(confidence))
            class_ids.append(class_id) 

indexes = cv2.dnn.NMSBoxes(boxes,confidences,0.4,0.6)


font = cv2.FONT_HERSHEY_PLAIN
for i in range(len(boxes)):
    if i in indexes:
        x,y,w,h = boxes[i]
        label = str(classes[class_ids[i]])
        color = colors[i]
        cv2.rectangle(img,(x,y),(x+w,y+h),color,2)
        cv2.putText(img,label,(x,y+30),cv2.FONT_HERSHEY_SIMPLEX, 1,color,1,cv2.LINE_AA)

cv2.imwrite(output_path,img)

print(output_path)
sys.stdout.flush()