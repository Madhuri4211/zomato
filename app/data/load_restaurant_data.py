import json
import mysql.connector

try:
    # Connect to MySQL database
    db_connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="system",
        database="zomato_db"
    )
    
    # Read and parse JSON file
    with open('file5.json', 'r') as json_file:
        data = json.load(json_file)

    cursor = db_connection.cursor()

    # Iterate through each restaurant in the JSON data
    for item in data:
        restaurants = item.get('restaurants', [])
        for restaurant_data in restaurants:
            restaurant = restaurant_data.get('restaurant', {})
            res_id = restaurant['R']['res_id']
            name = restaurant.get('name', '')
            cuisines = restaurant.get('cuisines', '')
            is_delivering_now = restaurant.get('is_delivering_now', 0)
            deeplink = restaurant.get('deeplink', '')
            menu_url = restaurant.get('menu_url', '')
            photos_url = restaurant.get('photos_url', '')
            url = restaurant.get('url', '')
            apikey = restaurant.get('apikey', '')
            price_range = restaurant.get('price_range', 0)
            featured_image = restaurant.get('featured_image', '')

            # Check if res_id exists in your MySQL restaurants table
            cursor.execute("SELECT restaurant_id FROM restaurants WHERE restaurant_id = %s", (res_id,))
            existing_record = cursor.fetchone()
            if existing_record:
                restaurant_id = existing_record[0]

                # If res_id exists, update existing record in restaurants table
                cursor.execute("""
                    UPDATE restaurants
                    SET cuisines = %s,
                        is_delivering_now = %s,
                        deeplink = %s,
                        menu_url = %s,
                        photos_url = %s,
                        url = %s,
                        apikey = %s,
                        price_range = %s,
                        featured_image = %s
                    WHERE restaurant_id = %s
                """, (
                    cuisines,
                    is_delivering_now,
                    deeplink,
                    menu_url,
                    photos_url,
                    url,
                    apikey,
                    price_range,
                    featured_image,
                    restaurant_id
                ))
                db_connection.commit()
                print(f"Updated data for restaurant with restaurant_id: {restaurant_id} (res_id: {res_id})")
            else:
                print(f"Restaurant with res_id {res_id} not found in database")

    # Close cursor and database connection
    cursor.close()
    db_connection.close()

except Exception as e:
    print(f"Error: {str(e)}")
