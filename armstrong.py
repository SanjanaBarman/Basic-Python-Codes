n=int(input("Enter the number to check Armstrong number:"))
rev=0
s = 0
rem = n
l=len(str(n))
while (n>0):
    rev=n%10
    s= s+pow(rev,l)
    n=n//10
if rem==s:
    print(rem, " is ARMSTRONG")
else:
    print(rem, " is NOT ARMSTRONG")
    
    
    """
    Enter the number to check Armstrong number:153
    153  is ARMSTRONG
    
    Enter the number to check Armstrong number:7
    7  is ARMSTRONG
    
    Enter the number to check Armstrong number:52
    52  is NOT ARMSTRONG
    """