from apps.begemotic.schemas import AggregationTypeEnum


async def update_aggregation(
        aggregation_type: str, aggregation: int, field: int | float,
        hexes_count: int | None = None
):
    if aggregation_type == AggregationTypeEnum.SUM:
        return aggregation + field
    elif aggregation_type == AggregationTypeEnum.AVG:
        return aggregation + field, hexes_count + 1
    elif aggregation_type == AggregationTypeEnum.MIN:
        if aggregation == 0:
            return field
        elif field < aggregation:
            return field
        else:
            return aggregation
    elif aggregation_type == AggregationTypeEnum.MAX:
        if field > aggregation:
            return field
        else:
            return aggregation
