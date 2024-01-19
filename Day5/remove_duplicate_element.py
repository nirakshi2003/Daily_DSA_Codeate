def remove_duplicate_element(arr):
    n=len(arr)
    if n==0:
        return 0
    i=0
    for j in range(1, n):
        if arr[j]!=arr[i]:
            i+=1
            arr[i]=arr[j]
    return i+1

arr=[1,1,2,2,2,3,3]
n=remove_duplicate_element(arr)

for i in range(n):
    print(arr[i], end=" ")
