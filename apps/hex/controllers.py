from h3 import geo_to_h3, k_ring

from apps.hex.schemas import HexAggregationSchema
from apps.aggregation import Aggregation
from apps.core import get_settings
from apps.enums import GeoPositionEnum


class HexController:
    @staticmethod
    async def calculate_hexes_aggregation(hexes_aggr: HexAggregationSchema):
        hex_id: str = geo_to_h3(
            hexes_aggr.geometry.coordinates[GeoPositionEnum.LATITUDE],
            hexes_aggr.geometry.coordinates[GeoPositionEnum.LONGITUDE],
            get_settings().DEFAULT_RADIUS
        )

        hexes_ring: set = k_ring(hex_id, hexes_aggr.radius)

        return await Aggregation().calculate_aggregation(
            hexes_aggr, hexes_ring
        )
