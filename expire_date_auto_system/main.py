import torch
import numpy as np

from GUI import openGUI

# dummy_data(image_random)
# 첫 번째 실행에 더미데이터 넣으며 다음 detection부터 실행시간 단축
model = torch.hub.load('ultralytics/yolov5', 'custom', path='expire_date.pt')  # custom trained model
results = model(np.random.randint(0, 255, (600, 600, 3), dtype=np.uint8))

if __name__ == '__main__':
    openGUI()