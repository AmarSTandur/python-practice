cars={
    1:{"name":"Swift","year":2019,"status":"avaliable","price_per_day":50,"rented_days":0},
    2:{"name":"Baleno","year":2020,"status":"rented","price_per_day":60,"rented_days":3},
    3:{"name":"Mustang","year":2021,"status":"avaliable","price_per_day":70,"rented_days":0},
}

def display_car_details(car_id):
    car=cars.get(car_id)
    if car:
        print(f"car_id: {car_id},Name: {car['name']}, Year: {car['year']}, Status: {car['status']}, Price per day: {car['price_per_day']}, Rented days: {car['rented_days']}")
    else:
        print("Car not found.")

def update_car_status(car_id, new_status):
    if car_id in cars:
        cars[car_id]['status'] = new_status
        print(f"Car ID {car_id} status updated to {new_status}.")
    else:
        print("Car not found.")

def calculate_rental_price(car_id):
    car=cars.get(car_id)
    if car:
        total_price=car['price_per_day']*car['rented_days']
        print(f"Total rental price for Car ID {car_id} is: ${total_price}")
    else:
        print("Car not found.")

display_car_details(2)
calculate_rental_price(2)
update_car_status(2, "avaliable")
display_car_details(2)
    