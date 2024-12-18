#list is a collection which is ordered and changable.
#Allows duplicate members.
my_list=["soap","oil","tea","23","rice"]
print(my_list)

for i in my_list:
    print(i)

my_list.append("maggie")
print(my_list)

#list element is recognized by its index valus
#first element my_list[0]
print(my_list[0])

#there is concept of negative indexing
print(my_list[1::4])
print(my_list[:])
print(my_list[2:])
print(my_list[:5])
print(my_list[::-1])

marks=[34,56,23,89,54]
print(min(marks))

print("the maximum value is ",max (marks))
#WAP to find second largest element

for i in range(0,5):
    for j in range(i+1,5):
        
        if marks[j]>marks[i]:
           temp=marks[i]
           marks[i]=marks[j]
           marks[j]=temp
print(marks)
print(marks[1])






