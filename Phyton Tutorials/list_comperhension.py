# l=[1,2,3,4,5]
# #dl=[exp for item in collection]
# dl=[num*34355 for num in l]
# print(dl)






# l=[x for x in range(1,10)]
# dl=[x**2 for x in l]
# print(dl)



# #Syntax:[exp for item in collection if condition]
# l=[x for x in range(1,10)]
# Evendl=[x**2 for x in l if x%2==0]
# print(l)
# print(Evendl)



# l=["amar","adarsh","ajay"]
# print(l)
# cl=[x[1] for x in l]
# print(cl)



# names=["amar","adarsh","ajay"]
# d={}
# d={name:len(name) for name in names }
# print(d) 


# city_population= {
#     "Bengaluru": 84,
#     "Mysuru": 11,
#     "Hubballi": 9,
#     "Mangaluru": 5
# }
# large_city={city:population for city,population in city_population.items() if population>10}
# print(large_city)





# s="this is a computer"
# l=s.split()
# print(l)



s="this-is-a-computer"
l=s.split("-")
print(l)