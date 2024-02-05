'''Write programs to find the sum of the following series:
x - x^2 /2! + x^3 /3! - x^4 /4! + x^5 /5! - x^6 /6! (Input x)'''

def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f
        


x=int(input("Enter the value of x:"))
s=x
for i in range(2,7):
    c=pow(x,i)/fact(i)
    if i%2==0:
        s=s-c
    else:
        s=s+c

print("sum of the following series:",s)


'''Enter the value of x:5
sum of the following series: -8.368055555555557'''
