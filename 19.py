# Write a Python program to get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged

input_string=input()

if input_string.startswith('If'):
    print(input_string)
else:
    print('If'+' '+input_string)