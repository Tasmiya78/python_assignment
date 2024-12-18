'''To present list in concise and easy way we List Comprehension.
As size of the code is less,performance will be increased
'''
marks=[20,35,50,78,40]
new_marks=[]
for x in marks:
    new_marks.append(x+2)
print(new_marks)

#code using list

marks=[20,35,50,78,40]
new_marks=[x+2 for x in marks]
print(new_marks)

'''Q2) find cube of even numbers'''
cubes=[]
for x in range(11):
    if x%2==0:
        cubes



