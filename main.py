from fastapi import FastAPI, HTTPException, status
# from pydantic import BaseModel, Field
# from typing import Optional
from commons.Util import CustomUtility
from schema.StudentSchema import StudentCreateDto
from schema.StudentSchema import StudentResponseDto
from fastapi import Depends
from sqlalchemy.orm import Session
from model.Student import Student
from db_config.db_connection import get_db
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException as FastAPIHTTPException
from db_config.db_connection import engine, Base
from commons.ApiResponse import ApiResponse

# Initialize FastAPI instance (backed by Starlette)
app = FastAPI(title="Item Management API", version="1.0.0")
Base.metadata.create_all(bind=engine)


#! Validation errors handler
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    errors = []

    for error in exc.errors():
        errors.append({"field": error["loc"][-1], "message": error["msg"]})

    return JSONResponse(
        status_code=422,
        content={"success": False, "message": "Validation failed", "errors": errors},
    )


#! Exception handler
@app.exception_handler(FastAPIHTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code, content=exc.detail
    )

students = []
id_counter = 0


@app.post("/students")
def create_student(
    student: StudentCreateDto,
    db: Session = Depends(get_db)
):

    new_student = Student(
        first_name=student.first_name,
        last_name=student.last_name,
        level=student.level,
        age=student.age,
        msisdn=student.msisdn
    )

    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    return CustomUtility.apiResponseFormat(True, "Student created successfully", new_student)
