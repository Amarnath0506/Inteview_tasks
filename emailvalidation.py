''' validation for email '''

import re

def check_valid_email(email):
    if (re.match("^[a-zA-Z0-9_+&*-]+(?:\\.[a-zA-Z0-9_+&*-]+)*@(?:[a-zA-Z0-9-]+\\.)+[a-zA-Z]{2,7}$", email) != None):
        return email
    return "colud you please provide correct email "


email = "abc@gmail.com"
output = check_valid_email(email)
print(output)