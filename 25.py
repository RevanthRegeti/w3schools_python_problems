# Write a Python program to check whether a specified value is contained in a group of values

lenght_of_the_group=int(input())
group=[]
number_to_be_checked=int(input())

for i in range(0,lenght_of_the_group):
    elements=int(input())
    group.append(elements)
if number_to_be_checked in group:
    print(True)
else:
    print(False)