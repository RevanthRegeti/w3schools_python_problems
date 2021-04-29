# Write a Python program to sum of three given integers. However, if two values are equal sum will be zero

number_1=int(input())
number_2=int(input())
number_3=int(input())

if number_1==number_2 or number_2==number_3 or number_3==number_1:
    print(0)
else:
    print(number_1+number_2+number_3)