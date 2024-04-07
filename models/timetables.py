from pydantic import BaseModel, Field
from typing import List


class TimetableEntryRequestDto(BaseModel):
    title: str = Field(...)
    description: str = Field(...)
    startTime: str = Field(..., format="date-time")
    endTime: str = Field(..., format="date-time")
    recurring: bool = Field(...)


class TimetableRequestDto(BaseModel):
    title: str = Field(...)
    description: str = Field(...)
    groupId: str = Field(...)


class TimetableEntryResponseDto(BaseModel):
    id: str = Field(...)
    title: str = Field(...)
    description: str = Field(...)
    startTime: str = Field(..., format="date-time")
    endTime: str = Field(..., format="date-time")
    recurring: bool = Field(...)


class TimetableResponseDto(BaseModel):
    id: str = Field(...)
    title: str = Field(...)
    description: str = Field(...)
    groupId: str = Field(...)
    entries: List[TimetableEntryResponseDto] = Field(...)
