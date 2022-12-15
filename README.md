# About MachineLearning
## 선형 회귀(Linear Regression)
특정 음식을 처음 요리하는 사람은 요리를 반복하여 연습하면 할 수록 더 완성도가 높은 음식이 나온다. 어느 정도의 연습이 끝나면,
완성된 음식은 대중적으로 대부분 만족하는 음식에 가까워져 있을 것이다.
이는 수학적으로 생각해보면, 어떤 요인의 수치에 따라 특정 요인의 수치가 영향을 받고있다고 할 수 있다.

선형 회귀 모델은 지도학습 알고리즘으로 주로 수치예측 문제에 사용한다. 독립변수를 이용하여 종속변수를 예측하는 모델이다.
이러한 모델에서는, 오차들의 합이 가장 작은경우가 좋은 모델이라고 한다.<br>

## K-NN Algorithm
분류와 군집화 - 지도학습 And 비지도 학습
* 분류 - 소속집단의 정보를 이미 알고 있는 상태에서 비슷한 집단으로 묶는 방법
* 군집화 - 소속집단의 정보가 없는 상태에서 비슷한 집단으로 묶는 방법

K-NN알고리즘은 특징 공간에 분포하는 데이터에 대하여 k개의 가장 가까운 이웃을 살펴보고 다수결 방식으로 데이터의 레이블을 할당하는 분류방식이다.<br>
이는 단순하고 직관적이며 사전학습이나 특별한 준비 시간이 필요없다는 점이 장점이다.<br>
K평균 알고리즘은 군집의 개수에 따라 데이터를 군집으로 분류하는 알고리즘으로 원리가 단순하고 직관적이며, 성능이 좋은군집화 알고리즘으로 사전에 군집의 개수 k 값을 지정해야 한다.

## 다항회귀/결정트리/SVM
* 다항회귀 - 3차 다항식과 같은 (x+1)^3의 계수를 조정하는 문제로 함수를 찾아 내는 것이다. <br>
-다항회귀는 훈련용 데이터에만 지나치게 맞춰진 과적합으로 훈련때에는 좋은 성능을 보이지만 실제 응용시 오차율이 매우 높아져 잘못 예측되는 경우가 많다.
* 결정트리 - 귀납 추론을 위해 자주 사용되는 실용적인 방법으로 트리구조에서 ROOT > Internal Node > Leaf Node 로 거쳐 배정하는 기능을 수행한다.<br>
-결정트리의 가장 큰 장점은 시각화하고 편하고, 직관적으로 이해가 가능하다는 것이다. 또, 데이터의 스케일에 구애받지 않는다. 각 피처가 개별적으로 처리되어 데이터를 분할하는데 데이터 스케일의 영향을 받지 않으므로, 결정트리에서는 피처 정규화나 표준화 같은 전처리 과정이 필요없다.
주요 단점은 pruning(가지치기)를 사용해도 과대적합되는 경향이 있어 일반화 성능이 좋지 않다는 것이다. 이를 대신해 앙상블 기법을 단일 결정트리의 대안으로 흔히 사용한다.
* SVM - 서포트 벡터 머신을 줄여서 말한다. 딥러닝을 통해 인공지능 분야의 중심으로 떠오르기 전에 각광받헌 학습중의 하나이며, 머신러닝 알고리즘중에서 가장 많이 사용되는 알고리즘중 하나. <br>
-이는 오류 데이터 영향이 적으며, 과적합이 되는 경우가 적다. 신경망보다 사용하기 쉽다. 그러나 학습속도가 느리며, 여러개의 조합테스트가 필요하다.

## MyProject
* 알고리즘의 순서 
1. 얼굴 이미지를 읽어 들여서 그 얼굴 이미지의 특징 데이터를 구한다.  
2. 사람 얼굴 이미지를 읽어 들여 그 사람 얼굴이 아닌 이미지의 특징 데이터를 구한다.
3. 그에 맞는 데이터를 만들어 학습한다.
4. 사람 얼굴이 섞인 사진들에 대해서 학습한 데이터와 비교하여 사람 얼굴의 사진을 걸러낸다.
- 이 프로젝트의 목표는 서포트 벡터 머신을 이용하여 내가 원하는 이미지를 학습시켜 다른이미지와 구분을 하는 것이다.
- 이는 이미지를 학습할 때, 16 x 16의 픽셀로 나누어서 배열에 담는다 그에 맞는 특징을 가지어 이미지를 가시화한다. 하지만 이는 특징 벡터로 사용하기 어려우므로, 16 x 8 = 128 크기의 배열을 이용한다. 이는 1차원 벡터로서 128 x 1의 이미지이며 이를 이용하여 이미지의 특징 벡터로 사용한다.
- 입력값으로 사람 얼굴은 1, 아닌 이미지에는 0의 레이블을 준비하면 이는 배열로서 1과 0 의 값이 각각 나누어져 있다.
- 이는 사람이 아닌 얼굴의 이미지또한 같은 방법으로 분석이 가능하며 테스트 할 사진과 비교 하였을 경우 사람이미지가 맞다면 1의 값을 출력하며 이미지를 보여주는 방식이다.<br>

## 적대적 공격
가장 많이사용되는 공격중 하나, FGSM을 이용하여 MNIST를 속인다.<br>
- 상황에 따라 다양한 공격이 있으며, 그 목표는 다 비슷하게도, 입력 데이터에 아주 작은 차이를 추가하여서 분류를 잘 못 되게 유도를 하는 것이다.<br>
화이트박스 공격과 블랙박스 공격이 있으며, 이에는 화이트박스 공격 내용을 다루었다.<br>
화이트 박스 공격은, 공격자가 타겟 모델에 대한 모든 정보를 알 고 있는 상황에서의 공격을 말하며, 이의 경우에는 공격률이 매우 높다.<br>

현실적으로는 화이트박스공격 보다는 블랙박스 공격이 더 가까우며, 이공격은 앞으로 점차 발전할 것이다.<br>

적대적 공격은 앞으로 발전할 것이며, 여러 분야에서 사용이 될 것이다. 가능하다면, 최악의 범죄가 일어날 수도 있을것이다.<br>
- 자동차 분야 - 도로를 따라 달리는 자율주행 자동차의 센서를 방해하는 공격이 있을수도 있을것이다. 센서에는 사람이 보지못하며 센서에는 혼동을 주는 공격(레이저 등)이 있을 수 있지 않을까 생각한다. 이 센서를 혼동시키게 만들면 자율주행은 무엇이 진짜 도로선인지 헷갈려서 사고를 유발하는 최악의 상황도 일어날 수 있다고 생각한다.<br>
- 음성 분야 - 사람이 듣지 못하는 음성의 입력값을 넣어 오작동/오인식 하게 만들어 혼동을 줄 수 있다고 생각한다.
