
#---------------------------------------------------------
#01 : Functions To Create Image 
#---------------------------------------------------------

def createiimage():

    image =[
        [0,0,0,0,0],
        [0,0,0,0,0],
        [1,1,1,1,1],
        [0,0,0,0,0],
        [0,0,0,0,0]
    ]

    print("image:",image)

    return image

#---------------------------------------------------------
#02 : Functions To Create Kernal
#---------------------------------------------------------

def  CreateKernal():

    kernal = [
        [-1,-1,-1],
        [0, 0, 0],
        [1, 1 ,1]
    ]

    print("Kernal :",kernal)

    return kernal

#---------------------------------------------------------
#03 : Functions Display Matrix
#---------------------------------------------------------

def displaymatrix(image):

    for Row in image:
        print(Row)


#---------------------------------------------------------
#04 : Functions To pErform Convolution Opertaions 
#---------------------------------------------------------

def Convolution(image,kernal):

    imageRows = len(image)
    imagecolumns = len(image[0])

    kernalRows = len(kernal)
    kernalColumns = len(kernal[0])

    OutputRows = imageRows - kernalRows +1 
    outputColumns = imagecolumns - kernalColumns +1

    Featuremap =[]

    for i in range(OutputRows):

        Row =[]

        for j in range(outputColumns):

            sum = 0 

            print("\nRegion")

            for  x in range(kernalRows):

                for y in range(kernalColumns):

                    imagevalue = image[i +x] [j + y]
                    kernalvalue = kernal[x][y]

                    print(
                        imagevalue,
                        "*",
                        kernalvalue,
                        end="+"
                    )

                    sum = sum+ (imagevalue * kernalvalue)

                    print()

            print("Output:",sum)

            Row.append(sum)

        Featuremap.append(Row)

    return Featuremap

        
def main():

    image =createiimage()

    kernal = CreateKernal()

    Display = displaymatrix(image)

    Feature = Convolution(image,kernal)


if __name__ == "__main__":
    main()