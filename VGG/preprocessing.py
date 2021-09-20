# Import Library
import numpy as np
import json
from PIL import Image
import matplotlib.pyplot as plt

import torch
import torchvision
from torchvision import models, transforms

# Import File
import read_model as md


# 입력 화상의 전처리 클래스
class BaseTransform():
    """
    Attributes
    ----------
    resize : int
        크기 변경 전의 화상 크기
    mean : (R, G, B)
        각 색상 채널의 평균 값
    std : (R, G, B)
        각 색상 채널의 표준 편차
    """
    def __init__(self, resize, mean, std):
        self.base_transform = transforms.Compose([
            transforms.Resize(resize),      # 짧은 변의 길이가 resize 크기가 된다.
            transforms.CenterCrop(resize),  # 화상 중앙을 resize x resize로 자른다.
            transforms.ToTensor(),          # 토치 텐서로 변환
            transforms.Normalize(mean, std) # 색상 정보의 표준화
        ])

    def __call__(self, img):
        return self.base_transform(img)


# 화상 전처리 확인

## 1. 화상 읽기
image_file_path = './data/goldenretriever-3724972_640.jpg'
img = Image.open(image_file_path)   # [높이[너비][색RGB]

## 2. 원본 화상 표시
plt.imshow(img)
plt.show()

## 3. 화상 전처리 및 처리된 화상의 표시
resize = 224
mean = (0.485, 0.456, 0.406)
std = (0.229, 0.224, 0.225)
transform = BaseTransform(resize, mean, std)
img_transformed = transform(img)    # torch.Size([3, 224, 224])

## (색상, 높이, 너비)를 (높이, 너비, 색상)으로 변환하고 0~1로 값을 제한하여 표시
img_transformed = img_transformed.numpy().transpose((1, 2, 0))
img_transformed = np.clip(img_transformed, 0, 1)

plt.imshow(img_transformed)
plt.show()