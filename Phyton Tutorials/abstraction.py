# class Car:
#     def start_engine(self):
#         print("Engine started")

#     def accelerate(self):
#         print("Car accelerating")

#     def brake(self):
#         print("Car stopping")

# car = Car()
# car.start_engine()  # Abstracts complex internal workings
# car.accelerate()
# car.brake()

# bike=Car()
# bike.start_engine()
# bike.accelerate()
# bike.brake()



# class Database:
#     def __init__(self):
#         self.__storage = {}

#     def save_data(self, key, value):
#         self.__storage[key] = value
#         print(f"Data saved for {key}")

#     def get_data(self, key):
#         return self.__storage.get(key, "No data found")

# db = Database()
# db.save_data("user_101", {"name": "Raj", "age": 30})
# print(db.get_data("user_101"))

# bc=Database()
# bc.save_data("user_143",{"name":"Amar","age":21})
# print(bc.get_data("user_143"))






class Phone:
    def call_contact(self, contact_name):
        print(f"Calling {contact_name}...")

    def take_picture(self):
        print("Picture captured successfully!")

# Creating an object
my_phone = Phone()

# Using the user-friendly interface
my_phone.call_contact("Amar")
my_phone.take_picture()
