n=int(input("Enter the number of rows:"))

for i in range(n):
    ch = 65
    for j in range(n,i,-1):
        print(chr(ch), end = " ")
        ch = ch + 1
    print()
    
    
'''Enter the number of rows:26
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 
A B C D E F G H I J K L M N O P Q R S T U V W X Y 
A B C D E F G H I J K L M N O P Q R S T U V W X 
A B C D E F G H I J K L M N O P Q R S T U V W 
A B C D E F G H I J K L M N O P Q R S T U V 
A B C D E F G H I J K L M N O P Q R S T U 
A B C D E F G H I J K L M N O P Q R S T 
A B C D E F G H I J K L M N O P Q R S 
A B C D E F G H I J K L M N O P Q R 
A B C D E F G H I J K L M N O P Q 
A B C D E F G H I J K L M N O P 
A B C D E F G H I J K L M N O 
A B C D E F G H I J K L M N 
A B C D E F G H I J K L M 
A B C D E F G H I J K L 
A B C D E F G H I J K 
A B C D E F G H I J 
A B C D E F G H I 
A B C D E F G H 
A B C D E F G 
A B C D E F 
A B C D E 
A B C D 
A B C 
A B 
A '''