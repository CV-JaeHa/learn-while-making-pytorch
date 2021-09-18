# Import Library
import numpy as np
import json
from PIL import Image
import matplotlib.pyplot as plt

import torch
import torchvision
from torchvision import models, transforms

# 파이토치 버전 확인
# print(f"Pytorch Version : {torch.__version__} | Torchvision Version : {torchvision.__version__}")

# Lead VGG-16 Model
use_pretrained = True   # 학습된 파라미터 사용
net = models.vgg16(pretrained=use_pretrained)
net.eval()  # 추론 모드(평가 모드)로 설정

