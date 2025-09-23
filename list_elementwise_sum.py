#To add the corresponding elements of two lists
a=[]
b=[]
a=eval(input("Enter a list: "))
b=eval(input("Enter a list with same number of elements as previous one: "))
c=[]
for i in range(0,len(a)):
    d=a[i]+b[i]
    c.append(d)
print("The list with the sum is",c)
