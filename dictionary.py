my_dictionary = { 
    "name" : "john",
    "gender" : "male",
    "salary" : "50K",
    "country" : "India"}

print(my_dictionary)
print("my_dictionary['gender'] : ", my_dictionary["gender"])

for x in my_dictionary:
    print(x)

print("\nLen(dictionary) : ", len(my_dictionary))

my_dictionary["city"]="New Delhi"
print("\nUpdated dictionary : ",my_dictionary)

my_dictionary.pop("gender")

print(my_dictionary.get("name"))