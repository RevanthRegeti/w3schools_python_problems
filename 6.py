# Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers

sample_data=[3, 5, 7, 23]

list_ouput=[]
list=[list_ouput.append(str(i)) for i in sample_data]

print(list_ouput)

tuple_output=tuple(str(i) for i in sample_data)

print(tuple_output)