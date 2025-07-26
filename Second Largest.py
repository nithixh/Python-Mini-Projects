#To find the second largest number in a list
num=list(eval(input("Enter list of numbers:")))
l=0
s=0
for i in num:
    if i>l:
        s=l
        l=i
    if i<l and i>s:
        s=i
print("Second largest number is:{}".format(s))
