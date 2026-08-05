from pydantic import BaseModel, Field

class Student(BaseModel):
    first_name: str = Field(..., example='John', min_length=3)
    last_name: str = Field(..., example='Doe', min_length=3)
    level: str = Field(..., example='Basic 2')
    age: int = Field(..., gt=0, lt=100)
    msisdn: str = Field(..., example='233xxxxxxxxx')

class StudentCreateDto(Student):
    pass

class StudentResponseDto(Student):
    id: int