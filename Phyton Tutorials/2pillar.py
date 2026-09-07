class Database:
    def __init__(self):
        self.__storage = {} #private attribute

    def write(self, key, value):
        self.__storage[key] = value
    def read(self, key):
        if key in self.__storage:
            print(self.__storage[key])
        else:
            print("DB item not avaliable")
    

db=Database()
db.write("Amar", "Data for Amar")
db.write("Raj", "Data for Raj")
db.write("Ravi", "Data for Ravi")
db.read("Raj")
db.read("Raj")
db.read("ccc")


