
graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
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

edges = edgeCreator(graph)
def descendantFind(edges):
    descendants = []
    for i in edges:
        if i[1] not in descendants:
            descendants.append(i[1])
    return descendants

descendants = descendantFind(edges)


def vertexFind(edges):
    vertices = []
    for i in edges:
        for j in i:
            if j not in vertices:
                vertices.append(j)
    return vertices
    
vertices = vertexFind(edges)
print("Descendants are:", descendants)
print("Vertices are:",vertices)
bfs(graph,'5')


def dfs(graph,vertex):
    visited = []
    if vertex not in visited:
        print(vertex)
        visited.append(vertex)
        for adjacent in graph[vertex]:
            dfs(graph,adjacent)

for i in vertices:
    if i not in descendants:
        root = i
