import numpy as np

def median(matrix):
    arr1=np.array(matrix).flatten()
    arr2=np.sort(arr1)
    n=len(arr2)
    print("Linearly sorted :", arr2)
    return arr2[n//2] 

matrix=[]
rows=int(input("Enter the number of rows : "))
cols=int(input("Enter the number of columns : "))
print("Enter the elements of the matrix - ")
for i in range(rows):
    element=list(map(int, input().split()))
    matrix.append(element)
print("Input Matrix :")
for j in matrix:
    print(j)

result=median(matrix)
print("Median :", result)
