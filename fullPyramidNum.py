# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 00:13:39 2024

@author: SANJANA BARMAN
"""

r=int(input("Enter the number of rows:"))
k=0
x=1
for i in range(1,r+1):
    for j in range(1,(r-i)+1):
        print( end="    ")
        
    x = 1
    while k!= (2*i-1):
        k=k+1
        print(x,"  ", end="")
        x=x+1
    k=0
    print()
    
    
    
    
'''Enter the number of rows:5
                1   
            1   2   3   
        1   2   3   4   5   
    1   2   3   4   5   6   7   
1   2   3   4   5   6   7   8   9   '''