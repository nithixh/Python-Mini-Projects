"""
Vowel Count

This script counts the number of vowels (both uppercase and lowercase) in a given string.
"""

#VOWEL COUNT
s=input("Enter a String: ")
l=len(s)
c=0
v="AEIOUaeiou"
for i in range(0,l):
    if s[i] in v:
        c+=1
print(c)
