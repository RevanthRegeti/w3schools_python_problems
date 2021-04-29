# Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string. Return the n copies of the whole string if the length is less than 2

input_string=input()
copies_to_be_printed=int(input())

for i in range(copies_to_be_printed):

    print(input_string[:2])