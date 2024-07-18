import csv
from sqlalchemy import create_engine, Table, MetaData, Column, Integer, String, Float, Boolean
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects.mysql import insert

# Replace with your MySQL database connection string
DATABASE_URL = "mysql+pymysql://root:system@localhost:3306/zomato_db"

# Create SQLAlchemy engine and metadata
engine = create_engine(DATABASE_URL)
metadata = MetaData()

# Define 'countries' table
countries = Table(
    'countries', metadata,
    Column('Country_Code', Integer, primary_key=True),
    Column('Country', String(50), nullable=False)
)

# Define 'restaurants' table
restaurants = Table(
    'restaurants', metadata,
    Column('restaurant_id', Integer, primary_key=True),
    Column('restaurant_name', String(255), nullable=False),
    Column('country_code', Integer, nullable=True),  # Foreign key to 'countries' table
    Column('city', String(255), nullable=False),
    Column('address', String(255), nullable=False),
    Column('locality', String(255), nullable=False),
    Column('locality_verbose', String(255), nullable=False),
    Column('longitude', Float, nullable=False),
    Column('latitude', Float, nullable=False),
    Column('cuisines', String(255), nullable=False),
    Column('average_cost_for_two', Float, nullable=False),
    Column('currency', String(10), nullable=False),
    Column('has_online_delivery', Boolean, nullable=False),
    Column('is_delivering_now', Boolean, nullable=False),
    Column('switch_to_order_menu', Boolean, nullable=False),
    Column('price_range', Integer, nullable=False),
    Column('aggregate_rating', Float, nullable=False),
    Column('rating_color', String(50), nullable=False),
    Column('rating_text', String(50), nullable=False),
    Column('votes', Integer, nullable=False),
    Column('deeplink', String(255)),
    Column('establishment_types', String(255)),
    Column('events_url', String(255)),
    Column('featured_image', String(255)),
    Column('has_table_booking', Boolean),
    Column('zomato_id', String(255)),
    Column('menu_url', String(255)),
    Column('offers', String(255)),
    Column('photos_url', String(255)),
    Column('thumb', String(255)),
    Column('url', String(255))
)

# Create tables in the database
metadata.create_all(engine)

# Function to load data from CSV to table
def load_csv_to_table(file_path, table):
    Session = sessionmaker(bind=engine)
    session = Session()
    with open(file_path, mode='r', encoding='ISO-8859-1') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            # Convert data types where necessary
            cleaned_row = {}
            for key, value in row.items():
                if key in ['restaurant_id', 'country_code', 'price_range', 'votes']:
                    cleaned_row[key] = int(value) if value else None
                elif key in ['longitude', 'latitude', 'average_cost_for_two', 'aggregate_rating']:
                    cleaned_row[key] = float(value) if value else None
                elif key in ['has_online_delivery', 'is_delivering_now', 'switch_to_order_menu', 'has_table_booking']:
                    cleaned_row[key] = value.lower() in ['true', '1', 'yes']
                else:
                    cleaned_row[key] = value
            
            # Insert or update the row
            stmt = insert(table).values(**cleaned_row)
            update_dict = {c.name: cleaned_row.get(c.name, None) for c in table.columns if c.name != 'restaurant_id'}
            stmt = stmt.on_duplicate_key_update(**update_dict)
            session.execute(stmt)

        session.commit()
    session.close()

# Load data into 'countries' table
load_csv_to_table('C:/Users/G V Madhuri/Downloads/Desktop/Zomato/countries.csv', countries)

# Load data into 'restaurants' table from CSV
load_csv_to_table('C:/Users/G V Madhuri/Downloads/Desktop/Zomato/restaurants.csv', restaurants)

print("Data successfully loaded into tables.")
