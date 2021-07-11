#imports
from collections import defaultdict
import math

# need to Edge.py file
from Edge import edge

# for counting nodes
nodes = []

# for save graph
graph = {}
Sources = []

# save graph to use in DFS
graphCopy = defaultdict(list)

#primGraph
primGraph = defaultdict(list)


# add nodes and edges to graph
def addToGraph(S , D , W):
    # ignore Loop
    if S != D:
        if edge(S,D) not in graph and edge(D,S) not in graph:
            graph[edge(S,D)] = W
        
        else:
            if edge(S,D) in graph and graph[edge(S,D)] > W:
                graph[edge(S,D)] = W
            if edge(D,S) in graph and graph[edge(D,S)] > W:
                graph[edge(D,S)] = W

        if D not in graphCopy[S]:
            graphCopy[S].append(D)

        if D not in primGraph[S]:
            primGraph[S].append(D)
        if S not in primGraph[D]:
            primGraph[D].append(S) 
        

        if S not in nodes:
            nodes.append(S)
        
        if D not in nodes:
            nodes.append(D)


# Depth First Search
def DFS(node , Visited):
    
    Visited.add(node)

    for neighbour in graphCopy[node]:
        if neighbour not in Visited:
            DFS(neighbour , Visited)


# check graph Connectivity
def checkConnectivity(node):

    visited = set()
    DFS(node , visited)

    return len(nodes) == len(visited)


# find shortest edge and path
def findShortestPath(Sources):
    min = math.inf

    sr ,  des = None , None
    
    for src in Sources:
        Destinations = primGraph[src]

        for dest in Destinations:

            if dest not in Sources:

                if edge(src , dest) in graph:
                    if graph[edge(src , dest)] < min:
                        min = graph[edge(src , dest)]
                        sr , des = src , dest

                if edge(dest , src) in graph:
                    if graph[edge(dest , src)] < min:
                        min = graph[edge(dest , src)]
                        sr , des = src , dest
                

    return edge(sr , des)

# prim algorithm
def prim(node):
    sum = 0
    Sources.append(node)

    while len(Sources) < len(nodes):
        edg = findShortestPath(Sources)
        Sources.append(edg.D)
        print(edg.S , "==>" , edg.D)
        if edg in graph : sum += graph[edg]
        elif edge(edg.D , edg.S) in graph : sum += graph[edge(edg.D , edg.S)]

    return sum
        

print("")
print("default:")
print("S" , "==>", "A" , "W:" , 7)
print("S" , "==>", "C" , "W:" , 8)
print("C" , "==>", "C" , "W:" , 1)

print("C" , "==>", "A" , "W:" , 3)
print("C" , "==>", "B" , "W:" , 4)
print("C" , "==>", "D" , "W:" , 3)
print("A" , "==>", "B" , "W:" , 6)
print("A" , "==>", "B" , "W:" , 9)
print("B" , "==>", "D" , "W:" , 2)
print("B" , "==>", "T" , "W:" , 5)
print("D" , "==>", "T" , "W:" , 2)
print("")
print("Do you want the program to work with a graph made by default? (y/n)")
defultInputsOrNot = input()


if defultInputsOrNot.lower() == 'y':
    addToGraph("S" , "A" , 7)
    addToGraph("S" , "C" , 8)
    addToGraph("C" , "C" , 1)
    addToGraph("C" , "A" , 3)
    addToGraph("C" , "B" , 4)
    addToGraph("C" , "D" , 3)
    addToGraph("A" , "B" , 6)
    addToGraph("A" , "B" , 9)
    addToGraph("B" , "D" , 2)
    addToGraph("B" , "T" , 5)
    addToGraph("D" , "T" , 2)


else:
    print("Please enter the number of graph edges:" , end=" ")
    n = int(input())
    print("")
    print("Please enter the vertices of the graph according to the example!")
    print("For example, for A==>B W:3 , Enter: A B 3")
    print("")
    
    for i in range(n):
        ver = input().split(" ")
        addToGraph(ver[0] , ver[1] , int(ver[2]))

    print("")


if checkConnectivity(nodes[0]):
    print("sum:" ,prim(nodes[0]))
else:
    print("graph is disconnected!")

print("")



# S A 7
# S C 8
# C C 1
# C A 3
# C B 4
# C D 3
# A B 6
# A B 9
# B D 2
# B T 5
# D T 2
