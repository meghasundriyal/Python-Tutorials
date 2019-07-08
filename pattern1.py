# simple right sided pyramid pattern 
def pattern(n):
    '''
    no of stars in each line will be equal to the line no.
    '''
    # number of rows
    for row in range(n):

        # keeping track of the pattern
        for column in range(0,row+1):
            print(" * ",end="")

        # next line     
        print("\n")
            
pattern(5)           
