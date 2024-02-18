from fastapi import Depends

from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload
from airport_checkin.database.model import PassportUsers
from airport_checkin.database.database_config import get_async_db_session



async def query_all_passport_users(db: AsyncSession = Depends(get_async_db_session)):
    async with db.begin():
        all_passport_users = await db.execute(select(PassportUsers))
        people_found = all_passport_users.scalars().all()
        if people_found:
            return people_found

async def query_first_user(db: AsyncSession = Depends(get_async_db_session)):
    async with db.begin():
        all_passport_users = await db.execute(select(PassportUsers))
        first_user_found = all_passport_users.scalars().first()
        if first_user_found:
            return first_user_found

async def query_passport_users_by_country(the_country, db: AsyncSession = Depends(get_async_db_session)):
    async with db.begin():
        users_by_country = await db.execute(select(PassportUsers).where(PassportUsers.country == the_country))
        users_found = users_by_country.scalars().all()
        if users_found:
            return users_found

async def add_passport_member(first_name, last_name, country, birth_date, db: AsyncSession = Depends((get_async_db_session))):
    new_member = PassportUsers(
        first_name = first_name,
        last_name = last_name,
        country = country,
        birth_date = birth_date
    )
    async  with db.begin():
        db.add(new_member)
        await db.flush()
        await db.commit()
        await db.close()
    return new_member
