s=input("Enter a string:")
u=0
l=0
s.strip()
for i in s:
    if i>='A' and i<='Z':
        u=u+1
    elif i>='a' and i<='z':
        l=l+1
print("the number of total lower case is" ,l)
print("the number of total upper case is" ,u)





'''Enter a string:My Name Is Sanjana Barman
the number of total lower case is 16
the number of total upper case is 5'''