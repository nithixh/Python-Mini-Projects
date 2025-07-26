"""
Bit Count (Hamming Weight)

This script counts the number of '1' bits in a given binary string.
Useful in error detection, cryptography, and bitwise programming.
"""

a=input("Enter bits: ")
c=0
for i in range(len(a)):
    if a[i]=='1':
        c+=1
print(c)  
