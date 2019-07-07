#simple funcction to compute  factorial of given number
def fact(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num*fact(num-1)

def main():
    x = int(input("Enter the number : "))
    print(x,"! = ",fact(x)) 

if __name__=="__main__":
    main()