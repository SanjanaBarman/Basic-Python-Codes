def bubble(arr,size):
    for i in range(0,size):
        for j in range(0,size-i-1):
            if arr[j]>arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
    return arr
            


def binarySearch(arr,size):
    l=0
    h=size-1
    f=0
    
    while(l<=h):
        mid=(l+h)//2
        if target==arr[mid]:
            f=1
            break
        elif target>arr[mid]:
            l=mid+1
        elif target<arr[mid]:
            h=mid-1
            
    if f==1:
        print(target, "found")
    else:
        print(target ,"NOT found")

arr=[]
size=int(input("Enter the size of the array:"))
for i in range(size):
    ch=int(input("enter the array element:"))
    arr.append(ch)

print("the sorted array is:", bubble(arr,size))


target=int(input("Enter the element you want to search:"))
binarySearch(arr,size)



'''Enter the size of the array:3
enter the array element:20
enter the array element:10
enter the array element:30
the sorted array is: [10, 20, 30]
Enter the element you want to search:30
30 found'''

