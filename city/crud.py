from sqlalchemy import insert, update
from sqlalchemy.ext.asyncio import AsyncSession

from city import models, schemas


async def create_city(db: AsyncSession, city: schemas.CityCreate) -> models.City:
    query = insert(models.City).values(
        name=city.name,
        additional_info=city.additional_info,
    )
    result = await db.execute(query)
    await db.commit()
    resp = {**city.model_dump(), "id": result.lastrowid}
    return models.City(**resp)
