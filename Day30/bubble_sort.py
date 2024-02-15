def bubble_sort(arr, n):
    for i in range(0, n-1):
        flag=0
        for j in range(0, n-1-i):
            if(arr[j+1]<arr[j]):
                key=arr[j+1]
                arr[j+1]=arr[j]
                arr[j]=key
                flag=1
        if(flag==0):
            break
    return arr

arr=[]
n=int(input("Enter the length of the array : "))
print("Enter elements - ")
for i in range(n):
    element=int(input())
    arr.append(element)
print("Input Array :", arr)

print("Sorted Array :", bubble_sort(arr, n))
