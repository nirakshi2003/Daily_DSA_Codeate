def func(arr):
    n=len(arr)
    c1=0
    c2=0
    for i in range(n):
        if arr[i]==1:
            c1+=1
        else:
            if c1>c2:
                c2=c1
            c1=0
    if c1>c2:
        c2=c1
        
    return c2

arr=[]
n=int(input("Enter the length of the array : "))
for i in range(n):
    element=int(input(f"Enter element at position {i + 1}: "))
    arr.append(element)
print("Input Array : ", arr)

result=func(arr)
print("Number of maximum consecutive 1s : ", result)
