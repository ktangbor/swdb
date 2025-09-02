from fastapi import APIRouter, Depends, status, Query
from sqlalchemy.ext.asyncio import AsyncSession

from swdb_app.api.v1.schemas.character import (CharacterRead,
                                               CharacterFilter)
from swdb_app.dependencies import get_async_session
from swdb_app.services.character import CharacterService
from swdb_app.services.orchestrator import OrchestratorService


router = APIRouter(prefix="/characters", tags=["Characters"])


@router.post("/fetch-all", status_code=status.HTTP_200_OK)
async def fetch_all(
        session: AsyncSession = Depends(get_async_session)):
    characters_count, films_count = \
        await OrchestratorService.fetch_sync_films(session)
    return {"message": f"Fetched and stored {characters_count} "
                       f"characters and {films_count} films"}


@router.get("/", response_model=list[CharacterRead],
            status_code=status.HTTP_200_OK)
async def list_all(
        session: AsyncSession = Depends(get_async_session)):
    page: int = Query(1, ge=1)
    size: int = Query(10, ge=1, le=100)
    offset = (page - 1) * size
    return await CharacterService.get_all(
        session, offset=offset, limit=size)


@router.get("/search", response_model=list[CharacterRead])
async def search(
        session: AsyncSession = Depends(get_async_session),
        filters: CharacterFilter = Depends()):
    return await CharacterService.search(session, filters.dict())
