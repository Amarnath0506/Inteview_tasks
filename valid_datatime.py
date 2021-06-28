import datetime

correctDate = None
try:
    newDate = datetime.datetime(2020,5,25)
    print(newDate)
    correctDate = True
except ValueError:
    correctDate = False
print(str(correctDate))