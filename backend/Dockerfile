# Django REST Framework 백엔드 이미지.
#
# 이 파일은 Python 의존성을 별도 단계에서 빌드하고, 실행 이미지는
# 로컬 Django 개발 서버를 실행하는 데 필요한 구성만 유지합니다.

FROM python:3.12-slim AS build

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

# 컴파일러와 MySQL 클라이언트 헤더는 빌드 단계에만 설치합니다.
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
        default-libmysqlclient-dev \
        pkg-config \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

# 실행 단계로 복사할 수 있는 가상환경을 생성합니다.
RUN python -m venv /opt/venv \
    && /opt/venv/bin/pip install --upgrade pip \
    && /opt/venv/bin/pip install -r requirements.txt


FROM python:3.12-slim AS run

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/opt/venv/bin:$PATH"

WORKDIR /app

# 실행 단계에는 컴파일 도구를 설치하지 않고 필요한 런타임 라이브러리만 둡니다.
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        libmariadb3 \
    && rm -rf /var/lib/apt/lists/*

# 빌드 단계에서 설치한 Python 패키지를 복사한 뒤 애플리케이션 코드를 복사합니다.
COPY --from=build /opt/venv /opt/venv
COPY . .

# 로컬 /app 마운트에 가려지지 않도록 entrypoint는 시스템 경로에 둡니다.
COPY docker/entrypoint.sh /usr/local/bin/backend-entrypoint.sh
RUN chmod +x /usr/local/bin/backend-entrypoint.sh

EXPOSE 8000

ENTRYPOINT ["backend-entrypoint.sh"]

# File History
# 2026-04-29: Django REST Framework 백엔드용 멀티스테이지 Dockerfile을 생성했습니다.
# 2026-04-29: 개발 실행 명령은 compose에서 관리하도록 기본 CMD를 제거했습니다.
# 2026-04-29: python 버전을 3.12로 변환
# 2026-04-29: Django 프로젝트 생성 책임을 Dockerfile에서 제거했습니다.
# 2026-04-29: config 설정 패키지를 생성하는 개발 entrypoint를 연결했습니다.
