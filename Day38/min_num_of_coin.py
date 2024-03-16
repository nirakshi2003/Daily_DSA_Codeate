def min_num_of_coin(v):
  coins = [1, 2, 5, 10, 20, 50, 100, 500, 1000]  
  ans = 0
  for coin in coins[::-1]:  
    if v >= coin:

      ans += v // coin
      v %= coin  
  return ans

v = int(input("Enter the amount (in Rs) for which you want change: "))

print(f"Minimum number of coins/notes required: {min_num_of_coin(v)}")
