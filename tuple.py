'''t1=("Aditya",78,"O grade",35)
print(type(t1))
print(t1)

#TUPLE SLICING
print(t1[1:])
print(t1[:3])
print(t1[1:3])

#FIND LENGTH OF THE TUPLE
print("The length of the tuple is",len(t1))

#you can also give negative indexing.
print(t1[-2])
print(t1[-1])

#note:
t2=list(t1)
print(t2)

t2[2]="A in sports"
print(t2)

for i in t2:
    print(i)'''


#WAP to reverse the given tuple
tup1=(56,78,34,55,66)
print("the original tuple is",tup1)
res=(tup1[::-1])
print("The reverse order is")
print(res)

#WAP to print even numbers in tuple
for i in tup1:
    if i%2==0:
        print(i)

tup2=(45,[34,89],80,40,73)
print(tup2[0])
print(tup2[1])
print(tup2[1][0])
print(tup2[1][1])

tup2[1][0]=45
print(tup2)

#WAP to count the 45 in th tuple
print("the 45 occurs",tup2.count(45),"times")
'''tuple can not be changed
tup[2]=78
print(tup2]'''

#WAP to create tuple with different
my_tuple=("Maggie",3,15.5,True)
print("I want to eat maggie",my_tuple)

marks=23,67,87,34
print("I have got marks as")
print(marks)

#WAP to create tuple with single item
price=34,
print(price)
















