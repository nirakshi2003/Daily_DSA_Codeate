def floor_ceiling(arr, x):
    arr.sort()
    n=len(arr)
    floor=None
    ceiling=None
    left=0
    right=n-1
    while left<=right:
        mid=(left+right)//2
        if arr[mid]==x:
            return x, x
        elif arr[mid]<x:
            floor=arr[mid]
            left=mid+1
        else:
            ceiling=arr[mid]
            right=mid-1
    return floor, ceiling

arr=[]
n=int(input("Enter the length of the array : "))
print("Enter the elements : ")
for i in range(n):
    element=int(input())
    arr.append(element)
print("Input Array :", arr)
x=int(input("Enter the target element : "))
floor, ceiling=floor_ceiling(arr, x)
print("Floor:", floor)
print("Ceiling:", ceiling)
