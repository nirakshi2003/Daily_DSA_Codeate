def union(arr1, arr2):
    arr3=set(arr1).union(arr2)
    result=sorted(list(arr3))
    return result

arr1=[1,2,3,4,5]
arr2=[2,3,4,4,5]

result=union(arr1, arr2)
print(result)
