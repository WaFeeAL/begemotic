from geojson_pydantic import Point
from pydantic import BaseModel, Extra, Field

from apps.enums import AggregationTypeEnum, DatasetFieldEnum


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
