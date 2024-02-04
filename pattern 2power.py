import math
row=int(input("Enter the number of row:"))
for i in range(0,row):
    for j in range(i,0-1,-1):
        num=pow(2,j)
        print(num,  end="  ")
    print()



"""Enter the number of row:10
1  
2  1  
4  2  1  
8  4  2  1  
16  8  4  2  1  
32  16  8  4  2  1  
64  32  16  8  4  2  1  
128  64  32  16  8  4  2  1  
256  128  64  32  16  8  4  2  1  
512  256  128  64  32  16  8  4  2  1  """