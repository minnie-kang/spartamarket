# 스파르타 마켓 (Sparta Market)

## 프로잭트 소개

스파르타 마켓은 Django 기반의 온라인 중고거래 플랫폼입니다.

## 주요 기능

- 사용자 인증 (회원가입/로그인)
- 제품 등록 및 관리(상세설명, 이미지 업로드)
- 제품 찜하기 및 해시태그 기능

### 필요 조건

- Python 3.10 이상
- Django 4.2

## 기술 스택

- Backend: Django 4.2
- Database: SQLite3
- 이미지 처리: Django ImageField

## 프로젝트 구조

spartamarket
├── accounts/ # 사용자 로그인 관련 앱
├── products/ # 제품 관리 관련 앱
├── static/ # 정적 파일 (CSS, JS, 이미지)
├── media/ # 사용자 업로드 파일
├── templates/ # HTML 템플릿
└── spartamarket/ # 프로젝트 설정
    ├── settings.py # 프로젝트 설정 파일
    └── urls.py # 메인 URL 설정


## 개발 환경 설정

- DEBUG = True (개발 환경)
- SQLite3 데이터베이스 사용
- Django 기본 인증 시스템 사용
- 커스텀 User 모델 사용 (AUTH_USER_MODEL = 'accounts.User')

## 실행 방법
### 1. 가상환경 생성 및 활성화
python -m venv venv
venv\Scripts\activate

### 2. 필요한 패키지 설치
pip install -r requirements.txt

### 3. 데이터베이스 마이그레이션
python manage.py makemigrations
python manage.py migrate

### 4. 서버 실행
python manage.py runserver
