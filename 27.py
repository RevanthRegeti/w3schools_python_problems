# Write a Python program to concatenate all elements in a list into a string and return it.
output=''
lenght_of_the_list=int(input())

group=[]

for i in range(0,lenght_of_the_list):
    elements=int(input())
    group.append(elements)

for i in group:
    output+=str(i)

print(output)