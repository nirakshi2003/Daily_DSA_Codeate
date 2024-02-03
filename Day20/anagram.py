def anagram(str1, str2):
    str1=str1.replace(" ", "").lower()
    str2=str2.replace(" ", "").lower()
    if len(str1)!=len(str2):
        return False
    string1={}
    string2={}
    for i in str1:
        string1[i]=string1.get(i, 0)+1
    for i in str2:
        string1[i]=string1.get(i, 0)+1 
    return string1==string2

str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

print("Are the strings anagrams?", anagram(str1, str2))
