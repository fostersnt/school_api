from pydantic import BaseModel, Field

class StudentModel:
    first_name: str = Field(..., examples='John', min_length=3)
    last_name: str = Field(..., examples='Doe', min_length=3)
    level: str = Field(..., examples='Basic 2')
    age: int = Field(..., gt=0, lt=100)