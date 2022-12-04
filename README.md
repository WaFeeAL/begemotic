# О проекте

Домашняя работа от <a href="https://www.bestplace.pro/" class="external-link" target="_blank">BestPlace</a>.

## Требования

Для развёртывания проекта необходимы:

* **Docker**
* **docker-compose**

## Развёртывание

Нужно создать файл с переменными виртуального окружения `.env` по примеру файла `example.env` или просто скопировать:

```dotenv
HOST=localhost
PORT=8000
DEBUG=True
DEFAULT_DATASET_NAME=apartments.csv
```

Затем необходимо открыть консоль в корневой папке проекта и выполнить следующую команду:

```console
$ docker-compose up -d --build
```

Об успешности развертывания сообщают такие строки в консоли:

```console
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process []
INFO:     Started server process []
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

### Документация

Документация расположена по адресу <a href="http://127.0.0.1:777/docs" class="external-link" target="_blank">127.0.0.1:777/docs</a>.

Пример данных запроса по пути `/calculate-hexes-aggregation`:

```JSON
{
  "geometry": {
    "coordinates": [
      "37.517259",
      "55.542444"
    ],
    "type": "Point"
  },
  "field": "apartments",
  "aggr": "sum",
  "r": 4
}
```

Пример данных запроса по пути `/calculate-polygon-aggregation`:

```JSON
{
  "geometry": {
    "coordinates": [
      [
        [37.520123, 55.54413],
        [37.515671, 55.54399],
        [37.514662, 55.541793],
        [37.521218, 55.542612],
        [37.520123, 55.54413]
      ]
    ],
    "type": "Polygon"
  },
  "field": "price",
  "aggr": "avg"
}
```