# Write a Python program to create a histogram from a given list of integers
charecter_to_be_printed=input()

lenght_of_the_list=int(input())

group=[]

for i in range(0,lenght_of_the_list):
    elements=int(input())
    group.append(elements)

for i in group:
    print(charecter_to_be_printed*i)