''' A dictionary is a built _in data structure in python
that allows you to store a collection of key_value pairs

dictionary is mutable and its is unorderd
'''
my_dict={
    "std_id":123,
    "std_name":"sameera",
    "course":"BCA"
    }
print(my_dict)
x=my_dict["course"]

print("the course selected is",x)

x=my_dict.get("std_id")
print(x)

#find all the keys present in the dictionary
y=my_dict.keys()
print("the keys present are:",y)

my_dict.update({"std_name":"tasmiya"})#to update
print(my_dict)


my_dict["address"]="mumbra"#adding new dictionary
print(my_dict)

#to remove certain element from the dictionary
my_dict.popitem()
print(my_dict)

#looping over dictionary
for i in my_dict:
    print(i)
#to get keys from the dictionary
for i in my_dict.values():
    print(i)

for x,y in my_dict.items():
    print(x,y)

my_dict.pop("std_name")
print(my_dict)






    
    




    





