def bubbleSort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
    return arr


n=int(input('Enter the size of an array:'))
arr = []
for i in range(0,n):
    ch=int(input("Enter the value of array:"))
    arr.append(ch)
sortedlist=bubbleSort(arr)  
print("The array in sorted order is:",sortedlist)



"""
Enter the size of an array:5
Enter the value of array:30
Enter the value of array:50
Enter the value of array:10
Enter the value of array:70
Enter the value of array:62
The array in sorted order is: [10, 30, 50, 62, 70]
"""



                
    