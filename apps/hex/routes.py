from fastapi import APIRouter, Body

from apps.hex.controllers import HexController
from apps.hex.schemas import HexesAggregationSchema

hex_router = APIRouter()


@hex_router.post('/calculate-hexes-aggregation', tags=['hex-operations'])
async def calculate_hexes_aggregation(
        hexes_aggr: HexesAggregationSchema = Body(...)
):
    return await HexController.calculate_hexes_aggregation(hexes_aggr)
