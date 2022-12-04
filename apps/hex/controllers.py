from h3 import geo_to_h3, k_ring

from apps.hex.schemas import HexesAggregationSchema
from apps.hex.utils import update_aggregation
from apps.core import get_settings
from apps.core.loader import load_csv
from apps.enums import AggregationTypeEnum, DatasetFieldEnum, GeoPositionEnum
from apps.schemas import GeoCharacteristicsSchema


class HexController:
    @staticmethod
    async def calculate_hexes_aggregation(hexes_aggr: HexesAggregationSchema):
        hex_id: str = geo_to_h3(
            hexes_aggr.geometry.coordinates[GeoPositionEnum.LATITUDE],
            hexes_aggr.geometry.coordinates[GeoPositionEnum.LONGITUDE],
            get_settings().DEFAULT_RADIUS
        )

        hexes_ring: set = k_ring(hex_id, hexes_aggr.radius)

        aggregation: int = 0
        hexes_count: int = 0

        async for row in load_csv(DatasetFieldEnum.GEO_POSITION):
            geo_characteristics: GeoCharacteristicsSchema = \
                GeoCharacteristicsSchema.parse_obj(row)

            hex_id: str = geo_to_h3(
                geo_characteristics.geo_position.coordinates[
                    GeoPositionEnum.LATITUDE
                ],
                geo_characteristics.geo_position.coordinates[
                    GeoPositionEnum.LONGITUDE
                ],
                get_settings().DEFAULT_RADIUS
            )

            if hex_id in hexes_ring:
                if hexes_aggr.aggregation == AggregationTypeEnum.AVG:
                    aggregation, hexes_count = await update_aggregation(
                        hexes_aggr.aggregation,
                        aggregation,
                        geo_characteristics.dict().get(hexes_aggr.field),
                        hexes_count
                    )
                else:
                    aggregation = await update_aggregation(
                        hexes_aggr.aggregation,
                        aggregation,
                        geo_characteristics.dict().get(hexes_aggr.field),
                    )

        if hexes_aggr.aggregation == AggregationTypeEnum.AVG:
            return aggregation / hexes_count
        else:
            return aggregation
