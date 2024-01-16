arr = [4, 7, 1, 9, 12, 3, 6]
largest_element = arr[0]

for num in arr:
    if num > largest_element:
        largest_element = num

print("The Largest Element is:", largest_element)
