from uuid import UUID

import requests
from src.config import settings
from src.model import Product
from src.service.base import BaseGetService


# class ProductService(BaseGetService):
#     def __init__(self, url=settings.PRODUCT_SERVICE_URL) -> None:
#         self.url = url

#     def get_by_id(self, id: UUID):
#         data = self._get(id)

#         return Product(**data)

#     def _get(self, id: UUID):
#         response = requests.get(f"{self.url}/{id}")
#         if response.status_code == 404:
#             raise ValueError(f"Invalid product {id=}")

#         return response.json()
