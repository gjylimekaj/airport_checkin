import uuid
from sqlalchemy import (
    JSON,
    TIMESTAMP,
    BigInteger,
    Boolean,
    Column,
    Date,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    String,
    Text,
    text,
)
from sqlalchemy.dialects.mysql import VARCHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()
metadata = Base.metadata

class PassportUsers(Base):
    __tablename__ = "passport_users"

    passport_ID =  Column(VARCHAR(255), primary_key=True, unique=True, autoincrement=True)
    first_name = Column(VARCHAR(255),nullable=False)
    last_name = Column(VARCHAR(255),nullable=False)
    country = Column(VARCHAR(255), unique=True)
    birth_date = Column(Date)