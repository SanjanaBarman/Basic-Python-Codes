yr=int(input("Enter the year:"))
if yr%400==0 or yr%4==0 and yr%100!=0:
    print(yr , "is a Leap Year")
else:
    print(yr , "is NOT a leap year")