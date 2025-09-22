n=int(input("Enter the kural number: "))
if n not in range(1,1331):
    print("There are only 1330 kurals")
else:
    a=0
    if n%10==0:
        a=n/10
    else:
        a=n//10+1
    print("Adigaram : ",int(a))
