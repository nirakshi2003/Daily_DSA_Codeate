def min_bit_flips(start, goal):
    xor_result = start ^ goal
    bit_count = 0
    while xor_result:
        bit_count += xor_result & 1
        xor_result >>= 1
    return bit_count

start = int(input("Enter the starting number: "))
goal = int(input("Enter the goal number: "))

result = min_bit_flips(start, goal)
print("Minimum number of bit flips required:", result)
