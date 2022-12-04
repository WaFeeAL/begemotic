from h3 import polyfill

from apps.aggregation import Aggregation
from apps.core import get_settings
from apps.polygon.schemas import PolygonAggregationSchema


class PolygonController:
    @staticmethod
    async def calculate_polygon_aggregation(
            polygon_aggr: PolygonAggregationSchema
    ):
        polygon_ids = polyfill(
            polygon_aggr.geometry.dict(), get_settings().DEFAULT_RADIUS, True
        )

        return await Aggregation().calculate_aggregation(
            polygon_aggr, polygon_ids
        )

