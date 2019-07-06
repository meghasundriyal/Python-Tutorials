#performing different string operations
a = "Sample! String  " #single line string
b = '''This is an example 
of multiline string '''                                       #double quotes can also be used
print(a)
print(b)

#strings are treated as array of byte characters in python 
print("a[1] : " ,a[1])
print("a[2:7] : ",a[2:7])

#METHODS ON STRINGS
print("strip : ", a.strip())
print("length of a : ",len(a))
print("uppercase : ",a.upper())
print("lowercase : ",a.lower())
print("split : ",a.split("!"))

print("Hello, world")
print("Helllo","world")
print("Hello"+"world")

print(a.find("t"))
