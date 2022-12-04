from enum import Enum

from geojson_pydantic import Point
from pydantic import BaseModel, Extra, Field


class GeoPositionEnum(int,  Enum):
    LONGITUDE: int = 0
    LATITUDE: int = 1


class DatasetFieldEnum(str, Enum):
    ID: str = 'id'
    GEO_POSITION: str = 'geopos'
    APARTMENTS: str = 'apartments'
    PRICE: str = 'price'
    YEAR: str = 'year'


class AggregationTypeEnum(str, Enum):
    SUM: str = 'sum'
    AVG: str = 'avg'
    MIN: str = 'min'
    MAX: str = 'max'


class GeoCharacteristicsSchema(BaseModel):
    id: int = Field(
        ..., unique=True, title='Уникальный идентификатор',
        description='Уникальный идентификатор дома.'
    )
    geo_position: Point = Field(
        ..., alias='geopos', title='Координаты дома',
        description='Координаты дома в формате geojson (порядок координат: '
                    'долгота, широта).'
    )
    apartments: int = Field(
        ..., title='Количество квартир',
        description='Количество квартир в доме.'
    )
    price: float = Field(
        ..., title='Средняя стоимость',
        description='Средняя стоимость квартир в доме за 1 кв. м'
    )
    year: int = Field(
        ..., title='Год постройки',
        description='Год постройки дома.'
    )

    class Config:
        extra = Extra.forbid


class HexesAggregationSchema(BaseModel):
    geometry: Point = Field(
        ..., title='Координаты точки',
        description='Координаты точки в формате geojson.'
    )
    field: DatasetFieldEnum = Field(
        ..., title='Поле',
        description='Поле датасета.'
    )
    aggregation: AggregationTypeEnum = Field(
        ..., alias='aggr', title='Тип агрегации',
        description='Тип агрегации.'
    )
    radius: int = Field(
        ..., alias='r', title='Радиус',
        description='Размер радиуса в гексах.'
    )

    class Config:
        extra = Extra.forbid
        error_msg_templates = {
            'type_error.float': 'Ожидается вещественное значение.',
            'type_error.integer': 'Ожидается целочисленное значение.',
            'value_error.const': 'Введено недопустимое значение.',
            'type_error.enum': 'Введено недопустимое значение.',
            'value_error.extra': 'Введено недопустимое значение.',
            'type_error.none.not_allowed': 'Обязательное поле.',
            'value_error.missing': 'Обязательное поле.'
        }
