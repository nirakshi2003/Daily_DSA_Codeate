def pairsum(arr, target):
    seen={}
    for i, num in enumerate(arr):
        complement=target-num
        if complement in seen:
            return "YES", [seen[complement], i]
        seen[num]=i
    return "NO", []

arr=[]
n=int(input("Enter the length of the array : "))
for i in range(n):
    element=int(input())
    arr.append(element)
print("Input Array :", arr)
target=int(input("Enter the target sum: "))

result, indices=pairsum(arr, target)
print("Result :", result)
if result=="YES":
    print("Indices :", indices)
