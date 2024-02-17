def partition(arr, low, high):
    pivot=arr[high]
    i=low-1
    for j in range(low, high):
        if arr[j]<pivot:
            i+=1
            arr[i], arr[j]=arr[j], arr[i]
    arr[i+1], arr[high]=arr[high], arr[i+1]
    return i+1

def quick_sort(arr, low, high):
    if low<high:
        pi=partition(arr, low, high)
        quick_sort(arr, low, pi-1)
        quick_sort(arr, pi+1, high)

arr=[]
n=int(input("Enter the length of the array : "))
print("Enter elements - ")
for i in range(n):
    element=int(input())
    arr.append(element)
print("Input Array :", arr)

quick_sort(arr, 0, n-1)
print("Sorted Array :", arr)
