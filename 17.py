# Write a Python program to test whether a number is within 100 of 1000 or 2000.
number=int(input())

if abs(1000-number)<=1000 or (abs(2000-number)<=100):
    print(True)
else:
    print(False)