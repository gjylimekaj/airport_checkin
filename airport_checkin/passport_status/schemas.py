import datetime
from sqlalchemy import Date
from pydantic import BaseModel

class PassportUser(BaseModel):
    first_name: str
    last_name: str
    country: str
    birth_date: datetime.date
