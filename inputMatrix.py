def orderTwo():
    '''
    Allows to take input for 2x2 matrix
    '''
    print()
    print("Enter your input for matrix :")
    print("----------------")
    mat = [] 
    for i in range(2):
        row = list(map(int , input().split()))
        mat.append(row)
    print("-----------------")
    return mat


def orderThree():
    '''
    Allows to take input for 3x3 matrix
    '''
    print()
    print("Enter your input for matrix :")
    print("----------------")
    mat = [] 
    for i in range(3):
        row = list(map(int , input().split()))
        mat.append(row)
    print("-----------------")
    return mat

  