# Program to extract vowels from an input string and print them in the order 'aeiou', 
# with each vowel repeated according to its frequency in the string.
# Example: Input = "communication" → Output = "aiioou"
s=input("Enter a string: ")
s=s.lower()
v="aeiou"
d={}
s1=""
for i in s:
    if i not in d and i in v:
        d[i]=1
    elif i in d and i in v:
        d[i]=d[i]+1
for i in v:
    if i in d:
        s1=s1+(d[i]*i)
print("Output:",s1)
