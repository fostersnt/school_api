from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import Optional


class ItemBase(BaseModel):
    name: str = Field(..., example="Wireless Mouse")
    description: Optional[str] = Field(None, example="A fast 2.4GHz mouse")
    price: float = Field(..., gt=0, example=29.99)


class ItemCreate(ItemBase):
    pass


class ItemResponse(ItemBase):
    id: int
