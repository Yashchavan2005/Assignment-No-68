
#-------------------------------------------------------
#01 " Function To Create 2d Mtarix
#--------------------------------------------------------

def Creatematrix():

    matrix = [
        [6,4],
        [8,6]
    ]

    print("Completed Created Matrix:",matrix)

    return matrix


#-------------------------------------------------------
#02 : Functions to Display Matrix
#--------------------------------------------------------

def displaymatrix(matix):

    for row in matix:
        print(row)


#-------------------------------------------------------
#03 : Flatten to flatten matrix
#--------------------------------------------------------

def Flattenatrix(matrix):

    faltten_output =[]

    for row in matrix:
        for value in row:
            faltten_output.append(value)


    return faltten_output


#-------------------------------------------------------
#04 : Functions To Calculate Final Output
#--------------------------------------------------------

def calculateOutput(faltten_output):
    total=0

    for value in faltten_output:
        total = total+ value

    return total



def main():

    matrix = Creatematrix()

    displaymatrix(matrix)

    faltten_output =Flattenatrix(matrix)

    print("\n Flatten Output")
    print(faltten_output)

    final_output =calculateOutput(faltten_output)

    print("\nFinal Output")
    print(final_output)


if __name__ == "__main__":
    main()