n=int(input("Enter the number:"))

rev=0
rem=0
while(n>0):
    rem=n%10
    rev=(rev*10)+rem
    n=n//10

print("The reverse number is:",rev)
if(rev%2==0):
    print(rev,"is an Even Number")
else:
    print(rev,"is a Odd Number")