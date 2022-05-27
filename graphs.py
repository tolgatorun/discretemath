import random
#for using sample matrices below comment out lines between 8-24
#adjacentMatrix = [[0,1,1,1,0],[1,0,1,0,0],[1,1,0,0,0],[1,0,0,0,1],[0,0,0,1,0]]  #euler path
#adjacentMatrix = [[0,1,1,1,1],[1,0,1,0,0],[1,1,0,0,0],[1,0,0,0,1],[1,0,0,1,0]] #euler cycle 
#adjacentMatrix = [[0,0,0,0,1,1,1],[0,0,0,0,1,1,1],[0,0,0,0,1,1,1],[0,0,0,0,1,1,1],[1,1,1,1,0,0,0],[1,1,1,1,0,0,0],[1,1,1,1,0,0,0]]  #bipartite
#adjacentMatrix = [[0, 4, 0, 0, 0, 0, 0, 8, 0],[4, 0, 8, 0, 0, 0, 0, 11, 0],[0, 8, 0, 7, 0, 4, 0, 0, 2],[0, 0, 7, 0, 9, 14, 0, 0, 0],[0, 0, 0, 9, 0, 10, 0, 0, 0],[0, 0, 4, 14, 10, 0, 2, 0, 0],[0, 0, 0, 0, 0, 2, 0, 1, 6],[8, 11, 0, 0, 0, 0, 1, 0, 7],[0, 0, 2, 0, 0, 0, 6, 7, 0]]


adjacentMatrixInput = input("Please enter adjacency matrix: ")
adjacentMatrixInput = adjacentMatrixInput.split(" ")
sq = int(len(adjacentMatrixInput) ** 0.5)
j = 1
tempArr = []
adjacentMatrix = []
for i in adjacentMatrixInput:
    if j % sq == 0:
        tempArr.append(i)
        adjacentMatrix.append(tempArr)
        tempArr = []
        j = 1
    else:
        j+=1
        tempArr.append(i)



matLen = adjacentMatrix
colorMap = {

}

def breadthFirstSearchColorInsert(visitList,graph,node): 
    visitList.append(node)
    que.append(node)
    while que:
        m = que.pop()
        if m not in colorMap:
            colorMap[m] = 'red'
        #print(m, end = " ")
        for adjacent in graph[m]:
            if adjacent not in colorMap:
                if colorMap[m] == 'red':
                    colorMap[adjacent] = 'blue'
                else:
                    colorMap[adjacent] = 'red'
            if adjacent not in visitList:
                visitList.append(adjacent)
                que.append(adjacent)

def isBipartite(graph):
    for i in graph:
        for adjacent in graph[i]:
            if i != adjacent:
                if(colorMap[i] == colorMap[adjacent]):
                    print("Not a bipartite")
                    return
    print("Bipartite")            

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
                #edges.append([numtoalph[x],numtoalph[y]])
                edges.append([x,y])           

def matToList(vertices,edges):
    adjList = dict()
    for i in vertices:
        adjList[i] = []
        for j in edges:
            if i == j[0]:
                adjList[i].append(j[1])
    return adjList

def findPaths(graph, start, end):
    visited = set()
    visited.add(start)

    nodestack = []
    indexstack = []
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

def dfs(u, graph, visited_edge, path=[]): #for using in check euler
    path = path + [u]
    for v in graph[u]:
        if visited_edge[u][v] == False:
            visited_edge[u][v], visited_edge[v][u] = True, True
            path = dfs(v, graph, visited_edge, path)
    return path

def check_circuit_or_path(graph, max_node):
    odd_degree_nodes = 0
    odd_node = -1
    for i in range(max_node):
        if i not in graph.keys():
            continue
        if len(graph[i]) % 2 == 1:
            odd_degree_nodes += 1
            odd_node = i
    if odd_degree_nodes == 0:
        return 1, odd_node
    if odd_degree_nodes == 2:
        return 2, odd_node
    return 3, odd_node

def check_euler(graph, max_node):
    visited_edge = []
    for i in range(max_node + 1):
        visited_edge.append(list())
        for j in range(max_node +1):
            visited_edge[i].append(False)
    check, odd_node = check_circuit_or_path(graph, max_node)
    if check == 3:
        print("graph is not Eulerian")
        print("no path")
        return
    start_node = 1
    if check == 2:
        start_node = odd_node
        print("graph has a Euler path")
    if check == 1:
        print("graph has a Euler cycle")
    path = dfs(start_node, graph, visited_edge)
    print(path)

def matToWeightedList(adjacentMatrix,matLen):
    weightedList = dict()
    for i in range(matLen):
        weightedList[i] = []
        for j in range(matLen):
            if adjacentMatrix[i][j] >= 1:
                weightedList[i].append([j,adjacentMatrix[i][j]])
    return weightedList 

def dijsktrasShortestPath(initial,destination):
    paths = []
    for p in findPaths(adjacentList,initial,destination):
        paths.append(p)
    distancePaths = []     
    for i in paths:
        distance = 0
        if len(i) == 2:
            for j in weightedList[i[0]]:
                if j[0] == i[1]:
#                    print(j[1])
                    distancePaths.append([i,j[1]])
        else:
            for j in range(len(i)-1):
                for a in weightedList[i[j]]:
                    if a[0] == i[j+1]:
                        distance += a[1]
        distancePaths.append([i,distance])
#    for i in distancePaths:
#        print("Path:",i[0],"\n","Distance:", i[1])
#    print(distancePaths)
    if len(distancePaths) >= 1:
        minDis = distancePaths[0][1]
        minDisPath = [0,0]
        for i in distancePaths:
            if i[1] < minDis:
                minDis = i[1]
                minDisPath[0] = i[0]
        minDisPath[1] = minDis
        return minDisPath
    else:
        return ["There isn't a path between"," "]

dir_undir = '2'
while dir_undir != '1' or dir_undir != '0':
    dir_undir = input("Enter 1 for directed 0 for indirected")
    if dir_undir == '1':
        degreeArray = directedDegree(adjacentMatrix)
        print(degreeArray)
        break
    elif dir_undir == '0':
        degreeArray = indirectedDegree(adjacentMatrix, matLen)
        print(degreeArray)
        break
    else:
        dir_undir = input("Enter 1 for directed 0 for indirected")


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

print("Random number between 0-vertexNumber - 1:", n,"\nChosen pair of vertices:", [initial,destination])
c = 1
for path in findPaths(adjacentList, initial, destination): 
    print("Path",c,":",path)
    c+=1

visitList = []
que = []

for i in adjacentList:
    breadthFirstSearchColorInsert(visitList,adjacentList,i)

isBipartite(adjacentList)
check_euler(adjacentList, 11)

weightedList = matToWeightedList(adjacentMatrix, matLen)
djk = random.choices(vertices, k=2)

minDis = dijsktrasShortestPath(djk[0],djk[1])

print("Path:", minDis[0],'\n',"Distance:",minDis[1])
