import os
from typing import List

import httpx
from dotenv import load_dotenv
from fastapi import APIRouter, Body

from models.timetables import TimetableResponseDto, TimetableRequestDto, TimetableEntryResponseDto, \
    TimetableEntryRequestDto

load_dotenv()
TIMETABLE_SERVICE_URL = os.getenv("TIMETABLE_SERVICE_URL")

timetables_router = APIRouter(
    prefix="/api/timetables",
    tags=["timetables"]
)


@timetables_router.get("/")
async def get_all_timetables():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{TIMETABLE_SERVICE_URL}/api/timetables")
    return response.json()


@timetables_router.post("/")
async def create_new_timetable(timetable: TimetableRequestDto = Body(...)):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{TIMETABLE_SERVICE_URL}/api/timetables", json=timetable.dict())
    return response.json()


@timetables_router.get("/{id}", response_model=TimetableResponseDto)
async def get_timetable_by_id(timetable_id: int):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{TIMETABLE_SERVICE_URL}/api/timetables/{timetable_id}")
    return response.json()


@timetables_router.put("/{id}")
async def update_timetable(timetable_id: int, timetable: TimetableRequestDto = Body(...)):
    async with httpx.AsyncClient() as client:
        response = await client.put(f"{TIMETABLE_SERVICE_URL}/api/timetables/{timetable_id}", json=timetable.dict())
    return response.json()


@timetables_router.delete("/{id}")
async def delete_timetable(timetable_id: int):
    async with httpx.AsyncClient() as client:
        response = await client.delete(f"{TIMETABLE_SERVICE_URL}/api/timetables/{timetable_id}")
    return response.json()


@timetables_router.get("/{id}/entries", response_model=List[TimetableEntryResponseDto])
async def get_all_entries_for_timetable(timetable_id: int):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{TIMETABLE_SERVICE_URL}/api/timetables/{timetable_id}/entries")
    return response.json()


@timetables_router.post("/{id}/entries")
async def add_entry_to_timetable(timetable_id: int, entry: TimetableEntryRequestDto = Body(...)):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{TIMETABLE_SERVICE_URL}/api/timetables/{timetable_id}/entries",
                                     json=entry.dict())
    return response.json()


@timetables_router.delete("/{id}/entries/{entryId}")
async def delete_entry_from_timetable(timetable_id: int, entry_id: int):
    async with httpx.AsyncClient() as client:
        response = await client.delete(f"{TIMETABLE_SERVICE_URL}/api/timetables/{timetable_id}/entries/{entry_id}")
    return response.json()

