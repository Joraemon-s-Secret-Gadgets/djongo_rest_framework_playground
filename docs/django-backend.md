# Django Backend 사전 문서

이 문서는 현재 `backend/` 코드 기준으로 Django REST Framework 백엔드 구조를 정리합니다.

## 현재 구조

```text
backend/
  manage.py
  config/
    settings.py
    urls.py
    asgi.py
    wsgi.py
  api/
    models.py
    serializers.py
    views.py
    urls.py
    tests.py
    migrations/
  docker/
    entrypoint.sh
  Dockerfile
  requirements.txt
```

## 설정 패키지

`config/`는 Django 프로젝트 설정 패키지입니다.

- `config.settings`: Django 설정 모듈
- `config.urls`: 프로젝트 최상위 URL 라우팅
- `config.asgi`: ASGI 진입점
- `config.wsgi`: WSGI 진입점

`docker-compose.yml`에서도 `DJANGO_SETTINGS_MODULE=config.settings`를 명시합니다.

## API 구성

`api/` 앱은 블로그 게시글 API를 제공합니다.

`Post` 모델:

- `title`
- `content`
- `is_active`
- `created_at`
- `updated_at`

라우트:

```text
/                  루트 상태 응답
/blog/             게시글 목록 조회, 생성
/blog/{id}/        게시글 단건 조회, 수정, 삭제
/api/schema/       OpenAPI schema
/api/schema/swagger-ui/
/api/schema/redoc/
```

## 개발 실행

루트에서 실행합니다.

```powershell
docker compose up --build
```

컨테이너는 로컬 `backend/`를 `/app`에 마운트합니다.

```text
./backend:/app
```

Django `runserver`는 기본적으로 파일 변경을 감지해 자동 reload합니다.

## 의존성

`backend/requirements.txt`에서 관리합니다.

- Django
- djangorestframework
- drf-spectacular
- django-cors-headers
- gunicorn
- mysqlclient

`python-dotenv`는 사용하지 않고 Docker compose 환경 변수 주입을 사용합니다.

## 관리 기준

- Django 설정 패키지는 `config`로 유지합니다.
- 실제 기능 앱은 `api`, `users`, `blog`처럼 별도 앱으로 분리합니다.
- 로컬 개발 산출물인 `db.sqlite3`, 캐시, `.vscode/`는 커밋하지 않습니다.
