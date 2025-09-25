#GP
a=int(input("Enter First Number: "))
r=int(input("Enter Common Ratio: "))
n=int(input("Enter No. of Terms: "))
print(a,end=",")
for i in range(1,n+1):
    an=a*(r**i)
    print(an,end=",")
