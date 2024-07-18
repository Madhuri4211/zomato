from fastapi import FastAPI, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from app import crud, models, schemas
from app.database import SessionLocal, engine
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

# Set up templates directory
templates = Jinja2Templates(directory="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],  # Replace with your frontend URL
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

# Dependency to get the DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/restaurants", response_model=schemas.RestaurantList)
def read_restaurants(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    restaurants = crud.get_restaurants(db, skip=skip, limit=limit)
    total = crud.get_restaurants_count(db)
    return schemas.RestaurantList(total=total, items=restaurants)

@app.get("/restaurants/{restaurant_id}", response_model=schemas.Restaurant)
def read_restaurant(restaurant_id: int, db: Session = Depends(get_db)):
    restaurant = crud.get_restaurant(db, restaurant_id=restaurant_id)
    if restaurant is None:
        raise HTTPException(status_code=404, detail="Restaurant not found")
    return restaurant

@app.get("/", response_class=HTMLResponse)
async def read_restaurants(request: Request):
    db: Session = SessionLocal()
    restaurants = crud.get_restaurants(db)
    return templates.TemplateResponse("index.html", {"request": request, "restaurants": restaurants})