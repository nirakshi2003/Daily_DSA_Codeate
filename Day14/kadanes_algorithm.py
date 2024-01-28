def kadane(arr):
    max_current=max_global=arr[0]
    start_index=end_index=0
    n=len(arr)
    for i in range(1, n):
        if arr[i] > max_current+arr[i]:
            start_index=i
        max_current=max(arr[i], max_current+arr[i])
        if max_current > max_global:
            max_global=max_current
            end_index=i
    return max_global, arr[start_index:end_index+1]

arr=[]
n=int(input("Enter the length of the array : "))
for i in range(n):
    element=int(input())
    arr.append(element)
print("Input Array :", arr)

max_subarray_sum, max_subarray=kadane(arr)
print("Maximum Subarray :", max_subarray)
print("Maximum Subarray Sum :", max_subarray_sum)
