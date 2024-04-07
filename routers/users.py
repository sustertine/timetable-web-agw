import os
import httpx
from dotenv import load_dotenv
from fastapi import APIRouter, Body
from models.users import UserRequestDto

load_dotenv()
USER_SERVICE_URL = os.getenv("USER_SERVICE_URL")

users_router = APIRouter(
    prefix="/api/users",
    tags=["users"]
)


@users_router.get("/")
async def get_all_users():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{USER_SERVICE_URL}/api/users")
    return response.json()


@users_router.get("/get-by-email/{email}")
async def get_user_by_email(email: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{USER_SERVICE_URL}/api/users/get-by-email/{email}")
    return response.json()


@users_router.post("/login")
async def login(user: UserRequestDto = Body(...)):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{USER_SERVICE_URL}/api/users/login", json=user.dict())
    return response.json()


@users_router.post("/register")
async def register(user: UserRequestDto = Body(...)):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{USER_SERVICE_URL}/api/users/register", json=user.dict())
    return response.json()


@users_router.put("/{id}")
async def update_user(user_id: str, user: UserRequestDto = Body(...)):
    async with httpx.AsyncClient() as client:
        response = await client.put(f"{USER_SERVICE_URL}/api/users/{user_id}", json=user.dict())
    return response.json()


@users_router.delete("/{id}")
async def delete_user(user_id: str):
    async with httpx.AsyncClient() as client:
        response = await client.delete(f"{USER_SERVICE_URL}/api/users/{user_id}")

    if response.status_code == 200:
        return {"message": "User deleted successfully"}
    elif response.status_code == 404:
        return {"message": f'User with id {user_id} not found'}
