# Explanation
ImageNet 데이터셋에서 사전에 파라미터를 학습한 VGG-16 모델로 미지의 화상을 분류하는 프로그램을 구현한다.

## ImageNet
ImageNet 데이터셋은 스탠퍼드 대학교에서 인터넷 화상을 수집해 분류한 데이터셋이다.  
파이토치는 ImageNet 데이터 중 ILSVRC2012 데이터셋(클래스 : 1천 개, 학습 데이터 : 120만 장, 검증 데이터 : 5만 장, 테스트 데이터 : 10만장)으로 학습한 다양한 모델을 사용 할 수 있다.

## VGG-16
VGG-16 모델은 2014년 ILSVRC에서 2위를 차지한 합성곱 신경망이다. 옥스퍼드 대학교의 VGG팀이 16층으로 구성한 모델이라 VGG-16이라고 불린다.

# How to Data Install
```
# learn-while-making-pytorch 파일에서 실행합니다.
% git clone https://github.com/YutaroOgawa/pytorch_advanced.git
% ipython3 pytorch_advanced/1_image_classification/make_folders_and_data_downloads.ipynb
% cp pytorch_advanced/1_image_classification/data/goldenretriever-3724972_640.jpg VGG/data/
% cp -r data/ VGG/data/ && rm -rf data
```

# Reference
[저자의 깃허브](https://github.com/YutaroOgawa/pytorch_advanced) </br>
[코드](https://www.hanbit.co.kr/src/10460)