#!/bin/sh
set -e

# Django REST Framework 개발 컨테이너 시작 스크립트.
#
# 이 파일은 로컬 backend 폴더가 /app에 마운트된 상태에서 manage.py가 없으면
# `django-admin startproject config .` 명령으로 Django 설정 패키지를 생성하고,
# Django REST Framework 개발 설정을 확인한 뒤 전달받은 명령을 실행합니다.

PROJECT_NAME="${DJANGO_PROJECT_NAME:-config}"

if [ ! -f "/app/manage.py" ]; then
    echo "manage.py가 없어 ${PROJECT_NAME} Django 프로젝트를 생성합니다."
    cd /app
    django-admin startproject "${PROJECT_NAME}" .
fi

SETTINGS_PATH=""

for candidate in "${PROJECT_NAME}" config; do
    if [ -f "/app/${candidate}/settings.py" ]; then
        SETTINGS_PATH="/app/${candidate}/settings.py"
        break
    fi
done

if [ -z "${SETTINGS_PATH}" ]; then
    SETTINGS_PATH="$(find /app -maxdepth 2 -name settings.py | head -n 1)"
fi

if [ -n "${SETTINGS_PATH}" ] && [ -f "${SETTINGS_PATH}" ]; then
    echo "Django REST Framework 개발 설정을 확인합니다: ${SETTINGS_PATH}"
    SETTINGS_PATH="${SETTINGS_PATH}" python - <<'PY'
import os
from pathlib import Path

settings_path = Path(os.environ["SETTINGS_PATH"])
settings = settings_path.read_text()


def append_installed_app(source: str, app_name: str) -> str:
    if f"'{app_name}'" in source or f'"{app_name}"' in source:
        return source
    return source.replace(
        "INSTALLED_APPS = [\n",
        f"INSTALLED_APPS = [\n    '{app_name}',\n",
        1,
    )


def append_middleware(source: str, middleware_name: str) -> str:
    if f"'{middleware_name}'" in source or f'"{middleware_name}"' in source:
        return source
    return source.replace(
        "MIDDLEWARE = [\n",
        f"MIDDLEWARE = [\n    '{middleware_name}',\n",
        1,
    )


settings = append_installed_app(settings, "rest_framework")
settings = append_installed_app(settings, "corsheaders")
settings = append_middleware(settings, "corsheaders.middleware.CorsMiddleware")

if "CORS_ALLOW_ALL_ORIGINS" not in settings:
    settings += "\n# 로컬 개발 중 프론트엔드 요청을 허용합니다.\n"
    settings += "CORS_ALLOW_ALL_ORIGINS = DEBUG\n"

if "REST_FRAMEWORK" not in settings:
    settings += "\n# Django REST Framework 기본 설정입니다.\n"
    settings += "REST_FRAMEWORK = {\n"
    settings += "    'DEFAULT_PERMISSION_CLASSES': [\n"
    settings += "        'rest_framework.permissions.AllowAny',\n"
    settings += "    ],\n"
    settings += "}\n"

settings_path.write_text(settings)
PY
else
    echo "settings.py를 찾지 못해 Django REST Framework 설정을 건너뜁니다."
fi

exec "$@"

# File History
# 2026-04-29: config 설정 패키지를 생성하는 Django 개발 entrypoint를 추가했습니다.
# 2026-04-29: Django 설정 패키지 후보를 config 기준으로 정리했습니다.
