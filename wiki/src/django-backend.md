# Django Backend

현재 백엔드는 Django REST Framework 기반의 블로그 API 예제 구조입니다.

이 문서는 `backend/`에 생성된 실제 코드를 기준으로, 프로젝트 구조와 실행 흐름을 빠르게 파악하기 위한 사전 문서입니다.

## Directory Structure

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

## Project Package

`config/`는 Django 설정 패키지입니다.

- `settings.py`: 설치 앱, 미들웨어, DB, CORS, DRF, Swagger schema 설정
- `urls.py`: admin, schema 문서, API URL 연결
- `asgi.py`: ASGI 서버 진입점
- `wsgi.py`: WSGI 서버 진입점

컨테이너 내부 작업 디렉터리는 `/app`이고, Django 설정 패키지는 `config`입니다. `/app/app`처럼 이름이 겹치지 않도록 설정 패키지 이름은 `config`를 사용합니다.

## Installed Apps

현재 `INSTALLED_APPS`에는 다음 주요 앱이 포함됩니다.

- `corsheaders`
- `rest_framework`
- `drf_spectacular`
- `api`

`DJANGO_SETTINGS_MODULE`은 `config.settings`를 사용합니다.

## API App

`api/`는 블로그 게시글 API를 담당합니다.

### Model

`Post` 모델 필드:

- `title`: 게시글 제목
- `content`: 게시글 내용
- `is_active`: 활성 상태
- `created_at`: 생성 시간
- `updated_at`: 수정 시간

### Serializer

`PostSerializers`는 `Post` 모델의 요청/응답 직렬화를 담당합니다.

읽기 전용 필드:

- `id`
- `created_at`
- `updated_at`

### Views

- `root`: 헬스 체크 성격의 루트 응답
- `BlogViewSet`: 게시글 CRUD API

### URLs

현재 API 라우팅:

```text
GET    /
GET    /blog/
POST   /blog/
GET    /blog/{id}/
PUT    /blog/{id}/
DELETE /blog/{id}/
```

Schema 문서:

```text
/api/schema/
/api/schema/swagger-ui/
/api/schema/redoc/
```

## Docker Development

개발 실행은 루트의 `docker-compose.yml`에서 관리합니다.

```text
./backend -> /app
```

로컬 `backend/`가 컨테이너 `/app`에 bind mount되므로 코드 변경이 개발 서버에 즉시 반영됩니다.

실행:

```powershell
docker compose up --build
```

중지:

```powershell
docker compose down
```

## Dependency Policy

Python 의존성은 `backend/requirements.txt`에서 관리합니다.

현재 주요 의존성:

- Django
- djangorestframework
- drf-spectacular
- django-cors-headers
- gunicorn
- mysqlclient

환경 변수는 Docker compose의 `environment`로 주입하며, `python-dotenv`는 사용하지 않습니다.

## Notes

- 로컬 SQLite 파일 `db.sqlite3`는 개발 산출물이므로 Git에 포함하지 않습니다.
- 개인 IDE 설정인 `.vscode/`는 기본적으로 커밋하지 않습니다.
- `__init__.py`는 wiki의 Python style 기준상 header/footer를 생략할 수 있습니다.
