# class Animal:
#     def make_sound(self):
#         print("Animal is making sound")

# class Dog(Animal):
#     def make_sound(self):
#         print("Bark")

# class Cat(Animal):
#     def make_sound(self):
#         print("Meow")

# animals = [Dog(), Cat(),Animal()]
# for animal in animals:
#     animal.make_sound()






class Notification:
    def send(self):
        print("Some notification sent")
class EmailNotification(Notification):
    def send(self):
        print("Email sent")
class SMSNotification(Notification):
    def send(self):
        print("SMS sent")

a1=[EmailNotification(),SMSNotification(),Notification()]
for a in a1:
    a.send()