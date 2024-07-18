CREATE TABLE IF NOT EXISTS countries(
  Country_Code INT PRIMARY KEY,
  Country VARCHAR(50) NOT NULL
);

CREATE TABLE  IF NOT EXISTS restaurants (
    restaurant_id INT PRIMARY KEY,
    restaurant_name VARCHAR(255) NOT NULL,
    country_code INT,
    city VARCHAR(255) NOT NULL,
    address VARCHAR(255) NOT NULL,
    locality VARCHAR(255) NOT NULL,
    locality_verbose VARCHAR(255) NOT NULL,
    longitude DECIMAL(9, 6) NOT NULL,
    latitude DECIMAL(9, 6) NOT NULL,
    cuisines VARCHAR(255) NOT NULL,
    average_cost_for_two DECIMAL(10, 2) NOT NULL,
    currency VARCHAR(50) NOT NULL,
    has_online_delivery BOOLEAN NOT NULL,
    is_delivering_now BOOLEAN NOT NULL,
    switch_to_order_menu BOOLEAN NOT NULL,
    price_range INT NOT NULL,
    aggregate_rating DECIMAL(2, 1) NOT NULL,
    rating_color VARCHAR(50) NOT NULL,
    rating_text VARCHAR(50) NOT NULL,
    votes INT NOT NULL,
    FOREIGN KEY (country_code) REFERENCES countries(country_code)
);

ALTER TABLE restaurants
ADD votes VARCHAR(50);
ADD deeplink VARCHAR(255),
ADD establishment_types TEXT,
ADD events_url VARCHAR(255),
ADD featured_image VARCHAR(255),
ADD has_table_booking BOOLEAN,
ADD zomato_id VARCHAR(255),
ADD menu_url VARCHAR(255),
ADD offers TEXT,
ADD photos_url VARCHAR(255),
ADD thumb VARCHAR(255),
ADD url VARCHAR(255);
ADD votes VARCHAR(50);

ALTER TABLE restaurants
ADD apikey VARCHAR(300),
ADD user_rating DECIMAL(2, 1),
ADD book_url VARCHAR(255);


