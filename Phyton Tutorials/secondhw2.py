# #arithematic
# a=8
# b=5
# print(a+b)
# print(a-b)
# print(a*b)
# print(a**b)
# print(a/b)
# print(a//b)
# print(a%b)

# #swaping
# a,b=12,19
# print(f"a: {a} , b: {b}")

# a,b=b,a
# print(f"a: {a} , b: {b}")



# dict={
#     "bengalur":"bisibelebath",
#     "mysore":"sweet",
#     "mandy":"vada",
#     "davangere":"dosa"

# }
# print(dict)
# dict["hasan"]="idili"
# print(dict)
# dict["bengalur"]="uta"
# print(dict)
# del dict["mysore"]
# print(dict)
# print(dict.keys())
# print(dict.values())







# d={
#     "friend1":{
#         "name":"amar",
#         "fav_sub":"maths",
#         "fav_food":"biriyani"
#     },
#     "friend2":{
#         "name":"adarsh",
#         "fav_sub":"science",
#         "fav_food":"rice"
#     }
# }
# f=(d["friend1"])
# print(f["fav_food"])
# print(d["friend1"]["fav_food"])



# i=1
# while(i<=20):
#     i+=1
#     if i%2!=0:
#         print(i)



# seats=8
# while seats>0:
#     book=input("Enter b to book seat: ")
#     book.lower()
#     if book=='b':
#         seats-=1
#         print("Seat is bookes")
#         print("avaliable seats:",seats)
#     print("seats are full")



# import time
# i=10
# while i>0:
#     i-=1 
#     print(i)
#     time.sleep(1)
# print("happy new year")





# vowels="aeiou"
# count=0
# letter=input("Enter a letter: ")
# l=letter.lower()
# for i in l:
#     if i in vowels:
#         count+=1
# print(count)





# foods=["idli","dosa","vada"]
# u_food=[ item.upper() for item in foods]
# print(u_food)



# items={
#     "pen":10,
#     "book":20,
#     "pencial":24,
# }
# total=0
# for key,value in items.items():
#     total+=value
# print(total)





# items={
#     "pen":10,
#     "book":20,
#     "pencial":24,
# }
# total=0
# print(sum(list(items.values())))




# l=[num**2 for num in range(1,11)]
# print(l)



# l=[
#     {
#     "name":"amar",
#     "marks":23
# },
# {
#     "name":"adarsh",
#     "marks":24

# }
# ]
# for student in l:
#     print(student["name"], "-" ,student["marks"])







rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = []

for i in range(rows):
    row = []
    for j in range(cols):
        x = int(input("Enter an element: "))
        row.append(x)
    matrix.append(row)

print(matrix)     

