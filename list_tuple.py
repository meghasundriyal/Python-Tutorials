my_list = ["apple","mango","banana","orange"]      # defining list
my_tuple = ("java","cpp","python")

print("LIST : ",my_list)
print("TUPLE : ",my_tuple)

#access item
print("\n ----- ACCESSING ITEM 0 ------")
print(my_list[0])
print(my_tuple[0])

#change item 
print("\n ----- CHANGING ITEM ------")
my_list[0] = "new"
# ERROR : my_tuple[0] = "new"
print(my_list)

#check membership
print("\n ----- MEMBERSHIP ------")
if "mango" in my_list:
    print("Mango is present in my_list")

if "java" in my_tuple:
    print("java is present in my_tuple")

#check length
print("\n ----- LEN() FUNCTION ------")
print("len(my_list) : " ,len(my_list))    
print("len(my_tuple) : " ,len(my_tuple))

#remove item 
print("\n ----- REMOVE() FUNCTION ------")
my_list.remove("banana")
print(my_list)    

#ERROR : my_tuple.remove("java")    

#Constructor tuple() and list()
new_tuple = tuple(my_list)            #creates a tuple 
new_list = list(my_list)              #creates a list  
print("\nnew_tuple : ",new_tuple)
print("new_list : ",new_list)
