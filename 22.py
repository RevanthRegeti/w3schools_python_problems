# Write a Python program to count the number 4 in a given list

size_of_list=int(input())
input_list=[]
count=0

for i in range(0,size_of_list):
    elements=int(input())
    input_list.append(elements)

for i in input_list:
    if i==4:
        count+=1

print(count)
