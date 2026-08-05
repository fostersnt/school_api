from pydantic import BaseModel, Field

class StudentCreate(BaseModel):
    first_name: str
    last_name: str
    level: str
    age: int
    msisdn: str


class StudentResponse(StudentCreate):
    id: int

    class Config:
        from_attributes = True