import traceback
import os
import aioredis
import redis
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker



# DB_NAME = os.getenv("DB_NAME").replace("'", "")
# DB_USER = os.getenv("DB_USER").replace("'", "")
# DB_PASSWORD = os.getenv("DB_PASSWORD").replace("'", "")
# DB_HOST = os.getenv("DB_HOST").replace("'", "")
# DB_PORT = os.getenv("DB_PORT").replace("'", "")

DB_NAME = "gjylis_db"
DB_USER = "gjyli"
DB_PASSWORD = "12345678"
DB_HOST = "139.59.156.28"
DB_PORT = "3306"
# Construct the DATABASE_URL for connecting to the database

DATABASE_URL = (f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

Base = declarative_base()
engine = create_engine(DATABASE_URL)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create an async session factory for async sessions
async_session = sessionmaker(
    bind=create_async_engine(f"mysql+aiomysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}", echo=False,),
    class_=AsyncSession,
    expire_on_commit=False,
)


async def get_async_db_session() -> AsyncSession:
    """
    Get an asynchronous database session.

    Returns:
        AsyncSession: An asynchronous database session.
    """
    async with async_session() as session:
        yield session


def get_db():
    """
    Get a synchronous database session.

    Returns:
        Session: A synchronous database session.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


async def get_redis_async_connection() -> aioredis.Connection:
    """
    This function makes an async connection to redis db
    for any transaction related to redis
    """
    conn = None
    try:
        conn = await aioredis.from_url(
            f"redis://{REDIS.get('HOST')}:{REDIS.get('PORT')}/{REDIS.get('DBNUM')}"
        )
        yield conn
    except aioredis.RedisError:
        print(traceback.format_exc())
    finally:
        # close the connection
        await conn.close()


def get_redis_connection() -> redis.Connection:
    """
    This function makes a connection to redis db
    for any transaction related to redis
    """
    conn = None
    try:
        conn = redis.Redis(
            host=REDIS.get("HOST"), port=REDIS.get("PORT"), db=REDIS.get("DBNUM")
        )
        yield conn
    except redis.RedisError:
        print(traceback.format_exc())
    finally:
        # closing the connection
        conn.close()

