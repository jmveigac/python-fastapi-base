from models.pizza import Pizza
from services.pizza_service import PizzaService


def test_update_matches_pizza_id() -> None:
    service = PizzaService()
    updated_pizza = Pizza(
        pizza_id=2,
        name="Updated Veggie",
        is_gluten_free=False,
    )

    assert service.update(updated_pizza) is True
    assert service.get(2) == updated_pizza


def test_delete_missing_pizza_returns_false() -> None:
    service = PizzaService()

    assert service.delete(999) is False
