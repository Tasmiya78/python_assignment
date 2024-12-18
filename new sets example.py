'''sports1={"sanoj","neha","Dev","Raj","sweta","hiral"}
sports2={"neha","sweta","hiral","arjun","ram"}

#find total participants in the sports list
Total_Ath=sports1|sports2
print("Toatl participants",Total_Ath)

for s in Total_Ath:
    print(s)

#set Difference
New_sports=sports1-sports2
print("The new sports one list is ",New_sports)'''

#WAP to accept different email ids of customer(repeat atleast three in list
#try to print unique emails
cust_Emails=["tas@123","snehal@123","kajal@123","neha@123","sanju@123",
             "tas@123","snehal@123","kajal@123"]

print(cust_Emails)

unique_Email=set(cust_Emails)
print("The unique data is",unique_Email)

new_emails={"enna123","tassu123","neha@123","sanju@123",}
update=new_emails-unique_Email

print("new customer are",update)







