# 코로나19 바이러스로 인한 사망자 수 예측 프로그램

### 서비스 설명

본 서비스는 코로나 라이브(https://corona-live.com) 사이트에서 지역별 확진자 수, 총 확진자. 총 사망자 수의 데이터를 크롤링 하였다. 입력받은 데이터들을 그룹화 한 후 그래프로 시각화하여 나타내었다. 또한 총 확진자 수와 총 사망자수의 데이터를 이용하여 모델을 학습한 후, 확진자 수에 대하여 사망자 수를 예측하는 머신러닝을 구축하였다.

## 설치방법

 - 용량이 큰 파일은 git에 올리지 않았다.

웹 데이터 크롤링
 ```
 pip install selenium
 pip install request
 pip install wevdriver_manager.chrome
 pip install BeatifulSoup
 ```
데이터 시각화
 ```
 pip install pandas
 pip install matplotlib
 pip install numpy
 ```
model 설치
 ```
 pip install sklearn
 pip install pandas
 pip install numpy
 ```
