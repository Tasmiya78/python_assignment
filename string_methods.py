#methods related to string
text="helloWorld"
text_upper=text.upper()

print("The data is upper case is",text_upper)

text_lower=text.lower()
print("The data is lower case is",text_lower)

name="   teenaDatta"
newname=name.strip()
print("the data without space is",newname)

lspace=name.lstrip()
print("the data without space is",lspace)

rspace=name.strip()
print("the data without space is",rspace)

#str.replace(old,new):this methods replace all occurance
#of the "old"substring with the new:
sentence="I like apple and I like mango"
new_sentence=sentence.replace("like","love")
print("before replacing",sentence)
print("after replacing ",new_sentence)

#str.split(sep=None,maxsplit=-1)
#this method splits a string into a list of substring
#we can also specify the maximum number of splits with maxspliy
sentences="python programming is fun"
words=sentences.split()
print(words)







