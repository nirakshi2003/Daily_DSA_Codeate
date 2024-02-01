def set_matrix_zero(matrix, rows, cols):
    if not matrix:
        return []
    zero_rows=set()
    zero_cols=set()

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j]==0:
                zero_rows.add(i)
                zero_cols.add(j)

    for k in zero_rows:
        matrix[k]=[0]*cols

    for l in zero_cols:
        for m in range(rows):
            matrix[m][l] = 0
    return matrix

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

result=set_matrix_zero(matrix, rows, cols)
print("Set Zero Matrix :")
for k in result:
    print(k)
