def power_of_two(n):
    return n > 0 and (n & (n - 1) == 0)

def main():
  while True:
    try:
      n = int(input("Enter an integer: "))
      break
    except ValueError:
      print("Invalid input. Please enter an integer.")

  if power_of_two(n):
    print(f"{n} is a power of two.")
  else:
    print(f"{n} is not a power of two.")

if __name__ == "__main__":
  main()
