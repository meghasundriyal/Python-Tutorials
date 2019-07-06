#simple set operations
my_set = {"mon", "tues","fri"}

print(my_set)

#accessing items
# ERROR : print(my_set[2])

for day in my_set:
    print(day)

#adding and updating item
my_set.add("sat")
print("after adding 'sat' : ", my_set)

my_set.update(["sun","sat"])
print("after updating : ",my_set)

#clear() and del
my_set.clear()
print(my_set)

del my_set
print(my_set)
    