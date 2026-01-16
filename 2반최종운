# Python 학습 저장소

Python 기초부터 실전 프로젝트까지 학습 과정을 기록한 저장소

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Firebase](https://img.shields.io/badge/Firebase-FFCA28?style=flat&logo=Firebase&logoColor=black)

## 📌 프로젝트 개요

이 저장소는 Python 프로그래밍 학습 과정에서 작성한 다양한 실습 코드와 프로젝트를 포함하고 있습니다. 기초 문법부터 데이터 처리, 그래픽 프로그래밍, 데이터베이스 연동까지 다양한 주제를 다룹니다.

## 📂 프로젝트 구조

```
Python/
├── firebase/                  # Firebase 실시간 데이터베이스 연동
├── input,turtle,last/         # 사용자 입력 & Turtle 그래픽
├── json,csv/                  # JSON, CSV 파일 처리
├── pickle,re/                 # Pickle 직렬화 & 정규표현식
├── pickle/                    # Pickle 심화
├── turtle,bmi,plus/           # Turtle 그래픽 & BMI 계산기
├── turtle,input/              # Turtle 그래픽 & 입력 처리
└── 2반최종운                   # 최종 프로젝트: 주소록 관리 프로그램
```

## 🎯 학습 주제

### 1. 기초 문법
- 변수와 자료형
- 조건문 (if, elif, else)
- 반복문 (for, while)
- 함수 정의와 호출
- 사용자 입력 처리 (input)

### 2. 자료구조
- 리스트 (List)
- 튜플 (Tuple)
- 딕셔너리 (Dictionary)
- 집합 (Set)

### 3. 파일 처리
- 파일 읽기/쓰기
- JSON 데이터 처리
- CSV 파일 다루기
- Pickle 직렬화

### 4. 정규표현식
- 패턴 매칭
- 텍스트 검색 및 치환
- 데이터 검증

### 5. 그래픽 프로그래밍
- Turtle Graphics
- 도형 그리기
- 애니메이션

### 6. 데이터베이스
- Firebase 연동
- 실시간 데이터베이스
- CRUD 작업

## 🚀 주요 프로젝트

### 1. 주소록 관리 프로그램 (최종 프로젝트)

**파일**: `2반최종운`

**기능:**
- ✅ 연락처 추가 (이름, 전화번호, 주소)
- ✅ 연락처 삭제
- ✅ 연락처 검색
- ✅ 전체 연락처 출력
- ✅ 파일 저장/불러오기 (Pickle)

**실행 방법:**
```bash
python 2반최종운
```

**사용 예시:**
```
1. 연락처 추가
2. 연락처 삭제
3. 연락처 검색
4. 연락처 출력
5. 연락처 파일 저장
6. 파일 불러 오기
7. 종료
메뉴 항목을 선택하시오: 1

이름: 홍길동
전화번호: 010-1234-5678
주소: 서울시 강남구
```

**주요 코드:**
```python
import pickle

def main():
   address_book = {}
   while True:
       user = display_menu()
       
       if user == 1:
          name, number, addr = get_contact()
          address_book[name] = [number, addr]
          
       elif user == 5:  # 저장
           with open("./addressData.bin", "wb") as f:
               pickle.dump(address_book, f)
               
       elif user == 6:  # 불러오기
           with open("./addressData.bin", "rb") as f:
               address_book = pickle.load(f)
```

**사용 기술:**
- Dictionary를 활용한 데이터 관리
- Pickle을 이용한 영구 저장
- 메뉴 기반 CLI 인터페이스

---

### 2. BMI 계산기

**폴더**: `turtle,bmi,plus/`

**기능:**
- 키와 몸무게 입력
- BMI 지수 계산
- 비만도 판정

**BMI 계산 공식:**
```
BMI = 몸무게(kg) / (키(m) ** 2)
```

---

### 3. Turtle Graphics

**폴더**: `turtle,input/`, `input,turtle,last/`

**학습 내용:**
- 기본 도형 그리기
- 색상 및 패턴
- 사용자 입력 기반 그래픽
- 애니메이션

**예제 코드:**
```python
import turtle

t = turtle.Turtle()
t.shape("turtle")

# 정사각형 그리기
for i in range(4):
    t.forward(100)
    t.right(90)

turtle.done()
```

---

### 4. 데이터 처리

#### JSON 처리
**폴더**: `json,csv/`

```python
import json

# JSON 파일 읽기
with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# JSON 파일 쓰기
with open("output.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
```

#### CSV 처리
```python
import csv

# CSV 파일 읽기
with open("data.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
```

---

### 5. Firebase 연동

**폴더**: `firebase/`

**기능:**
- Firebase Realtime Database 연결
- 데이터 읽기/쓰기
- 실시간 동기화

**예제 코드:**
```python
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Firebase 초기화
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://your-project.firebaseio.com/'
})

# 데이터 쓰기
ref = db.reference('users')
ref.set({
    'user1': {
        'name': '홍길동',
        'age': 25
    }
})

# 데이터 읽기
print(ref.get())
```

---

### 6. Pickle 직렬화

**폴더**: `pickle/`, `pickle,re/`

**학습 내용:**
- 객체 직렬화/역직렬화
- 파일로 저장
- 데이터 영구 보관

**예제:**
```python
import pickle

# 데이터 저장
data = {'name': '홍길동', 'age': 25, 'city': '서울'}
with open('data.pkl', 'wb') as f:
    pickle.dump(data, f)

# 데이터 불러오기
with open('data.pkl', 'rb') as f:
    loaded_data = pickle.load(f)
    print(loaded_data)
```

---

### 7. 정규표현식

**폴더**: `pickle,re/`

**학습 내용:**
- 패턴 매칭
- 이메일 검증
- 전화번호 추출
- 텍스트 치환

**예제:**
```python
import re

# 이메일 패턴
email_pattern = r'^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
email = "test@example.com"

if re.match(email_pattern, email):
    print("유효한 이메일입니다.")

# 전화번호 추출
text = "연락처: 010-1234-5678, 02-123-4567"
phone_numbers = re.findall(r'\d{2,3}-\d{3,4}-\d{4}', text)
print(phone_numbers)  # ['010-1234-5678', '02-123-4567']
```

## 💻 개발 환경

- **Python**: 3.x
- **IDE**: PyCharm / VS Code / IDLE
- **주요 라이브러리**:
  - `pickle`: 객체 직렬화
  - `json`: JSON 처리
  - `csv`: CSV 파일 처리
  - `re`: 정규표현식
  - `turtle`: 그래픽
  - `firebase-admin`: Firebase 연동

## 📦 설치 및 실행

### 1. Python 설치
```bash
# Python 3.x 설치 확인
python --version
# 또는
python3 --version
```

### 2. 필요한 라이브러리 설치
```bash
# Firebase 사용 시
pip install firebase-admin

# 기본 라이브러리는 Python에 내장되어 있음
# pickle, json, csv, re, turtle
```

### 3. 프로젝트 클론
```bash
git clone https://github.com/yesgosu/Python.git
cd Python
```

### 4. 실행
```bash
# 주소록 프로그램 실행
python 2반최종운

# 다른 프로젝트 실행
cd turtle,bmi,plus
python bmi.py
```

## 🎓 학습 순서 (권장)

### 초급
1. **기초 문법** (`input,turtle,last/`)
   - 변수, 자료형
   - 조건문, 반복문
   - 함수

2. **Turtle Graphics** (`turtle,input/`)
   - 기본 도형 그리기
   - 사용자 입력 처리

### 중급
3. **자료구조** (`pickle/`)
   - 리스트, 딕셔너리
   - 파일 I/O

4. **데이터 처리** (`json,csv/`)
   - JSON, CSV 다루기
   - 데이터 변환

5. **정규표현식** (`pickle,re/`)
   - 패턴 매칭
   - 텍스트 처리

### 고급
6. **통합 프로젝트** (`2반최종운`)
   - 주소록 관리 프로그램
   - 모든 개념 통합

7. **데이터베이스 연동** (`firebase/`)
   - Firebase 실시간 DB
   - 클라우드 저장

## 📚 학습 자료

### 공식 문서
- [Python 공식 문서](https://docs.python.org/ko/3/)
- [Python Tutorial](https://docs.python.org/ko/3/tutorial/)
- [Firebase Python SDK](https://firebase.google.com/docs/admin/setup)

### 추천 학습 사이트
- [점프 투 파이썬](https://wikidocs.net/book/1)
- [코딩도장](https://dojang.io/course/view.php?id=7)
- [프로그래머스 Python](https://programmers.co.kr/learn/courses/2)

### 연습 문제
- [백준 온라인 저지](https://www.acmicpc.net/)
- [프로그래머스](https://programmers.co.kr/)
- [LeetCode](https://leetcode.com/)

## 🔧 코딩 스타일

### PEP 8 준수
```python
# 좋은 예
def calculate_bmi(weight, height):
    """BMI를 계산하는 함수"""
    bmi = weight / (height ** 2)
    return bmi

# 나쁜 예
def calculateBMI(w,h):
    return w/(h**2)
```

### 주석 작성
```python
# 단일 라인 주석
x = 5  # 변수 설명

"""
여러 줄 주석
(docstring)
"""
```

## 🐛 일반적인 오류 해결

### 1. 인코딩 오류
```python
# 한글 파일 처리 시
with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read()
```

### 2. 모듈 import 오류
```bash
# 모듈 설치
pip install module_name

# 또는
pip3 install module_name
```

### 3. 경로 오류
```python
import os

# 현재 디렉토리 확인
print(os.getcwd())

# 절대 경로 사용
file_path = os.path.join(os.getcwd(), "data.txt")
```

## 📈 향후 학습 계획

### 다음 단계
- [ ] 객체지향 프로그래밍 (OOP)
- [ ] 예외 처리 (Exception Handling)
- [ ] 모듈과 패키지
- [ ] 웹 스크래핑 (BeautifulSoup, Selenium)
- [ ] 데이터 분석 (Pandas, NumPy)
- [ ] 웹 개발 (Flask, Django)
- [ ] 머신러닝 (Scikit-learn, TensorFlow)

### 프로젝트 아이디어
- [ ] 가계부 프로그램
- [ ] 할일 관리 앱
- [ ] 웹 크롤러
- [ ] 간단한 게임 (Snake, Tetris)
- [ ] 날씨 API 활용 앱
- [ ] 주식 가격 조회 프로그램

## 🤝 기여하기

학습 내용 공유나 개선 사항은 언제나 환영합니다!

### 기여 방법
1. Fork this repository
2. Create feature branch
3. Commit changes
4. Push to branch
5. Open a Pull Request

## 💡 코드 개선 제안

### 주소록 프로그램 개선안
```python
# 현재 코드의 개선 가능한 부분

# 1. 예외 처리 추가
try:
    with open("./addressData.bin", "rb") as f:
        address_book = pickle.load(f)
except FileNotFoundError:
    print("저장된 파일이 없습니다.")
    address_book = {}

# 2. 함수 분리
def save_contacts(contacts):
    """연락처를 파일로 저장"""
    with open("./addressData.bin", "wb") as f:
        pickle.dump(contacts, f)
    print("저장 완료!")

# 3. 데이터 검증
def validate_phone(phone):
    """전화번호 형식 검증"""
    pattern = r'^\d{2,3}-\d{3,4}-\d{4}$'
    return re.match(pattern, phone) is not None
```

## 📝 라이선스

이 프로젝트는 학습 목적으로 작성되었습니다.

## 👨‍💻 개발자

**yesgosu** - [GitHub](https://github.com/yesgosu)

## 📧 문의

학습 관련 질문이나 프로젝트 문의는 GitHub Issues를 이용해주세요.

---

**학습 기간**: 2024-2025년  
**마지막 업데이트**: 2026년 1월

📚 Python으로 프로그래밍의 즐거움을 느껴보세요!
