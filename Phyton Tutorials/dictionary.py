# birthday={"amar":"07-07-2005","adarsh":"07-04-2007","virat":"05-10-1988",}
# num={"a":"1","b":"2","c":"3","d":"4",}
# print(type(birthday))
# print(birthday["adarsh"])
# print(birthday["amar"])
# print(birthday["virat"])
# print(birthday.get("amar","not found"))
# print(birthday.get("sudeep","not found"))
# #get() is used for safe access in program to avoide crash 
# birthday["ajay"]="07-08-2006"
# print(birthday)
# birthday["ajay"]="07-09-2006"
# print(birthday)
# x=birthday.pop("ajay")
# print(birthday)
# print(x)
# del birthday["virat"]
# print(birthday)
# print(birthday.keys())
# print(birthday.values())
# print(birthday.items())
# print(num)
# birthday.update(num)
# print(birthday)
# print(num)




item1={"name":"milk",
       "weight":1,
       "price": 45
       }

item2={"name":"sugar",
       "weight":2,
       "price": 60
       }
items=[item1,item2]
print(items)
print(f"Total Weight:{item1['weight']+item2['weight']}")
