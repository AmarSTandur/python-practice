# def DivExp(a,b):
#     assert a>0,"a must be greater than 0"
#     if b==0:
#         raise ZeroDivisionError("Division by zero is not allowed")
#     return a/b
# try:
#     a=int(input("enter the value of a: "))
#     b=int(input("enter the value of b: "))
#     result=DivExp(a,b)
#     print(f"{result:.2f}")
# except AssertionError as ae:
#     print(ae)
# except ZeroDivisionError:
#     print("Division by zero is not allowed")
    

import string
sample=input()
with open(sample,'r') as file:
    text=file.read()
words=text.split()
word_freq={}
for  word in words:
    if word in word_freq:
        word_freq[word]+=1
    else:
        word_freq[word]=1
sorted_word=sorted(word_freq.items(),key=lambda item: item[1],reverse=True)
for word,freq in sorted_word[:10]:
    print(f"{word}-{freq} times")
    