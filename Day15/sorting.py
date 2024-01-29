def sorting(arr):
    n=len(arr)
    zero=0
    one=0
    two=n-1
    
    while one <= two:
        if arr[one]==0:
            arr[zero], arr[one]=arr[one], arr[zero]
            zero += 1
            one += 1
        elif arr[one]==2:
            arr[one], arr[two]=arr[two], arr[one]
            two -= 1
        else:
            one += 1

arr=[]
n=int(input("Enter the length of the array : "))
for i in range(n):
    element=int(input())
    arr.append(element)
print("Input Array :", arr)

print("Sorted Array :", sorting(arr))
