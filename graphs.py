

adjacentMatrix = [[0,1,0,1],[1,0,2,0],[0,2,0,0],[1,0,0,1]]
matLen = len(adjacentMatrix)

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

degreeOfVertices = indirectedDegree(adjacentMatrix, matLen)
print(degreeOfVertices)