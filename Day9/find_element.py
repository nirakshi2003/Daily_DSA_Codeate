def find_element(arr, num):
    n=len(arr)
    for i in range(n):
        if arr[i]==num:
            return i
    return -1

arr=[]
n=int(input("Enter the length of the array: "))
for i in range(n):
    element=int(input(f"Enter element at position {i + 1}: "))
    arr.append(element)
    
num=int(input("Enter the element to find : "))

index=find_element(arr, num)

if index!=-1:
    print("Element found at index : ", index)
else:
    print("Element not found in the array : ", index)
