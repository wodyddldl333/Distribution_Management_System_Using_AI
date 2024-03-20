# yolo_module.py
import cv2
import torch
import shutil
import os
from glob import glob

from image_module import image_make


def detect_expiry_date():
    file = image_make()
    model = torch.hub.load('ultralytics/yolov5', 'custom', path='expire_date.pt')  # custom trained model
    results = model(file)
    results.crop()
    results.save()
    if os.path.isdir('runs/detect/exp2'):
        detect_image_path = glob('runs/detect/exp2/*.jpg')
    detect_image = cv2.imread(detect_image_path[0])
    cv2.imshow('', cv2.resize(detect_image, dsize=(0, 0), fx=0.3, fy=0.3, interpolation=cv2.INTER_LINEAR))
    while True:
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
    shutil.rmtree('runs/detect/exp2')