#AP
a=int(input("Enter first term: "))
d=int(input("Common difference: "))
n=int(input("No. of terms: "))
an=a+(n-1)*d
print("Last term: ",an)
e=an+d
for i in range(a,e,d):
    print(i,end=",")
