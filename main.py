from fastapi import FastAPI
from starlette.responses import RedirectResponse

from routers.timetable_entries import timetable_entries_router
from routers.timetables import timetables_router
from routers.users import users_router

app = FastAPI()
app.include_router(timetables_router)
app.include_router(timetable_entries_router)
app.include_router(users_router)


@app.get("/")
async def root():
    return RedirectResponse(url="/docs")
