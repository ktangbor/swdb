from fastapi import APIRouter, Depends, status, Query
from sqlalchemy.ext.asyncio import AsyncSession

from swdb_app.api.v1.schemas.film import (FilmRead, FilmFilter)
from swdb_app.dependencies import get_async_session
from swdb_app.services.film import FilmService


router = APIRouter(prefix="/films", tags=["Films"])


@router.post("/fetch-all", status_code=status.HTTP_200_OK)
async def fetch_all(
        session: AsyncSession = Depends(get_async_session())):
    characters_count, films_count = \
        await FilmService.fetch_all(session)
    return {"message": f"Fetched and stored {characters_count} "
                       f"characters and {films_count} films"}


@router.get("/", response_model=list[FilmRead],
            status_code=status.HTTP_200_OK)
async def list_all(
        session: AsyncSession = Depends(get_async_session())):
    page: int = Query(1, ge=1)
    size: int = Query(10, ge=1, le=100)
    offset = (page - 1) * size
    return await FilmService.get_all(
        session, offset=offset, limit=size)


@router.get("/search", response_model=list[FilmRead])
async def search(
        session: AsyncSession = Depends(get_async_session()),
        filters: FilmFilter = Depends()):
    return await FilmService.search(session, filters.dict())
