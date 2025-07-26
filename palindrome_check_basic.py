# Program to check whether a given string is a palindrome (ignores spaces and is case-insensitive)
s=input("Enter string: ")
string1=""
for i in range(0,len(s)):
    if s[i]!=" ":
        string1+=s[i]
string=string1.lower()
if string[::-1]==string:
    print("{} is palindrome".format(string))
else:
    print("{} is not a palindrome".format(string))
