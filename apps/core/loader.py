from aiocsv import AsyncDictReader
from aiofiles import open

from apps.core import get_settings


async def load_csv(geojson_field: str):
    async with open(
            get_settings().ROOT_DIR / get_settings().DEFAULT_DATASET_NAME,
            mode='r', encoding='utf-8'
    ) as f:
        async for row in AsyncDictReader(f):
            try:
                row[geojson_field] = row[geojson_field].replace('\'', '\"')
            except KeyError as e:
                raise KeyError(
                    "There is no geojson format field named "
                    f"'{geojson_field}' in the dataset."
                ) from e
            yield row
