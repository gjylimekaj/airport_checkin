

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

