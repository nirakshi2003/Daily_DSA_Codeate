def length_of_longest_substring(s):
  char_index = {}
  max_length = 0
  start = 0
  for i, ch in enumerate(s):
    if ch in char_index:
      start = max(start, char_index[ch] + 1)
    char_index[ch] = i
    max_length = max(max_length, i - start + 1)
  return max_length

s=input("Enter a string: ")
print(length_of_longest_substring(s))
