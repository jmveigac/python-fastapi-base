from collections.abc import Iterable

from models.pizza import Pizza, PizzaCreate


DEFAULT_PIZZAS = (
    Pizza(pizza_id=1, name="Classic Italian", is_gluten_free=False),
    Pizza(pizza_id=2, name="Veggie", is_gluten_free=True),
)


class PizzaService:
    def __init__(self, pizzas: Iterable[Pizza] | None = None) -> None:
        self._pizzas = list(DEFAULT_PIZZAS if pizzas is None else pizzas)
        self._next_id = max((pizza.pizza_id for pizza in self._pizzas), default=0) + 1

    def get_all(self) -> list[Pizza]:
        return list(self._pizzas)

    def get(self, pizza_id: int) -> Pizza | None:
        return next(
            (pizza for pizza in self._pizzas if pizza.pizza_id == pizza_id), None
        )

    def add(self, pizza_input: PizzaCreate) -> Pizza:
        pizza = Pizza(pizza_id=self._next_id, **pizza_input.model_dump())
        self._next_id += 1
        self._pizzas.append(pizza)
        return pizza

    def delete(self, pizza_id: int) -> bool:
        for index, pizza in enumerate(self._pizzas):
            if pizza.pizza_id == pizza_id:
                del self._pizzas[index]
                return True
        return False

    def update(self, updated_pizza: Pizza) -> bool:
        for index, pizza in enumerate(self._pizzas):
            if pizza.pizza_id == updated_pizza.pizza_id:
                self._pizzas[index] = updated_pizza
                return True
        return False
