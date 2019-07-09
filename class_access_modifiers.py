# simple program to understand access modifiers in python
''' 
    Python has no access modifiers, all methods and attributes are public. 
    It follows naming convention to emulate the behaviour of protected and private variables/method
'''

class Rectangle():
    def __init__(self,length,width,height):
        self.length = length                        
        self._width = width                          #protected
        self.__height = height                       #private   

    def area(self):
        ar = self.length * self._width * self.__height
        print("Area ", ar)

#driver code
def main():
    # creating an object of Rectangle class
    obj1 = Rectangle(10,10,10) 
    obj1.area()
    print("Length :", obj1.length)
    print("Width :", obj1._width)
    #ERROR print("Height :",obj1.__height) 
    print("Height :", obj1._Rectangle__height)  #mangling of private data 

if __name__=='__main__':
    main()