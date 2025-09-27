import csv
mf=open("test.csv","w")
w=csv.writer(mf,delimiter=",")
l=[["PHYSICS","CHEMISTRY"],["MATHS","COMPUTER SCIENCE"],["ENGLISH"]]
for i in l:
     w.writerow(i)
     print(i)
mf.close()
