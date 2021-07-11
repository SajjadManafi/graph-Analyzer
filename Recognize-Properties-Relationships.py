
# check Matrix Inputs
def checkMatrixInputs(matrix):

    for Row in matrix:
        for column in Row:
            if column != 0 and column != 1:
                return False

    return True

# check Reflexive
def checkReflexive(matrix):
    n = len(matrix)

    for i in range(n):
        if matrix[i][i] != 1:
            return False
    return True

# build Transpose Matrix
def buildTransposeMatrix(matrix):
    Tmatrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return Tmatrix


# check Symmetric
def checkSymmetric(matrix):
    if matrix == buildTransposeMatrix(matrix):
        return True
    else:
        return False

# intersection
def intersection(Num1 , Num2):
    if Num1 == 1 and Num2 == 1:
        return 1
    else:
        return 0


# check Antisymmetric
def checkAntisymmetric(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if intersection(matrix[i][j] , buildTransposeMatrix(matrix)[i][j]) == 1 and i!=j:
                return False
    return True

# matrix Multiplication
def matrixMultiplication(matrix1,matrix2):
    res = []
    for i in range(0,len(matrix1)):
        temp=[]
        for j in range(0,len(matrix2[0])):
            s = 0
            for k in range(0,len(matrix1[0])):
                s += matrix1[i][k]*matrix2[k][j]
            temp.append(s)
        res.append(temp)

    return res

# fix After Multiplication
def fixAfterMultiplication(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] > 1:
                matrix[i][j] = 1
    return matrix

# check Transitive
def checkTransitive(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if fixAfterMultiplication(matrixMultiplication(matrix,matrix))[i][j] > matrix[i][j]:
                return False
    return True

# Get inputs
print ("Please enter the elements of matrix!. For example:")
print("------")
print("1 0 0")
print("0 1 0")
print("0 0 1")
print("------")

print("")
matrix = []

firstLine = input().split(" ")
matrix.append(list(map(int,firstLine)))

for i in range(len(firstLine)-1):
    Line = input().split(" ")
    matrix.append(list(map(int,Line)))

print("")

if checkMatrixInputs(matrix):

    Reflexive = checkReflexive(matrix)
    Symmetric = checkSymmetric(matrix)
    Antisymmetric = checkAntisymmetric(matrix)
    Transitive = checkTransitive(matrix)
    Equivalence =  Reflexive and Symmetric and Transitive
    partiallyOrderedSet = Reflexive and Antisymmetric and Transitive

    print("Reflexive:", Reflexive)
    print("")
    print("Symmetric" , Symmetric)
    print("")    
    print("Antisymmetric" , Antisymmetric)
    print("")
    print("Transitive" , Transitive)
    print("")
    #Equivalence
    print("Equivalence:", Equivalence)
    print("")
    #partiallyOrderedSet
    print("partiallyOrderedSet" , partiallyOrderedSet)

    print("")

else:
    print("invalid inputs")


