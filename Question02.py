
#-------------------------------------------
#01 : Function To Create Feature map
#-------------------------------------------

def CreateFeaturemap():

    feature_map =[
        [3,3,3],
        [0,0,0],
        [-3,-3,-3]
    ]

    print("Feature Map Created Sucessfully:",feature_map)

    return feature_map

#-------------------------------------------
#02 : Functions to Display Matrix 
#-------------------------------------------

def Displaymatrix(feature_map):

    for row in (feature_map):
        print(row)


#-------------------------------------------
#03 : Functions To Apply Relu
#-------------------------------------------
def applyrelu(feature_map):

    relu_output =[]

    for row in feature_map:
        new_row =[]

        for value in row:
            if value <0 :
                new_row.append(0)
            else:
                new_row.append(value)

        relu_output.append(new_row)

    return relu_output


#-------------------------------------------
#03 : Functions To Apply 2 x  2 Max Pooling
#-------------------------------------------

def Maxpooling(relu_output):

    pooled_output =[]

    rows = len(relu_output)
    columns =len(relu_output[0])

    for i in range(rows -1):
       new_row =[]

       for j in range(columns -1):

            value1 = relu_output[i][j]
            value2 = relu_output[i][j+1]
            value3 = relu_output[i +1][j]
            value4 = relu_output[i +1][j+1]

            maximum = max(value1,value2,value3,value4)

            new_row.append(maximum)

       pooled_output.append(new_row)

    return pooled_output


#-------------------------------------------
#04 : Functions Yo Display size
#-------------------------------------------

def Displaysize(feature_map,message):

    rows = len(feature_map)
    columns = len(feature_map[0])

    print(message,rows,"X",columns)

    

def main():

    feature_map = CreateFeaturemap()

    DisplayRow = Displaymatrix(feature_map)

    relu_output = applyrelu(feature_map)

    pooled_output = Maxpooling(relu_output)


    Displaysize(feature_map, "Feature Map Size:")
    Displaysize(relu_output, "ReLU Output Size:")
    Displaysize(pooled_output, "Pooled Output Size:")



if __name__ == "__main__":
    main()