# WHILE LOOP
print(" ~~~~ while loop ~~~~~ \n")
i = 0
while i<5:
    print(i)
    i+=1

# FOR LOOP
print(" ~~~~ for loop ~~~~~ \n")
for x in range(5):    # 5 is not included
    print(x)

#for loop is commonly used to iterate through lists, tuples, sets...
print("\nfor loop in list ")
for x in ["mon","tues","wed","thurs","fri","sat","sun"]:
    print(x)    

print("\nfor loop in set ")
for x in {"mon","tues","wed","thurs","fri","sat","sun"}:
    print(x)        