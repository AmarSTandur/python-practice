class Human:
    def __init__(self,name):
        self.name=name
    def walk(self):
        print(f"{self.name} is walking.")

human1=Human("Alice")
human1.walk()
h1=Human("Bob")
h1.walk()