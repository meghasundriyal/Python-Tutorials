# simple pyramid pattern  
def pyramid(n): 
    spaces = 2*n - 2
  
    # number of rows 
    for row in range(0, n): 
        # column pattern 
        for j in range(0, spaces): 
            print(end=" ") 
      
        # decrementing space after each loop 
        spaces = spaces - 1

        for j in range(0, row+1): 
            # printing stars 
            print("* ", end="") 
      
        # ending line after each row 
        print("\r") 

pyramid(5)            