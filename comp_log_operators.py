#comparison and logical operators

x = y = 5
z = 8

print("x = ",x)
print("y = ",y)
print("z = ",z)

print("x == y : ", x==y)
print("x == z : ", x==z)

print("x < y : ", x<y)
print("x <= y : ", x<=y)

print("x<y and x<z : ", x<y and x<z)      # x<y(False) and x<z(True) : False
print("x<y or x<z : ", x<y or x<z)      # x<y(False) or x<z(True) : True
