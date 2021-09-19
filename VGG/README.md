# Explanation
ImageNet 데이터셋에서 사전에 파라미터를 학습한 VGG-16 모델로 미지의 화상을 분류하는 프로그램을 구현한다.

## ImageNet
ImageNet 데이터셋은 스탠퍼드 대학교에서 인터넷 화상을 수집해 분류한 데이터셋이다.  
파이토치는 ImageNet 데이터 중 ILSVRC2012 데이터셋(클래스 : 1천 개, 학습 데이터 : 120만 장, 검증 데이터 : 5만 장, 테스트 데이터 : 10만장)으로 학습한 다양한 모델을 사용 할 수 있다.

### How to Data Install
```
# learn-while-making-pytorch 파일에서 실행합니다.
% git clone https://github.com/YutaroOgawa/pytorch_advanced.git
% ipython3 pytorch_advanced/1_image_classification/make_folders_and_data_downloads.ipynb
% cp pytorch_advanced/1_image_classification/data/goldenretriever-3724972_640.jpg VGG/data/
% cp -r data/ VGG/data/ && rm -rf data
```

## VGG-16
VGG-16 모델은 2014년 ILSVRC에서 2위를 차지한 합성곱 신경망입니다.  
옥스퍼드 대학교의 VGG팀이 16층으로 구성한 모델이라 VGG-16이라고 불립니다.  
</br>
모델을 불러와 출력 결과를 보면 모델의 네트워크 구성은 features와 classifier 두 모듈로 나누어져 있습니다.</br>
그리고 각 모듈 속에 합성곱 층과 전결합 층이 있다. 활성화 함수 ReLu, 풀링 층, 드롭 아웃 층은 포함하지 않습니다.</br>
입력 화상의 크기는, RGB 색상채널 3, 높이와 너비가 224 픽셀이므로 (batch_num, 3, 224, 224)가 됩니다.</br>
입력 화상은 처음에 3X3 크기의 합성곱 필터(64채널), 활성화 함수 ReLU 쌍을 두 번 통과하고, 이후 2X2 크기의 최대 풀링층을 통과합니다.</br>
그렇게 되면 크기는 절반인 112X112가 됩니다. 최종적으로 features의 모듈의 끝에 있는 최대 풀링을 빠져나오면 데이터 크기는 (512, 7, 7)이 됩니다.</br>
</br>
features 모듈을 통과한 후 classifier 모듈에 들어가면 첫번째 전결합층은 입력요소 수가 25088, 출력 수가 4096입니다.</br>
25088이라는 숫자는 classifier 모듈에 대한 화상의 전체 요소 수인 512X7X7=25088로 계산된 것입니다.</br>
전결합 층 이후에는 ReLU, Dropout 층을 통과합니다. </br>
여기에 다시 한 번 전결합 층, ReLU, Dropout 조합을 통과하여 마지막에는 출력 유닛 수가 1,000인 전결합층을 통과합니다.</br>
출력 수 1,000의 출력 유닛은 ImageNet 데이터셋의 클래스 수 1,000 종류에 대응하며, 1,000 클래스 중 입력 화상이 어디에 해당하는지 나타냅니다.</br>
</br>
학습된 VGG-16 모델을 읽은 후에는 VGG-16 화상을 입력하는데 필요한 전처리 부분을 작성합니다.</br>
크기를 224X224로 변경하고 색상정보 RGB를 평균(0.485, 0.456, 0.406), 표준편차 (0.229, 0.224, 0.225)의 조건으로 표준화 합니다.</br>
그 다음 화상의 전처리 클래스를 구현합니다. BaseTransform을 만들어 동장을 확인합니다.</br>
파이토치는 PIL과 화상 요소의 순서가 다릅니다. 파이토치는 (색상 채널, 높이, 너비)순 필로는 (높이, 너비, 색상 채널) 순입니다.</br>
파이토치에서 출력된 텐서의 순서를 `img_transformed = img_transformed.numpy().transpose((1, 2, 0))`으로 교체합니다.

# Reference
[저자의 깃허브](https://github.com/YutaroOgawa/pytorch_advanced) </br>
[코드](https://www.hanbit.co.kr/src/10460)