# This is a simple program to import and use different modules in one file

import factorial as fact            # import factorial module and call it "fact"

#driver code
def main():
    print(" in-built functions of imported module : " ,dir(fact))       # list all the functions and variables in the module
    x = 5
    print(" factorial ",x,"=",fact.fact(x))       # accessing variable of fact module

if __name__ == "__main__":
    main()    