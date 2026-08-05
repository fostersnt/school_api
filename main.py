from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import Optional
from commons.Util import CustomUtility

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


class ItemBase(BaseModel):
    name: str = Field(..., example="Wireless Mouse")
    age: int = Field(...)
    msisdn: str = Field(..., min_length=12, max_length=12, example="233xxxxxxxxx")
    # level: Optional[str] = Field(None, example="A fast 2.4GHz mouse")
    # price: float = Field(..., gt=0, example=29.99)


class ItemCreate(ItemBase):
    pass


class ItemResponse(ItemBase):
    id: int


students = []
id_counter = 0


@app.post("/items", response_model=ItemResponse, status_code=status.HTTP_201_CREATED)
def create_item(item: ItemCreate):
    msisdn_check = CustomUtility.validateMsisdn(item.msisdn)
    if msisdn_check == False:
        raise HTTPException(
            status_code=500,
            detail=CustomUtility.apiResponseFormat(False, "Invalid msisdn", []),
        )
    else:
        global id_counter
        new_item = ItemResponse(id=id_counter, **item.model_dump())
        students.append(new_item)
        id_counter += 1
        return new_item
