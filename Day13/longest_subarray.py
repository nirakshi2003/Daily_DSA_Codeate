def longest_subarray(arr, k):
    subarray_len = 0
    current_sum = 0
    start = 0
    subarray_start = 0
    subarray_end = 0
    
    n=len(arr)
    
    for end in range(n):
        current_sum += arr[end]
        
        while current_sum > k:
            current_sum -= arr[start]
            start += 1
        
        if current_sum == k:
            subarray_len = end - start + 1
            subarray_start = start
            subarray_end = end
            
    return arr[subarray_start : subarray_end+1]


arr=[]
n=int(input("Enter the length of the array : "))
for i in range(n):
    element=int(input())
    arr.append(element)
print("Input Array : ", arr)

k=int(input("Enter the sum value : "))

subarray = longest_subarray(arr, k)
subarray_len = len(subarray)

print("The longest subarray with sum", k, "is", subarray, "and its length is", subarray_len)
