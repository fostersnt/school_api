from pydantic import BaseModel, Field

class StudentCreateDto(BaseModel):
    first_name: str
    middle_name: str
    last_name: str
    level: str
    age: int
    phone_number: str


class StudentResponseDto(StudentCreateDto):
    id: int

    class Config:
        from_attributes = True