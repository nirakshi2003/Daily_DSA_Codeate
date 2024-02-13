def recursive_insertion_sort(arr, n):
    if n<=1:
        return
    recursive_insertion_sort(arr, n-1)
    key=arr[n-1]
    i=n-2
    while i>=0 and arr[i]>key:
        arr[i+1]=arr[i]
        i-=1
    arr[i+1]=key

arr=[]
n=int(input("Enter the length of the array : "))
print("Enter elements - ")
for i in range(n):
    element=int(input())
    arr.append(element)
print("Input Array :", arr)

recursive_insertion_sort(arr, n)
print("Sorted Array :", arr)
