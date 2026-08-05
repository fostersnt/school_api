from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import Optional
from commons.Util import CustomUtility
from model.Student import StudentCreateDto
from model.Student import StudentResponseDto

from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException as FastAPIHTTPException

# Initialize FastAPI instance (backed by Starlette)
app = FastAPI(title="Item Management API", version="1.0.0")


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
        status_code=exc.status_code, content={"success": False, "message": exc.detail}
    )

students = []
id_counter = 0


@app.post("/students", response_model=StudentResponseDto, status_code=status.HTTP_201_CREATED)
def create_item(student: StudentCreateDto):
    msisdn_check = CustomUtility.validateMsisdn(student.msisdn)
    if msisdn_check == False:
        raise HTTPException(
            status_code=500,
            detail=CustomUtility.apiResponseFormat(False, "Invalid msisdn", []),
        )
    else:
        global id_counter
        new_item = StudentResponseDto(id=id_counter, **student.model_dump())
        students.append(new_item)
        id_counter += 1
        return new_item
