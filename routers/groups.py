from fastapi import APIRouter

groups_router = APIRouter(
    prefix="/api/groups",
    tags=["groups"],
)

