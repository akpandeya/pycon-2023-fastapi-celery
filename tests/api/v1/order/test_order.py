from unittest.mock import Mock, patch

from src.main import app
from src.service import EmailService
from src.tasks import send_email_task


class MockEmailService(EmailService):
    ...


def test_create_order(test_client):
    order_data = {
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
    MockEmailService.send_email = Mock(spec=MockEmailService.send_email)

    app.dependency_overrides[EmailService] = MockEmailService

    response = test_client.post("v1/order", json=order_data)
    assert response.status_code == 201

    data = response.json()

    assert data["id"] is None
    MockEmailService.send_email.assert_called_once()
    assert data["total_cost"] == round(34.99 * 2 + 14.99 * 1 * (1 - 0.2), 2)


def test_create_order1(test_client):
    order_data = {
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

    with patch(
        "src.api.v1.order.send_email_task.delay", Mock(spec=send_email_task)
    ) as mocked_send_email_task:
        response = test_client.post("v1/order", json=order_data)
        assert response.status_code == 201

        data = response.json()

        assert data["id"] is not None
        mocked_send_email_task.assert_called_once()
        assert data["total_cost"] == round(34.99 * 2 + 14.99 * 1 * (1 - 0.2), 2)
