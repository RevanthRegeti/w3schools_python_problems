# Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20

number_1=int(input())
number_2=int(input())

if number_1+number_2 in range(15,20):
    print(20)
else:
    print(number_1+number_2)