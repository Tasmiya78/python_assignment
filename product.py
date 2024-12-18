'''WAP to create dictionaries for below task
and perform all the above operation on below
 each product in a supermarkset is associated with its price.'''

supermarket={
    "product":"maggie",
    "price":50
    }

print(supermarket)
print(type(supermarket))#to check type

x=supermarket["product"]#storing product in x
print("product is",x)#printing product

x=supermarket.get("price")
print("product price is ",x)#printing price

#find all the keys present in the dictionary
y=supermarket.keys()
print("the keys present are:",y)

supermarket.update({"price":20})#to update
print(supermarket)


supermarket["Tax"]="2%"#adding new dictionary
print(supermarket)

#to remove certain element from the dictionary
supermarket.popitem()
print(supermarket)

#looping over dictionary
for i in supermarket:
    print(i)
    
#to get keys from the dictionary
for i in supermarket.values():
    print(i)

for x,y in supermarket.items():
    print(x,y)
    
#to remove an item at specified index.
supermarket.pop("product")
print(supermarket)












