from decimal import Decimal
from typing import Annotated

from fastapi import APIRouter, Depends
from src.model import OrderData, OrderResponse
from src.service import EmailService, OrderService, ProductService
from src.tasks import send_email_task

# order_router_v1 = APIRouter(prefix="/v1/order")


# @order_router_v1.post("/", status_code=201, response_model=OrderResponse)
# def create_order(
#     *,
#     order_data: OrderData,
#     email_service: Annotated[EmailService, Depends(EmailService)],
#     product_service: Annotated[ProductService, Depends(ProductService)],
# ):
#     email_service.send_email(
#         order_data.customer_email, f"Order Created {order_data}"
#     )

#     total_cost = Decimal(0)
#     for item in order_data.items:
#         product = product_service.get_by_id(item.product_id)
#         item_price = product.price
#         for discount in product.discounts:
#             if item.discount_code == discount.code:
#                 item_price *= Decimal(1 - discount.rate / 100)
#                 break
#         total_cost += item_price * item.quantity

#     return OrderResponse(
#         customer_name=order_data.customer_name,
#         customer_email=order_data.customer_email,
#         shipping_address=order_data.shipping_address,
#         payment_info=order_data.payment_info,
#         items=order_data.items,
#         total_cost=round(total_cost, 2),
#     )


# @order_router_v1.post("/", status_code=201, response_model=OrderResponse)
# def create_order(
#     *,
#     order_data: OrderData,
#     email_service: Annotated[EmailService, Depends(EmailService)],
#     order_service: Annotated[OrderService, Depends(OrderService)],
# ):
#     email_service.send_email(
#         order_data.customer_email, f"Order Created {order_data}"
#     )

#     return order_service.create_order_response(order_data)


# @order_router_v1.post("/1", status_code=201, response_model=OrderResponse)
# def create_order(
#     *,
#     order_data: OrderData,
#     order_service: Annotated[OrderService, Depends(OrderService)],
# ):
#     send_email_task.delay(
#         order_data.customer_email, f"Order Created {order_data}"
#     )

#     return order_service.create_order_response(order_data)
