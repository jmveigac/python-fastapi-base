from pydantic import BaseModel


class Pizza(BaseModel):
    pizza_id: int
    name: str
    is_gluten_free: bool
