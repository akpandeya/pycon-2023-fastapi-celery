import pytest
from fastapi.testclient import TestClient
from src.main import app


@pytest.fixture(scope="session")
def test_client():
    return TestClient(app)


@pytest.fixture
def mock_order_data():
    return {
        "customer_name": "John Smith",
        "customer_email": "john.smith@example.com",
        "shipping_address": "123 Main St, Anytown USA",
        "payment_info": "4242 4242 4242 4242",
        "items": [
            {
                "product_id": "5c5a5a52-58e3-48a5-85a5-31942c0e1918",
                "quantity": 2,
                "discount_code": None,
            },
            {
                "product_id": "b0d6dd8f-15e1-4a13-831c-4a9d1a4c4e4f",
                "quantity": 1,
                "discount_code": "SAUSAGE20",
            },
        ],
    }
