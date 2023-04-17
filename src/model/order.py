from decimal import Decimal
from typing import Optional
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class OrderItemData(BaseModel):
    product_id: UUID
    quantity: int
    discount_code: str = None


class OrderData(BaseModel):
    id: Optional[UUID] = Field(default_factory=uuid4, primary_key=True)

    customer_name: str
    customer_email: str
    shipping_address: str
    payment_info: str
    items: list[OrderItemData]


class OrderResponse(OrderData):
    total_cost: Decimal
