#To find the sum of numbers in a string
print("To find the sum of numbers in a string")
s1=input("Enter a String: ")
s2=" "
for i in s1:
    if i.isdigit():
        s2=s2+str(i)
if s2==" ":
    print(s1,"has no digits")
print("The original string: ",s1)
print("The digits: ",s2)
s3=s2.split()
s=0
for i in range(0,len(s3[0])):
    s=int(s3[0][i])+s
print("Sum of digits: ",s)
