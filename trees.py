
""" graph = {
  '1' : ['2','3','4'],
  '2' : ['5', '6'],
  '3' : ['7','8'],
  '4' : ['9','10','11'],
  '5' : ['12','13'],
  '6' : [],
  '7' : ['14','15'],
  '8' : ['16','17'],
  '9' : [],
  '10' : [],
  '11' : [],
  '12' : [],
  '13' : [],
  '14' : [],
  '15' : [],
  '16' : [],
  '17' : []
} """

""" graph = {
    'a' : ['b','g'],
    'b' : ['c','d'],
    'g' : ['h','i','j'],
    'c' : ['e'],
    'd' : ['f'],
    'h' : [],
    'i' : ['k'],
    'j' : [],
    'e' : [],
    'f' : [],
    'k' : [],
} """

graph = {
    '1': ['2'],
    '2': ['3'],
    '3': ['4'],
    '4': []
}
def edgeCreator(graph):
    edges = []
    for i in graph:
        for j in graph[i]:
            edges.append([i,j])
    return edges

def bfs(graph,vertex):
    visited = []
    queue = []
    visited.append(vertex)
    queue.append(vertex)
    
    while queue:
        m = queue.pop(0)
        print(m)
        for adjacent in graph[m]:
            if adjacent not in visited:
                visited.append(adjacent)
                queue.append(adjacent)

def descendantFind(edges): #checks second index of edges
    descendants = []
    for i in edges:
        if i[1] not in descendants:
            descendants.append(i[1])
    return descendants

def vertexFind(edges): 
    vertices = []
    for i in edges:
        for j in i:
            if j not in vertices:
                vertices.append(j)
    return vertices

""" def dfs(graph,vertex):
    visited = []
    if vertex not in visited:
        print(vertex)
        visited.append(vertex)
        for adjacent in graph[vertex]:
            dfs(graph,adjacent)
 """
def rootFind(vertices,descendants):
    for i in vertices:
        if i not in descendants:
            root = i
    print(root)
    return root

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
        start_node = 1
        print("graph has a Euler path")
    if check == 1:
        print("There is a euler cycle")
    path = dfs(start_node, graph, visited_edge)
    print(path)
print(list(graph.keys()))
check_euler(graph, len(graph)+1)