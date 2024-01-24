def find_missing_number(n, arr):
    actualsum = sum(arr)
    expectedsum = (n+1)*(n+2)//2      #sum of n elements = n*(n+1)//2
    missingnumber = expectedsum - actualsum
    return missingnumber

arr=[]
n=int(input("Enter the length of the array: "))
for i in range(n):
    element=int(input(f"Enter element at position {i + 1}: "))
    arr.append(element)
print("Input Array : ", arr)

result = find_missing_number(n, arr)
print("Missing Number : ", result)
