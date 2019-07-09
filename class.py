# program to create a class and its objects
class Person:
    # method which gets executed when the class is initiated
    def __init__(self, name, age):
        self.name = name 
        self.age = age
    
    def display(self):
        print("\n",self.name, "is" ,self.age, "years old")
    
#driver code     
def main():
    obj1 = Person("mary", 35)
    obj2 = Person("john", 40)

    obj1.display()
    obj2.display()

    del obj1
    # ERROR : print(obj1.name)

if __name__== '__main__':
    main()

