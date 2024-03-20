# 인공지능을 활용한 유통관리 시스템

Distribution_Management_System_Using_AI

## 개요

- 프로젝트 명 : 인공지능을 활용한 유통관리 시스템
- 프로젝트 기간 : 2022.09 ~ 2023.06
- 개발 언어 : Python, PyTorch
- 팀원 : 최재용, 김수현, 이우영, 안정현

## 프로젝트 설명

YOLO v5를 기반으로 한 객체 탐지 기술을 활용하여 제품의 유통기한 (혹은 소비기한) 및 바코드와 관련된 정보를 추출하여 자동화된 유통관리 시스템을 구축하는 방법을 구현. 구현한 시스템은 여러 제품의 유통기한 (소비기한)과 제품정보를 실시간으로 파악하고, 해당 제품의 입고 및 출고를 자동으로 제어함으로써 유통관리의 자동화를 실현

## 주요역할

- 유통기한 crop을 위한 객체탐지 모델 훈련 및 성능 향상
- 제품 제어를 위한 로봇팔을 서버를 통한 소켓 통신 기능 구현
- 모터, 로봇팔 하드웨어 제어 코드 구현

## 최종 결과

### Yolo를 이용한 유통기한 부분 추출

<img src="./image/detectionImg.png" style="width:500px;"/>

### 로봇팔 제어를 통한 재고 관리

<img src="./image/robotImg.jpeg"  style="width:500px;"/>

### 최종결과물

<img src="./image/result.jpeg " style="width:500px;"/>
