# Parent class
class Person:
    def __init__(self,name,age):
        self.__name = name                        #private attribute
        self.__age = age                          #private attribute
    
    def display(self):
        print("Inside Person Class")
        print("Name :", self.__name)
        print("Age :", self.__age)

# Child class
class Student(Person):
    # overriding __init__() method of parent class
    def __init__(self,sname,sage,marks):
        Person.__init__(self,sname,sage)        #calling parent's init
        self.__marks = marks

    def display_marks(self):
        print("Inside Student Class")
        Person.display(self)
        print("Marks :",self.__marks)  

def main():
    s1 = Student("john",15,150)
    s1.display_marks()

if __name__=='__main__':
    main()    