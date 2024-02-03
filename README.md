# testwork_picasso
Files uploading and handling API service
## Автор:
Алексей Наумов ( algena75@yandex.ru )
## Используемые технолологии:
* Django
* SQLite/PostgreSQL
* Docker
* Celery
* Redis
* Nginx
## Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:


```
git clone git@github.com:Algena75/testwork_picasso.git
```

```
cd testwork_picasso
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
Из корня проекта выполнить
```
docker compose -f docker-compose.yml up -d
```
открыть в браузере http://127.0.0.1/
