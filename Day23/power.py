def power(x, n):
    return pow(x, n)result = 1
    for i in range(n):
        result *= x
    return result
    
x=float(input("Enter the a number : "))
n=int(input("Enter the power : "))
print("Output : ", power(x, n))
