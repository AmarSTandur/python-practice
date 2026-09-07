class Car:
    def __init__(self,car_id,name,year,price_per_day,status="avaliable",rented_days=0):
        self.car_id=car_id
        self.name=name 
        self.year=year
        self.price_per_day=price_per_day
        self.status=status
        self.rented_days=rented_days

    def display_details(self):
        print(f"car_id: {self.car_id},Name: {self.name}, Year: {self.year}, Status: {self.status}, Price per day: {self.price_per_day}, Rented days: {self.rented_days}")

    def update_status(self,new_status):
        self.status=new_status
        print(f"Car ID {self.car_id} status updated to {new_status}.")
    def calculate_rental_price(self):   
        total_price=self.price_per_day*self.rented_days
        print(f"Total rental price for Car ID {self.car_id} is: ${total_price}")

car1=Car(1,"Swift",2019,50)
car2=Car(2,"Baleno",2020,60,"rented",3)
car3=Car(3,"Mustang",2021,70)

car1.display_details()
car2.display_details()
car2.calculate_rental_price()
car2.update_status("avaliable")
    




#if i want to add this all attribute to anothe class means for electric car beu it contain extra so we first inherit this attibute to that class by ElcerticCar(car) by this we can inherit properties of car class to electric car class and then we can add extra properties to that class.