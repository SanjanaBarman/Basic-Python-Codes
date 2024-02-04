n=int(input("Enter the number of rows:"))

for i in range(n):
    ch = 65
    for j in range(i+1):
        print(chr(ch), end = " ")
        ch = ch + 1
    print()



'''Enter the number of rows:10
A 
A B 
A B C 
A B C D 
A B C D E 
A B C D E F 
A B C D E F G 
A B C D E F G H 
A B C D E F G H I 
A B C D E F G H I J '''
