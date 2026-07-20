from pydantic import BaseModel, ConfigDict, Field


class PizzaCreate(BaseModel):
    name: str = Field(min_length=1)
    is_gluten_free: bool


class Pizza(PizzaCreate):
    model_config = ConfigDict(frozen=True)

    pizza_id: int = Field(gt=0)
