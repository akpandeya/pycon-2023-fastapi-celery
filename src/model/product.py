from decimal import Decimal
from uuid import UUID

from pydantic import BaseModel


class Discount(BaseModel):
    code: str
    rate: int


class Product(BaseModel):
    id: UUID
    name: str
    currency: str
    price: Decimal
    discounts: list[Discount]
    description: str
    image: str
    in_stock: int
