from fastapi import FastAPI, HTTPException
from models.pizza import Pizza
from services.pizza_service import PizzaService

app = FastAPI()


@app.get("/")
async def get_all():
    return PizzaService.get_all()


@app.get("/{pizza_id}")
async def get(pizza_id: int):
    pizza = PizzaService.get(pizza_id)
    if not pizza:
        raise HTTPException(status_code=404, detail="Not Found.")
    return pizza


@app.post("/")
async def create(pizza_input: Pizza):
    PizzaService.add(pizza_input)
    return {"message": "Created"}


@app.put("/")
async def update(pizza_input: Pizza):
    if PizzaService.update(pizza_input):
        return {"message": "Updated"}
    raise HTTPException(status_code=404, detail="Not Found.")


@app.delete("/{pizza_id}")
async def delete(pizza_id: int):
    if PizzaService.delete(pizza_id):
        return {"message": "Deleted"}
    raise HTTPException(status_code=404, detail="Not Found.")
