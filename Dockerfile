# 베이스 이미지
FROM python:3.13

# 작업 디렉토리 생성
WORKDIR /app

# 의존성 복사 및 설치
COPY requirements.txt .
RUN pip install -r requirements.txt

# 프로젝트 복사
COPY . .

# 포트 노출
EXPOSE 8000

# 서버 실행
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]