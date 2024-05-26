from pydantic import BaseModel


class GroupCreateDto(BaseModel):
    name: str
    userIds: list[str]
    adminId: str
    timetableId: int
