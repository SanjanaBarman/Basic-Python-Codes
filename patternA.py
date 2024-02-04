n=int(input("Enter the number of rows:"))

for i in range(n):
    ch = 65
    for j in range(i+1):
        print(chr(ch), end = " ")
        ch = ch + 1
    print()
