import random

adjacentMatrix = [[0,1,0,1],[1,0,2,0],[0,2,0,0],[1,0,0,1]]
#adjacentMatrix = [[0,1,0,1,1],[1,0,1,1,0],[0,0,0,1,1],[1,0,1,0,1],[0,0,0,0,0]]
matLen = len(adjacentMatrix)

numtoalph = {
    0: "A",
    1: "B",
    2: "C",
    3: "D",
    4: "E",
    5: "F",
    6: "G",
    7: "H",
    8: "I",
    9: "J",
    10: "K",
    11: "L",
    12: "M"
}

def directedDegree(adjacentMatrix):
    # outdeg
    outdegArr = []
    for x in adjacentMatrix:
        count = 0
        for y in x:
            if(y>=1):
                count += 1
        outdegArr.append(count)    
    #
    # indeg
    indegArr = []
    i = 0
    for y in adjacentMatrix:
        count = 0
        for x in adjacentMatrix:
            if (x[i]>=1):
                count += x[i]
        indegArr.append(count)
        i+=1
    return [indegArr,outdegArr]

def indirectedDegree(adjacentMatrix, matLen):
    i = 0
    degreeOfVertices = []
    for x in range(matLen):
        degreeOfVertices.append(0)

    while i < matLen:
        j = matLen-1
        while j >= i:
            if adjacentMatrix[i][j]>=1:
                degreeOfVertices[i] += adjacentMatrix[i][j]
                degreeOfVertices[j] += adjacentMatrix[i][j]
            j-=1
        i+=1
    return degreeOfVertices

def edgeCreator(adjacentMatrix):
    for x in range(matLen):
        for y in range(matLen):
            if(adjacentMatrix[x][y]>=1):
                edges.append([numtoalph[x],numtoalph[y]])           

def matToList(vertices,edges):
    adjList = dict()
    for i in vertices:
        adjList[i] = []
        for j in edges:
            if i == j[0]:
                adjList[i].append(j[1])
    return adjList

def find_simple_paths(graph, start, end):
    visited = set()
    visited.add(start)

    nodestack = list()
    indexstack = list()
    current = start
    i = 0

    while True:
        neighbors = graph[current]

        while i < len(neighbors) and neighbors[i] in visited: i += 1

        if i >= len(neighbors):
            visited.remove(current)
            if len(nodestack) < 1: break
            current = nodestack.pop()
            i = indexstack.pop()
        elif neighbors[i] == end:
            yield nodestack + [current, end]
            i += 1
        else:
            nodestack.append(current)
            indexstack.append(i+1)
            visited.add(neighbors[i])
            current = neighbors[i]
            i = 0

edges = []
edgeCreator(adjacentMatrix)

vertices = []
for x in edges:
    for y in x:
        if y not in vertices:
            vertices.append(y)

adjacentList = matToList(vertices,edges)

n = random.randint(0,matLen-1)
initial,destination = edges[n]
#initial = 'A'
#destination = 'D'
print(n,initial,destination)
for path in find_simple_paths(adjacentList, initial, destination): 
    print(path)
for i in adjacentList:
    print(i,adjacentList[i])


 