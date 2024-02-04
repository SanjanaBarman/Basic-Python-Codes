p=float(input("Enter  the amount of principal:"))
r=float(input("Enter thge rate of interest:"))
t=float(input("Enter the time period:"))

si=(p*t*r)/100
print("The simple interest is:",si)

ci=p * ((1 + r/100)**t - 1)
print("The Compound Interest is",ci)