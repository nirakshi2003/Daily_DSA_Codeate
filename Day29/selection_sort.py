def selection_sort(arr):
    n=len(arr)
    for i in range(n-1):
        key=i
        for j in range(i+1, n):
            if arr[j]<arr[key]:
                key=j
        if key!=i:
            arr[i], arr[key]=arr[key], arr[i]
    return arr

arr=[]
n=int(input("Enter the length of the array : "))
print("Enter elements - ")
for i in range(n):
    element=int(input())
    arr.append(element)
print("Input Array :", arr)

arr1=selection_sort(arr)
print("Sorted Array :", arr1)

