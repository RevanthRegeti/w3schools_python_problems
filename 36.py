# Write a Python program to add two objects if both objects are an integer type

number_1=int(input())
number_2=int(input())

if not isinstance(number_1,int) and isinstance(number_2,int):
    print('Wrong data types')
else:
    print(number_1+number_2)