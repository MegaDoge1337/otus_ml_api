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

3. Запустите сервис:
```
docker-compose up -d
```

## Использование

Сервис использует один основной `POST`-метод `/make_inference` со следующими параметрами:
```py
{
    "paws_count": 4, # количество лап
    "has_fur": 1,    # есть ли у животного шерсть
    "mammal": 1      # является ли животное млекопитающим
}
```

Пример curl-запроса:
```
curl --location 'http://localhost:8000/make_inference' \
--header 'Content-Type: application/json' \
--data '{
    "paws_count": 4,
    "has_fur": 1,
    "mammal": 1
}'
```

Ответ возвращается в формате JSON с полем `result`:
```py
{
    "result": "dog"
}
```
