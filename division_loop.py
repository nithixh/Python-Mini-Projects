#Division using loop
a=int(input("Enter a number greater than 0: "))
b=int(input("Enter a number greater than 0: "))
res=0
while a>=b:
    a=a-b
    res+=1
rem=a
print("Quotient : ",res)
print("Remainder : ",rem)
