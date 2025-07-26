"""
2x2 Matrix Determinant Calculator

This script calculates the determinant of a 2x2 matrix using the formula:
det = ad - bc
"""
print("Determinant calculator for a 2x2 matrix")
matrix2 = list(map(int, input("Enter 4 elements separated by space: ").split()))
det2=(matrix2[0]*matrix2[3])-(matrix2[2]*matrix2[1])
print("Determinant of the given matrix = ",det2)
