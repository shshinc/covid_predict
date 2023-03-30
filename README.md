# 코로나19 확진자 수에 대한 사망자 수 예측

### 서비스 설명

본 서비스는 코로나 라이브(https://corona-live.com) 사이트에서 지역별 확진자 수, 총 확진자. 총 사망자 수의 데이터를 크롤링 하였다. 입력받은 데이터들을 그룹화 한 후 그래프로 시각화하여 나타내었다. 또한 총 확진자 수와 총 사망자수의 데이터를 이용하여 모델을 학습한 후, 확진자 수에 대하여 사망자 수를 예측하는 머신러닝을 구축하였다.

### 설치방법

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

### 의존성

for 웹 데이터 크롤링
 ```
 selenium==3.8.1
 requests==2.28.1
 ChromeDriver
 ```
 
for 데이터 시각화
 ```
 matplotlib==1.5.1
 pandas==1.3.3
 numpy==1.23.5
 ```
 
for model
 ```
 python==3.x
 numpy==1.23.5
 sklearn==1.2.2
 pandas==1.3.3
 ```
 
### Autor
 - SuHwan-Shin, shshinc77@gmail.com, ChungBuk National Univ(Undergraduate).
