from sqlalchemy.orm import Session
from app.models import Restaurant
from app.schemas import RestaurantBase

def get_restaurant(db: Session, restaurant_id: int):
    return db.query(Restaurant).filter(Restaurant.restaurant_id == restaurant_id).first()

def get_restaurants(db: Session, skip: int = 0, limit: int = 100):
    restaurants = db.query(Restaurant).offset(skip).limit(limit).all()
    return [
        RestaurantBase(
            restaurant_name=r.restaurant_name,
            restaurant_id=r.restaurant_id,
            featured_image=r.featured_image  # Include featured_image
        ) for r in restaurants
    ]

def get_restaurants_count(db: Session):
    return db.query(Restaurant).count()