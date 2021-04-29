# Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5

def same_integers(number_1,number_2):
    if number_1==number_2 or abs(number_1-number_2) ==5:
        return True
    else:
        return False

print(same_integers(2,2))