def find_single(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

nums = list(map(int, input("Enter the array of integers separated by spaces: ").split()))

print("The single element is:", find_single(nums))
