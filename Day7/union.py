def union(arr1, arr2):
    set1=set(arr1)
    set2=set(arr2)
    union_set=set1.union(set2)
    return union_set

arr1=[1,2,3,4,5]
arr2=[2,3,4,4,5]

union_set=union(arr1, arr2)
print(union_set)
