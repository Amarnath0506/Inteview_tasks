'''Working on Dictionary bulit-in-methods'''


d1 = {}
d2 = {"1":"test","2":2,"3":3,"4":4}

d1.update(d2)
#get keys
d_keys = d2.keys()
print(d_keys)
#get values
d_values = d2.values()
print(d_values)

#get dictionary items
d_items = d2.items()
print(d_items)

#get dir of the dictionary
d_dirs = dir(d2)
print(d_dirs)

# using get method to get perticular value
d_get = d2.get("1")
print(d_get)

# elemenate element in the dictionary
d_pop = d2.pop("4")
print(d2)
print(d_pop)

# remove last key pair in the dictionary
d_popitem = d2.popitem()
print(d2)
print(d_popitem)

# remove all elements in the dictionary
d_clear = d2.clear()
print(d2)
print(d_clear)
