def divide(dividend, divisor):
  if divisor==0:
    return None  
  sign = 1
  if dividend < 0 and divisor > 0 or dividend > 0 and divisor < 0:
    sign = -1
  dividend = abs(dividend)
  divisor = abs(divisor)
  quotient = 0
  while dividend >= divisor:
    dividend -= divisor
    quotient += 1
  return quotient * sign

def main():
  while True:
    try:
      dividend = int(input("Enter the dividend: "))
      divisor = int(input("Enter the divisor: "))
      break
    except ValueError:
      print("Invalid input. Please enter integers.")
  quotient = divide(dividend, divisor)

  if quotient is None:
    print("Error: Cannot divide by zero.")
  else:
    print(f"The quotient of {dividend} / {divisor} is {quotient}.")

if __name__ == "__main__":
  main()
