# API для классификации животных
API-сервис для классификации животных по их внешним признакам.

## Системные требования
- `Python` версии `3.12.4` или выше

## Установка

1. Склонируйте репозиторий:
```
git clone https://github.com/MegaDoge1337/otus_ml_api.git
```

2. Соберите Docker-образ:
```
docker-compose build
```

3. При необходимости заполните файл `.env` (см. раздел `Переменные среды`), и добавьте его в `docker-compose.yml`:
```yml
version: '3.8'

services:
    web:
        image: fastapi-ml-app
        build:
            context: .
            dockerfile: Dockerfile
        ports:
            - "8000:8000"
        volumes:
            - ./:/app
        restart: always
        env_file: .env
```

4. Создайте базу данных `db.json` (см. раздел `База данных`)

5. Запустите сервис:
```
docker-compose up -d
```

## Переменные среды

Для задания переменных среды скопируйте файл `.env.example` как `.env` и заполните следующие значения:
```py
SECRET_KEY= # секретный ключ для генерации JWT-токенов
ALGORITHM= # алгоритм шифрования
ACCESS_TOKEN_EXPIRE_MINUTES= # время, за которое JWT-токен истекает (в минутах, по умолчанию 1 минута)
```

## База данных

В качестве примитивной базы данных для хранения пользователей используется `JSON`-документ со следующей структурой:
```py
{
    "john_doe": { # ключом выступает логин пользователя
        "username": "john_doe", # имя пользователя
        "hashed_password": "$2b$12$Rk3jf9xInxJj0f61PmT2G.kwCplb0SlFehdX05vLrjpMDCy1L4u4e", # хеш пароля (хешируется алгоритмом bcrypt)
        "email": "john@example.com", # электронная почта пользователя
        "age": 40 # возраст пользователя
    }
}
```

## Использование

В начале работы необходимо авторизоваться, для этого вы можете получить токен, отправив следующий POST-запрос по маршруту `/token`:
```
curl --location 'http://localhost:8000/token' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'username=john_doe' \
--data-urlencode 'password=mypassword'
```

Пример ответа:
```py
{
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJqb2huX2RvZSIsImV4cCI6MTczNTIxMzU3Mn0.JyxVg7NjihW2UXVtYwTHngxDQ_POnmmJezQM8Mu9tRc",
    "token_type": "bearer"
}
```

Для запуска фейковой ML-модели выполните запрос по маршруту `/make_inference` со следующими параметрами:
```py
{
    "paws_count": 4, # количество лап
    "has_fur": 1,    # есть ли у животного шерсть
    "mammal": 1      # является ли животное млекопитающим
}
```

Для доступа к маршруту, поместите ранее полученный токен в заголовок `Authorization`.

Пример curl-запроса:
```
curl --location 'http://localhost:8000/make_inference' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJqb2huX2RvZSIsImV4cCI6MTczNTIxMzU3Mn0.JyxVg7NjihW2UXVtYwTHngxDQ_POnmmJezQM8Mu9tRc' \
--header 'Content-Type: application/json' \
--data '{
    "paws_count": 4,
    "has_fur": 1,
    "mammal": 1
}'
```

Пример ответа:
```py
{
    "result": "dog",
    "user": {
        "username": "john_doe",
        "email": "john@example.com",
        "age": 40
    }
}
```
