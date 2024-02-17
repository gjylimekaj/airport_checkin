from fastapi import APIRouter,Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from airport_checkin.database.model import PassportUsers
from airport_checkin.database.database_config import get_async_db_session
from .crud import query_all_passport_users

passport_status_app = APIRouter(
    tags=["passport_status"]
)

@passport_status_app.get("/get_data_from_people")
async def get_user_info_from_passport(db: AsyncSession = Depends(get_async_db_session)):
    the_query_function = await query_all_passport_users(db)


    if not the_query_function:
        raise HTTPException(status_code=409, detail="Sorry, no passport users found")

    elif the_query_function:
        return the_query_function
