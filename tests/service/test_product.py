from uuid import UUID

import pytest
from src.model import Discount, Product
from src.service import ProductService


# def test_get_valid_product(product_service_url):
#     product_service = ProductService(url=product_service_url)

#     id = UUID("9d4f4aa2-4efb-4be6-8e99-294e9730a7b1")

#     product = product_service.get_by_id(id)
#     assert isinstance(product, Product)
#     assert product.id == id

#     for discount in product.discounts:
#         assert isinstance(discount, Discount)


# def test_get_invalid_product(product_service_url):
#     product_service = ProductService(url=product_service_url)
#     with pytest.raises(ValueError) as e:
#         product_service.get_by_id("invalid_id")
#     assert "Invalid product id" in str(e.value)
