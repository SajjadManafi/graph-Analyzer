# need to Edge.py file
from Edge import edge


def checkMatrixInputs(matrix):

    for Row in matrix:
        for column in Row:
            if column != 0 and column != 1:
                return False

    return True


def countingEdges(matrix):
    edges = []
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i!=j and edge(i,j) not in edges and edge(j,i) not in edges:
                edges.append(edge(i,j))

    return(len(edges))

def checkPlanarity(E,V):
    return E <= 3*V - 6

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
    edges = countingEdges(matrix)
    V = len(matrix)

    if checkPlanarity(edges , V):
        print("graph in planar!")
    else:
        print("graph is non-planar!")
else:
    print("invalid inputs")


print("")
