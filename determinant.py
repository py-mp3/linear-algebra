def orderTwo(orderTwoMatrix):
    det = (orderTwoMatrix[0][0] * orderTwoMatrix[1][1] ) -  (orderTwoMatrix[1][0] * orderTwoMatrix[0][1] )
    return det

def orderThree(orderThreeMatrix):
    det = (orderThreeMatrix[0][0] * (orderThreeMatrix[1][1]*orderThreeMatrix[2][2] - orderThreeMatrix[2][1]*orderThreeMatrix[1][2]) 
                  -orderThreeMatrix[0][1] * (orderThreeMatrix[1][0]*orderThreeMatrix[2][2] - orderThreeMatrix[2][0]*orderThreeMatrix[1][2])
                  +orderThreeMatrix[0][2] * (orderThreeMatrix[1][0]*orderThreeMatrix[2][1] - orderThreeMatrix[2][0]*orderThreeMatrix[1][1]))

    return det