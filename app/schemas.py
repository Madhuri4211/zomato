from pydantic import BaseModel
from typing import List

class RestaurantBase(BaseModel):
    restaurant_name: str
    restaurant_id: int
    featured_image: str

class Restaurant(RestaurantBase):
    menu_url: str  # Include menu_url here for detailed view

    class Config:
        orm_mode = True

class RestaurantList(BaseModel):
    total: int
    items: List[RestaurantBase]  # Change to RestaurantBase to include only required fields