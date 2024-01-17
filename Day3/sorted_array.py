def sorted_array(arr):
    n=len(arr)
    if n==1:
        return True
    for i in range(1,n):
        if arr[i-1]>arr[i]:
            return False
    return True

n=5
arr=[1,2,3,4,5]
print(sorted_array(arr))
