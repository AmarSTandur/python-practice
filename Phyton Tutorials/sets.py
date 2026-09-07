# # s={1,2,3}
# # print(s)
# # s1={29,20,388,26}  #set is unordered
# # print(s1)
# s1={1,2,3,4}
# s2={4,5,6,7}
# print(s1|s2)
# print(s1&s2)
# print(s1-s2)
set1={"apple","banana","grapes"}
set2={"grapes","orange","mango"}
print(set1|set2)
print(set1&set2)
print(set1-set2)
set1.add("kiwi")
print(set1)
set1.remove("apple")
print(set1)

set1.discard("mango")
print(set1)