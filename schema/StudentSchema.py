from pydantic import BaseModel, Field

class StudentCreateDto(BaseModel):
    first_name: str
    last_name: str
    level: str
    age: int
    msisdn: str


class StudentResponseDto(StudentCreateDto):
    id: int

    class Config:
        from_attributes = True