import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'

from ultralytics import YOLO

#  Load a pretrained YOLOV8n model
model=YOLO('yolov5n.pt')

# colors for object detected
COLORS = [(0, 255, 255), (255, 255, 0), (0, 255, 0), (255, 0, 0)]
GREEN = (0, 255, 0)
RED = (0, 0, 255)
PINK = (147, 20, 255)
ORANGE = (0, 69, 255)

 #Run inference on the sorce
results =model.track(source=0,show=True,tracker="bytetrack.yaml")