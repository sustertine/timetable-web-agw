import os

import httpx
from dotenv import load_dotenv
from fastapi import APIRouter, Body

from models.timetables import TimetableEntryResponseDto, TimetableEntryRequestDto

load_dotenv()
TIMETABLE_SERVICE_URL = os.getenv("TIMETABLE_SERVICE_URL")

timetable_entries_router = APIRouter(
    prefix="/api/timetable-entries",
    tags=["timetable-entries"]
)


@timetable_entries_router.get("/{id}", response_model=TimetableEntryResponseDto)
async def get_timetable_entry_by_id(entry_id: int):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{TIMETABLE_SERVICE_URL}/api/timetable-entries/{entry_id}")
    return response.json()


@timetable_entries_router.put("/{id}")
async def update_timetable_entry(entry_id: int, entry: TimetableEntryRequestDto = Body(...)):
    async with httpx.AsyncClient() as client:
        response = await client.put(f"{TIMETABLE_SERVICE_URL}/api/timetable-entries/{entry_id}", json=entry.dict())
    return response.json()
