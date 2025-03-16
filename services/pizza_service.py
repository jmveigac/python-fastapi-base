from models.pizza import Pizza


class PizzaService:
    pizzas = [
        Pizza(pizza_id=1, name="Classic Italian", is_gluten_free=False),
        Pizza(pizza_id=2, name="Veggie", is_gluten_free=True),
    ]
    next_id = 3

    @staticmethod
    def get_all():
        return PizzaService.pizzas

    @staticmethod
    def get(pizza_id):
        return next(
            (pizza for pizza in PizzaService.pizzas if pizza.pizza_id == pizza_id), None
        )

    @staticmethod
    def add(pizza_input):
        pizza_input.pizza_id = PizzaService.next_id
        PizzaService.next_id += 1
        PizzaService.pizzas.append(pizza_input)
        return pizza_input

    @staticmethod
    def delete(pizza_id):
        pizza_delete = PizzaService.get(pizza_id)
        if pizza_delete:
            PizzaService.pizzas.remove(pizza_delete)
            return True

    @staticmethod
    def update(updated_pizza):
        index = next(
            (
                i
                for i, pizza in enumerate(PizzaService.pizzas)
                if pizza.pizza_id == updated_pizza.id
            ),
            -1,
        )
        if index != -1:
            PizzaService.pizzas[index] = updated_pizza
            return True
        return False
