from geojson_pydantic import Point
from pydantic import BaseModel, Extra, Field


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
