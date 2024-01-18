arr = [13, 46, 24, 52, 20, 9]
n = len(arr)

for i in range(0, n):
    min_val = arr[i]
    index = i
    for j in range(i, n):
        if arr[j] < min_val:
            min_val = arr[j]
            index = j
    temp = arr[i]
    arr[i] = arr[index]
    arr[index] = temp

print(arr)
