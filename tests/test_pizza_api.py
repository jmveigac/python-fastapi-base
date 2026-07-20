import pytest
from fastapi.testclient import TestClient

from main import create_app
from services.pizza_service import PizzaService


@pytest.fixture
def client() -> TestClient:
    return TestClient(create_app(PizzaService()))


def test_pizza_crud_flow(client: TestClient) -> None:
    list_response = client.get("/")
    assert list_response.status_code == 200
    assert len(list_response.json()) == 2

    create_response = client.post(
        "/",
        json={"name": "Margherita", "is_gluten_free": False},
    )
    assert create_response.status_code == 201
    created_pizza = create_response.json()
    assert created_pizza == {
        "name": "Margherita",
        "is_gluten_free": False,
        "pizza_id": 3,
    }

    get_response = client.get("/3")
    assert get_response.status_code == 200
    assert get_response.json() == created_pizza

    updated_pizza = {
        "pizza_id": 3,
        "name": "Updated Margherita",
        "is_gluten_free": True,
    }
    update_response = client.put("/", json=updated_pizza)
    assert update_response.status_code == 200
    assert update_response.json() == updated_pizza
    assert client.get("/3").json() == updated_pizza

    delete_response = client.delete("/3")
    assert delete_response.status_code == 200
    assert delete_response.json() == {"message": "Deleted"}
    assert client.get("/3").status_code == 404


def test_missing_pizza_operations_return_404(client: TestClient) -> None:
    missing_pizza = {
        "pizza_id": 999,
        "name": "Missing",
        "is_gluten_free": False,
    }

    assert client.get("/999").status_code == 404
    assert client.put("/", json=missing_pizza).status_code == 404
    assert client.delete("/999").status_code == 404
