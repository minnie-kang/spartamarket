# 스파르타 마켓 (Sparta Market)

## 프로잭트 소개
스파르타 마켓은 Django 기반의 온라인 중고거래 플랫폼입니다.

## 주요 기능
- 사용자 인증 (회원가입/로그인)
- 제품 등록 및 관리(상세설명, 이미지 업로드)
- 제품 찜하기 및 해시태그 기능

### 필요 조건
Python 3.10 이상
Django 4.2

## 기술 스택
- Backend: Django 4.2
- Database: SQLite3
- 이미지 처리: Django ImageField

## 프로젝트 구조

spartamarket
├── accounts/ # 사용자 로그인 관련 앱앱
├── products/ # 제품 관리 관련 앱
├── static/ # 정적 파일 (CSS, JS, 이미지)
├── media/ # 사용자 업로드 파일
├── templates/ # HTML 템플릿
└── spartamarket/ # 프로젝트 설정
├── settings.py # 프로젝트 설정 파일
├── urls.py # 메인 URL 설정
├── wsgi.py
└── asgi.py


## 환경 설정
- 언어 설정: 한국어 (ko-kr)
- 시간대: Asia/Seoul
- 정적 파일 설정: STATIC_URL = "static/"
- 미디어 파일 설정: MEDIA_URL = '/media/'

## 개발 환경 설정
- DEBUG = True (개발 환경)
- SQLite3 데이터베이스 사용
- Django 기본 인증 시스템 사용
- 커스텀 User 모델 사용 (AUTH_USER_MODEL = 'accounts.User')


## 실행 방법
#### 가상 환경 설정

1. 먼저 vscode의 터미널이나 cmd 환경에서 아래 문장 입력

```python -m venv [가상환경이름]```  


2. 가상환경에 접속

```[가상환경명]\Scripts\activate```   


3. [requirements.txt](./requirement.txt) 활용하여 패키지 설치

```pip install -r requirements.txt```  


#### Django 앱 실행

```python manage.py runserver ``` 입력하여 Django 앱 실행
