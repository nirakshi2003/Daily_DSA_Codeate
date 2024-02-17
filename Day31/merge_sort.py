def MergeSort(arr):
    n=len(arr)
    if n<=1:
        return arr
    mid=n//2
    left=arr[:mid]
    right=arr[mid:]
    left_half=MergeSort(left)
    right_half=MergeSort(right)
    return Merge(left_half, right_half)

def Merge(left, right):
    sorted_array=[]
    i=j=0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            sorted_array.append(left[i])
            i+=1
        else:
            sorted_array.append(right[j])
            j+=1
    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])
    return sorted_array

arr=[4,2,1,6,7]
print("Unsorted Array : ", arr)
sort=MergeSort(arr)
print("Sorted Array : ", sort)
