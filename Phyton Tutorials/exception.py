a=int(input("a : "))
b=int(input("b : "))
try:
    print(a/b)
except Exception as e:
    print(f"Error banthu : {e}")
else:
    print("no error")
finally:
   print("End of program")




# try:
#     Boy=input("Who do you want to marry? - ")
#     if Boy.lower()!="amar":
#         raise Exception("You can only marry Amar. Select him!")
# except Exception as e:
#     print(f"Error: {e}")
# else:
#     print("your selection is Good. he is a good guy")
    