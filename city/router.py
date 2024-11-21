from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from dependencies import get_db
from city import crud, schemas


router = APIRouter()


@router.post("/cities/", response_model=schemas.City)
async def create_city(city: schemas.CityCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create_city(db=db, city=city)


@router.get("/cities/", response_model=list[schemas.City])
async def list_cities(db: AsyncSession = Depends(get_db)):
    return await crud.get_city_list(db=db)


@router.get("/cities/{city_id}/", response_model=schemas.City)
async def detail_city(city_id: int, db: AsyncSession = Depends(get_db)):
    return await crud.get_city_by_id(db=db, id=city_id)
