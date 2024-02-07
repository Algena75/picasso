# API service
Files uploading and handling API service
## Автор:
Алексей Наумов ( algena75@yandex.ru )
## Используемые технолологии:
* Django
* PostgreSQL
* Docker
* Celery
* Redis
* Nginx
## Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:


```
git clone git@github.com:Algena75/picasso.git
```

```
cd picasso
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```
## Как запустить проект локально:
В корне проекта создать файл `.env` с настройками для базы данных, после чего:
* #### для запуска проекта в контейнерах выполнить:
    ```
    docker compose -f docker-compose.yml up -d
    ```
    открыть в браузере http://127.0.0.1/
* #### для запуска проекта в терминале перейти в директорию `backend` и выполнить:
    - в одном терминале 
    ```
    python3 manage.py runserver
    ```
    - во втором терминале 
    ```
    celery -A backend worker --loglevel=info --concurrency 1 -E
    ```
    открыть в браузере http://127.0.0.1:8000/
