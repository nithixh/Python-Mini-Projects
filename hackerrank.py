"""
Transform Sentence

This program transforms a sentence based on the relative positions of characters in the alphabet.
Originally implemented as part of the HackerRank Python Basic Skills Certification test.
"""

def transformSentence(sentence):
    a="abcdefghijklmnopqrstuvwxyz"
    ls=list(sentence)
    r=""+ls[0]
    for i in range(1,len(ls)):
        if ls[i]==" ":
            r=r+ls[i]
        elif ls[i-1]==" ":
            r=r+ls[i]
        elif a.index(ls[i].lower()) < a.index(ls[i-1].lower()):
            r=r+ls[i].lower()
        elif a.index(ls[i].lower()) > a.index(ls[i-1].lower()):
            r=r+ls[i].upper()
        elif a.index(ls[i].lower()) == a.index(ls[i-1].lower()):
            r=r+ls[i]
    return r
sen=input("Enter Sentence: ")
res=transformSentence(sen)
print(res)
