import re
phone =str(input("enter the number : "))
print(phone)

result = re.findall(r"[\d]{3} [\d]{3} [\d]{4}", phone)
print(result)
if result == []:
   print("this is not valid phone number")
else:
    print(result)