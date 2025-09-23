import random
operators=["+","x","-"]
error=0
score=0
print("########### WELCOME TO MATHS GAME ##########\n##########{ONLY FOR KIDDOS}##########")
print("+4 for correct answer \n-2 for wrong answer")
print("You'll be asked 5 simple maths questions")
name=input("Enter your name: ")
for i in range(5):
    print("*"*50)
    n1=random.randint(2,100)
    n2=random.randint(2,100)
    i=random.randrange(0,3)
    op=operators[i]
    result=0
    if op=="+":
        result=n1+n2
    elif op=="x":
        n2=random.randint(2,10)
        result=n1*n2
    elif op=="-":
        if n1<n2:
            n1,n2=n2,n1
        result=n1-n2
    print(n1,op,n2,"=")
    ask=int(input("Enter your answer: "))
    if ask==result:
        print("Your answer is right",name,"!!")
        score+=4
    else:
        print("Your answer is wrong!!!\nExpected Better from you",name,"\nThe answer is ",result)
        score-=2
print("*"*50)
print("YOU SCORED : ",score)
if score==20:
    print("DAYUM!!!\nPERFECT!! YOU SMACKED IT",name.upper(),"!!!!!")
elif score>=14 and score<20:
    print("GOOD!! YOU DID IT",name.upper(),"!!!")
elif score>=8 and score<14:
    print("KINDA OK, BUT TRY TO DO BETTER NEXT TIME")
elif score>=0 and score<8:
    print("PCCHT!! WHAT ARE YOU DOING? VERY POOR!! \nTRY AGAIN RIGHT NOW!!")
else:
    print("YOU ARE NOT WORTH IT, I AM SORRY")
