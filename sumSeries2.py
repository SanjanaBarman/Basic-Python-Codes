'''Write a Python program to sum the sequence: 1 + 1/1! + 1/2! + 1/3! +........+ 1/n!
(Input n through keyboard)'''


def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f   
n=int(input("Enter the value of n:"))
s=1
for i in range(1,n+1):
    c=1/fact(i)
    s=s+c

print("Sum of the series is:",s)
    


'''Enter the value of n:5
Sum of the series is: 2.7166666666666663'''