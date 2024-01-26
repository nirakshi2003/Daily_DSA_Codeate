def appearing_once(arr):
    result=0
    for num in arr:
        result ^= num          #XOR with a number itself results in 0. When we XOR an element that appears twice
                               #with the result it cancels out returning 0.
                               #But when we XOR the single number with 0, it remains unchanged.
    return result

arr=[]
n=int(input("Enter the length of the array : "))
for i in range(n):
    element=int(input())
    arr.append(element)
print("Input Array : ", arr)

print("Element that appears only once : ", appearing_once(arr))
