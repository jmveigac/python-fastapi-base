from fastapi import FastAPI, HTTPException, status

from models.pizza import Pizza, PizzaCreate
from services.pizza_service import PizzaService


def create_app(service: PizzaService | None = None) -> FastAPI:
    app = FastAPI(title="Python FastAPI Base")
    pizza_service = service or PizzaService()

    @app.get("/", response_model=list[Pizza])
    async def get_all() -> list[Pizza]:
        return pizza_service.get_all()

    @app.get("/{pizza_id}", response_model=Pizza)
    async def get(pizza_id: int) -> Pizza:
        pizza = pizza_service.get(pizza_id)
        if pizza is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Not Found."
            )
        return pizza

    @app.post("/", response_model=Pizza, status_code=status.HTTP_201_CREATED)
    async def create(pizza_input: PizzaCreate) -> Pizza:
        return pizza_service.add(pizza_input)

    @app.put("/", response_model=Pizza)
    async def update(pizza_input: Pizza) -> Pizza:
        if pizza_service.update(pizza_input):
            return pizza_input
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found.")

    @app.delete("/{pizza_id}")
    async def delete(pizza_id: int) -> dict[str, str]:
        if pizza_service.delete(pizza_id):
            return {"message": "Deleted"}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found.")

    return app


app = create_app()
