from cProfile import label
from gettext import find
import random

#adjacentMatrix = [[0,1,0,1],[1,0,2,0],[0,2,0,0],[1,0,0,1]]
#adjacentMatrix = [[0,1,0,1,1],[1,0,1,1,0],[0,0,0,1,1],[1,0,1,0,1],[0,0,0,0,0]]
#adjacentMatrix = [[0,1,1,1,0],[1,0,1,0,0],[1,1,0,0,0],[1,0,0,0,1],[0,0,0,1,0]]
adjacentMatrix = [[0,1,1,1,1],[1,0,1,0,0],[1,1,0,0,0],[1,0,0,0,1],[1,0,0,1,0]]
#adjacentMatrix = [[0,0,0,0,1,1,1],[0,0,0,0,1,1,1],[0,0,0,0,1,1,1],[0,0,0,0,1,1,1],[1,1,1,1,0,0,0],[1,1,1,1,0,0,0],[1,1,1,1,0,0,0]]  #bipartite
#adjacentMatrix = [[0,0,0,0,1,1,0,0],[0,0,0,0,0,0,1,0],[0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1],[1,0,0,0,0,0,0,0],[1,0,1,0,0,0,0,0],[0,1,0,0,0,0,0,0],[0,0,0,1,0,0,0,0]] #bipartite
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

def find_simple_paths(graph, start, end):
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

def dfs(u, graph, visited_edge, path=[]):
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
for path in find_simple_paths(adjacentList, initial, destination): 
    print("Path",c,":",path)
    c+=1

#for i in adjacentList:
#    print("Vertex:",i," -> Adjacents of vertex:",adjacentList[i])

visitList = []
que = []

for i in adjacentList:
    breadthFirstSearchColorInsert(visitList,adjacentList,i)
#for i in colorMap:
#    print(i,colorMap[i])
isBipartite(adjacentList)
check_euler(adjacentList, 11)
