def palindrome(s):
    s = ''.join(char.lower() for char in s if char.isalnum())
    return s == s[::-1]

s = input("Enter a string : ")
result = palindrome(s)
print(result)
