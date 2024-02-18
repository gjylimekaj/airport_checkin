from fastapi import APIRouter,Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from .schemas import PassportUser
from airport_checkin.database.database_config import get_async_db_session
from .crud import query_all_passport_users, query_passport_users_by_country, query_first_user, add_passport_member

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

@passport_status_app.get("/get_first_user_from_passport")
async def get_first_user_from_passport(db: AsyncSession = Depends(get_async_db_session)):
    first_user = await query_first_user(db)
    return first_user

@passport_status_app.get("/get_passport_users_by_their_country/{contry}")
async def get_passport_users_by_their_country(country : str, db: AsyncSession = Depends(get_async_db_session)):
    users_by_country = await query_passport_users_by_country(country, db)
    return users_by_country

@passport_status_app.post("/add_passport_user")
async def insert_member_to_db(passport_scheme: PassportUser, db: AsyncSession = Depends(get_async_db_session)):
    try:
        print(passport_scheme)

        await add_passport_member(passport_scheme.first_name, passport_scheme.last_name, passport_scheme.country, passport_scheme.birth_date, db)

        return {"message": "Passport user added successfully"}

    except Exception as e:
        print(e)