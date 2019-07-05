#creating variables 
string = "This is within quotes"           #string type 
num = 5                   #number   
comp_num = 1 + 8j         #complex number
x = eval("1+2")           #evaluating  

print("string : " , string)
print("num : " ,num)
print("comp_num : " ,comp_num)
print("x : " ,x)

#multiple assigments
a,b,c = 1,2.6,"c"
print(a,b,c)

#assigning same value 
x=y=55
print(x,y)

#casting 
print(str(a))
print(complex(b))
