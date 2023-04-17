from decimal import Decimal

from src.model import OrderData, OrderResponse
from src.service import ProductService


# class OrderService:
#     def __init__(self, product_service=ProductService()) -> None:
#         self.product_service = product_service

#     def create_order_response(self, order_data: OrderData) -> OrderResponse:
#         total_cost = Decimal(0)
#         for item in order_data.items:
#             product = self.product_service.get_by_id(item.product_id)
#             item_price = product.price
#             for discount in product.discounts:
#                 if item.discount_code == discount.code:
#                     item_price *= Decimal(1 - discount.rate / 100)
#                     break
#             total_cost += item_price * item.quantity

#         order_response = OrderResponse(
#             customer_name=order_data.customer_name,
#             customer_email=order_data.customer_email,
#             shipping_address=order_data.shipping_address,
#             payment_info=order_data.payment_info,
#             items=order_data.items,
#             total_cost=round(total_cost, 2),
#         )

#         return order_response
