import queue


graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

visited = []
queue = []

def bfs(visited,graph,vertex):
    visited.append(vertex)
    queue.append(vertex)
    
    while queue:
        m = queue.pop(0)
        print(m)
        for adjacent in graph[m]:
            if adjacent not in visited:
                visited.append(adjacent)
                queue.append(adjacent)


bfs(visited,graph,'5')