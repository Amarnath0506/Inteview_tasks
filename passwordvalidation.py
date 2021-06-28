''' password validation in python code'''

import re


def check_valid_password(password):
    while True:
        if len(password) < 8:
            return "Make sure your password is at least 8 letters"
        elif re.search('[0-9]', password) is None:
            return "Make sure your password has a number in it"
        elif re.search('[A-Z]', password) is None:
            return "Make sure your password has a capital letter in it"
        else:
            return password
            break


password = input("Enter a password: ")
output = check_valid_password(password)
print(output)