import pickle as p
def appendData():
    f=open("Products.dat","ab")
    a="y"
    while a=="y":
        i=int(input("Enter ID: "))
        n=input("Enter Name: ")
        pr=int(input("Enter Price: "))
        p.dump({"PID":i,"PNAME":n,"PRICE":pr},f)
        a=input("Add more?[y/n]: ")
    f.flush()
    f.close()
def findProduct(pid):
    f=open("Products.dat","rb")
    while True:
        try:
            D=p.load(f)
            if D["PID"]==pid:
                print("Name: ",D["PNAME"])
                print("Price: ",D["PRICE"])
                break
        except EOFError:
            print("Product not found")
            break
    f.close()
pi=int(input("Enter ID to search: "))
appendData()
findProduct(pi)
