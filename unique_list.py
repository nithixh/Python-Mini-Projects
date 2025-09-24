def unique_list(l):
    d=[]
    for i in l:
        if i not in d:
            d.append(i)
    print("Unique elements :",d)
#Main
l=list(eval(input("Enter a list of integers : ")))
unique_list(l)
