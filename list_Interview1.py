''' nested list is converted to single list'''

l1 = [1,2,3,[5,6,7],[8,9,5]]
output = []
for x in l1:
    if type(x) == list:
        output.extend(x)
    else:
        output.append(x)

print(output)