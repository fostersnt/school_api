from sqlalchemy import Column, Integer, String
from db_config.db_connection import Base


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    level = Column(String)
    age = Column(Integer)
    msisdn = Column(String)