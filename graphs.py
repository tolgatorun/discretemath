

#adjacentMatrix = [[0,1,0,1],[1,0,2,0],[0,2,0,0],[1,0,0,1]]
adjacentMatrix = [[0,1,0,1,1],[1,0,1,1,0],[0,0,0,1,1],[1,0,1,0,1],[0,0,0,0,0]]
matLen = len(adjacentMatrix)

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
                vertices.append([numtoalph[x],numtoalph[y]])           

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
vertices = []

edgeCreator(adjacentMatrix)
chosenPair = ["A","D"]
allPaths = []
for x in vertices:
    if x[0] == chosenPair[0]:
        print(x)
        for y in vertices:
            if y[0] == x[1]:
                print("this is y", y)
                if y[1] == chosenPair[1]:
                    print("this is a path")
