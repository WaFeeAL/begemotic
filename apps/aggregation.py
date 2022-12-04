from h3 import geo_to_h3

from apps.core import get_settings
from apps.core.loader import load_csv
from apps.enums import AggregationTypeEnum, DatasetFieldEnum, GeoPositionEnum
from apps.schemas import GeoCharacteristicsSchema


class Aggregation:
    AGGREGATION: int = 0
    COUNT: int = 0

    async def update_aggregation(
            self, aggregation_type: str, field: int | float
    ) -> None:
        if aggregation_type == AggregationTypeEnum.SUM:
            self.AGGREGATION += field
        elif aggregation_type == AggregationTypeEnum.AVG:
            self.AGGREGATION += field
            self.COUNT += 1
        elif aggregation_type == AggregationTypeEnum.MIN:
            if self.AGGREGATION == 0 or field < self.AGGREGATION:
                self.AGGREGATION = field
        elif aggregation_type == AggregationTypeEnum.MAX:
            if field > self.AGGREGATION:
                self.AGGREGATION = field

    async def calculate_aggregation(
            self, aggr_schema, hex_ids: set
    ) -> int | float:
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

            if hex_id in hex_ids:
                await self.update_aggregation(
                    aggr_schema.aggregation,
                    geo_characteristics.dict().get(aggr_schema.field)
                )

        if aggr_schema.aggregation == AggregationTypeEnum.AVG:
            return round(self.AGGREGATION / self.COUNT, 2)
        else:
            return self.AGGREGATION
