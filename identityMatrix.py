print("This program creates a square identity matrix.")
size = int(input("Please enter the width of the matrix desired: "))

def matrix(width):
    for row in range(0, width):
        for col in range(0, width):
            if (row == col):
                print("1 ", end = " ")
            else:
                print("0 ", end = " ")
        print( )

matrix(size)
