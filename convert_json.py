# Python has in-built package 
import json         

'''
JSON is a syntax for storing and exchanging data. 
'''
# Convert from JSON to python
j1 =  '{ "name":"John", "age":30, "city":"New York"}'        #sample JSON string
py1 = json.loads(j1)                                         #convert JSON string to python object
print("\nJSON String :",j1)
print("Python :",type(py1),py1) 

j2 =  '["apple", "bananas"]'       
py2 = json.loads(j2)                                         #convert JSON string to python object
print("\nJSON String :",j2)
print("Python :",type(py2),py2)


# Convert from python to JSON
py3 = "sample python string"
py4 = 55
py5 = None
print("\nPython to JSON conversions")
print(json.dumps(py3))                    #string converted to JSON
print(json.dumps(py4))                    #integer converted to JSON
print(json.dumps(py5))                    #None is converted to NULL object in JSON