def movezeros(arr):
    zero=0
    n=len(arr)
    for i in range(n):
        if arr[i]!=0:
            arr[i], arr[zero]=arr[zero], arr[i]
            zero+=1
    return arr

arr=[]
n=int(input("Enter the length of the array : "))
print("Enter elements - ")
for i in range(n):
    element=int(input())
    arr.append(element)
print("Input Array :", arr)

arr1=movezeros(arr)
print("Output Array :", arr1)
