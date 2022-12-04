from enum import Enum


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
