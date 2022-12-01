import inputMatrix
import determinant
import matrix

from help import inputRules

print("Linear Algebra Problem Solver")

while True:
    print()
    print("Operations available : ")
    print("-------------------------------")
    print("1 -> Addition of matrix")
    print()
    print("2 -> Subtraction of matrix")
    print()
    print("3 -> Multiplication of matrix")
    print()
    print("4 -> Square of matrix")
    print()
    print("5 -> Determinant of matrix")
    print()
    print("6 -> Exit program")
    print()
    print("7 -> Know input rules ( Important )")
    print("-------------------------------")

    mainMenuChoice = input("Enter your choice : ")
    
    if mainMenuChoice == "6":
        print("Thank you")
        break
    elif mainMenuChoice == "7":
        inputRules()
        
    print("Please select the order of matrix")
    print("1 -> 2x2")
    print("2 -> 3x3")

    orderOfMatrixChoice = input("Enter youir choice :")


    if mainMenuChoice == "1":

        if orderOfMatrixChoice == "1":

            firstOrderTwoMatrix = inputMatrix.orderTwo()
            secondOrderTwoMatrix = inputMatrix.orderTwo()
            res = matrix.addition(firstOrderTwoMatrix,
                                            secondOrderTwoMatrix)
            for i in res:
                print(i)
                
        elif orderOfMatrixChoice == "2":

            orderThreeMatrix = inputMatrix.orderThree()
            secondOrderThreeMatrix = inputMatrix.orderThree()
            res = matrix.addition(orderThreeMatrix,
                                            secondOrderThreeMatrix)
            for i in res:
                print(i)
            
        else:
            print("Invalid Input")

    elif mainMenuChoice == "2":

        if orderOfMatrixChoice == "1":

            firstOrderTwoMatrix = inputMatrix.orderTwo()
            secondOrderTwoMatrix = inputMatrix.orderTwo()
            res = matrix.subtraction(firstOrderTwoMatrix,
                                               secondOrderTwoMatrix)

            for i in res:
                print(i)
            
        elif orderOfMatrixChoice == "2":

            orderThreeMatrix = inputMatrix.orderThree()
            secondOrderThreeMatrix = inputMatrix.orderThree()
            res = matrix.subtraction(orderThreeMatrix,
                                               secondOrderThreeMatrix)

            for i in res:
                print(i)
        
        else:
            print("Invalid input")

    elif mainMenuChoice == "3":

        if orderOfMatrixChoice == "1":

            firstOrderTwoMatrix = inputMatrix.orderTwo()
            secondOrderTwoMatrix = inputMatrix.orderTwo()
            res = matrix.multiply(firstOrderTwoMatrix,
                                            secondOrderTwoMatrix)
            for i in res:
                print(i)
                
        elif orderOfMatrixChoice == "2":

            orderThreeMatrix = inputMatrix.orderThree()
            secondOrderThreeMatrix = inputMatrix.orderThree()
            res = matrix.multiply(orderThreeMatrix,
                                            secondOrderThreeMatrix)

            for i in res:
                print(i)
                
        else:
            print("Invalid input")        
    
    elif mainMenuChoice == "4":

        if orderOfMatrixChoice == "1":

            firstOrderTwoMatrix = inputMatrix.orderTwo()
            res = matrix.square(firstOrderTwoMatrix)

            for i in res:
                print(i)
                
        elif orderOfMatrixChoice == "2":

            firstOrderThreeMatrix = inputMatrix.orderThree()
            res = matrix.square(firstOrderThreeMatrix)

            for i in res:
                print(i)
                
        else:
            print("Invalid input")

    elif mainMenuChoice == "5":

        if orderOfMatrixChoice == "1":

            orderTwoMatrix = inputMatrix.orderTwo()
            res = determinant.orderTwo(orderTwoMatrix)
            print("Determinant of given matrix is :")

            print(res)
                
        elif orderOfMatrixChoice == "2":

            orderThreeMatrix = inputMatrix.orderThree()
            res = determinant.orderThree(orderThreeMatrix)
            print("Determinant of give matrix is : ")

            print(res)
            

       

        
    

    else:
        print("Invalid input. Please try again")
