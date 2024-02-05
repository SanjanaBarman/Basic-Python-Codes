r=int(input("Enter the number of rows:"))
k=0
for i in range(1,r+1):
    for j in range(1,(r-i)+1):
        print( end="    ")
        

    while k!= (2*i-1):
        k=k+1
        print("*  ", end=" ")
    k=0
    print()  
    
    
    
'''Enter the number of rows:5
                *   
            *   *   *   
        *   *   *   *   *   
    *   *   *   *   *   *   *   
*   *   *   *   *   *   *   *   *   '''