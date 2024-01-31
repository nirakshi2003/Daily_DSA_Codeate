def next_permutation(arr):
    n=len(arr)
    i=n-1
    while i>0 and arr[i-1]>=arr[i]:
        i-=1
    if i<=0:
        return sorted(arr)
    j=n-1
    while arr[j]<=arr[i-1]:
        j-=1
    arr[i-1], arr[j]=arr[j], arr[i-1]
    arr[i:]=reversed(arr[i:])
    return arr

arr=[]
n=int(input("Enter the length of the array : "))
print("Enter elements - ")
for i in range(n):
    element=int(input())
    arr.append(element)
print("Input Array :", arr)

print("Output :", next_permutation(arr))

