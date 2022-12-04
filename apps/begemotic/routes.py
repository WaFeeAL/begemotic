from fastapi import APIRouter, Body

from apps.begemotic.controllers import HexController
from apps.begemotic.schemas import HexesAggregationSchema

router = APIRouter()


@router.post('/calculate-hexes-aggregation', tags=['hex-operations'])
async def calculate_hexes_aggregation(
        hexes_aggr: HexesAggregationSchema = Body(...)
):
    return await HexController.calculate_hexes_aggregation(hexes_aggr)
