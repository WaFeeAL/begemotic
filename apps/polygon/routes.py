from fastapi import APIRouter, Body

from apps.polygon.controllers import PolygonController
from apps.polygon.schemas import PolygonAggregationSchema

polygon_router = APIRouter()


@polygon_router.post(
    '/calculate-polygon-aggregation', tags=['polygon-operations']
)
async def calculate_polygon_aggregation(
        polygon_aggr: PolygonAggregationSchema = Body(...)
):
    return await PolygonController.calculate_polygon_aggregation(polygon_aggr)
