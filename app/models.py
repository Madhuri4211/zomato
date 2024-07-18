from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Country(Base):
    __tablename__ = "countries"

    Country_Code = Column(Integer, primary_key=True, index=True)
    Country = Column(String(50), nullable=False)

class Restaurant(Base):
    __tablename__ = "restaurants"

    restaurant_id = Column(Integer, primary_key=True, index=True)
    restaurant_name = Column(String(255), nullable=False)
    country_code = Column(Integer, ForeignKey('countries.Country_Code'))
    city = Column(String(255), nullable=False)
    address = Column(String(255), nullable=False)
    locality = Column(String(255), nullable=False)
    locality_verbose = Column(String(255), nullable=False)
    longitude = Column(Float, nullable=False)
    latitude = Column(Float, nullable=False)
    cuisines = Column(String(255), nullable=False)
    average_cost_for_two = Column(Float, nullable=False)
    currency = Column(String(50), nullable=False)
    has_online_delivery = Column(Boolean, nullable=False)
    is_delivering_now = Column(Boolean, nullable=False)
    switch_to_order_menu = Column(Boolean, nullable=False)
    price_range = Column(Integer, nullable=False)
    aggregate_rating = Column(Float, nullable=False)
    rating_color = Column(String(50), nullable=False)
    rating_text = Column(String(50), nullable=False)
    votes = Column(Integer, nullable=False)
    deeplink = Column(String(255))
    establishment_types = Column(String(255))
    events_url = Column(String(255))
    featured_image = Column(String(255))
    has_table_booking = Column(Boolean)
    zomato_id = Column(String(255))
    menu_url = Column(String(255))  # Include menu_url
    offers = Column(String(255))
    photos_url = Column(String(255))
    thumb = Column(String(255))
    url = Column(String(255))
    apikey = Column(String(300))
    user_rating = Column(Float)
    book_url = Column(String(255))
