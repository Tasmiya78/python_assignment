'''A set in python programming is an unorderd collection data types
that is iterable and has no duplicate elements.while sets are mutable,
meaning you can add or remove elements after their creation.
'''
set_a={5,6,67,3}
print(set_a)

set_b={6,9,5,6}#set does not allow duplicate value.
print(set_b)

set_c={7,9,78,4}
print(set_c)

#set union operation
set_d=set_a.union(set_b)
print("the union of both the sets are:",set_d)

set_e=set_a.union(set_b,set_c)
print("the union of all the sets are",set_e)

#using union operator|
result=set_a|set_b|set_c
print("the union of all is",result)

print(type(set_a))

#WAP to find intersection of two sets using intersection()function
set_f=set_a.intersection(set_b)
print(set_f)

#WAP to find intersection of two sets using()function and & operator.
result=set_a&set_b
print(result)

#set difference(-)
result=set_a-set_b
print(result)

#set difference using difference()method
result=set_a.difference(set_b)
print(result)

#WAP to get symmetric_difference(elements which are not in both the sets)
result=set_a^set_b
print("The symmetric difference is",result)







