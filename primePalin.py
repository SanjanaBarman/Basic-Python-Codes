def isPrime(n):
    f=0
    if f==2:
        return 1
    for i in range(2,n):
        if n%i==0:
            f=1
            return 0
            break
    if f==0:
        return 1
    
def isPalin(n):
    rev = 0
    new = n 
    while(n>0):
        rem=n%10
        rev=(rev*10)+rem
        n=n//10
    if rev==new:
        return 1
    else:
        return 0

l=int(input("Enter the starting range:"))
h=int(input("Enter the ending range:"))
print("Prime Palindrome Numbers in this range are : ")
for i in range(l , h+1):
    if (isPrime(i)==1) and (isPalin(i)==1):
        print(i)
        
        
'''
Enter the starting range:10
Enter the ending range:1000
Prime Palindrome Numbers in this range are : 
11
101
131
151
181
191
313
353
373
383
727
757
787
797
919
929
'''
        