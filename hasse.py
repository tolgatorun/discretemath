import networkx as nx
import matplotlib.pyplot as plt

#s = [['a','a'],['a','b'],['a','c'],['a','d'],['a','e'],['a','f'],['b','b'],['b','d'],['b','e'],['b','f'],['c','c'],['c','f'],['d','d'],['e','e'],['e','f'],['f','f']] 
#s = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [2, 2], [2, 5], [2, 6], [3, 3], [3, 4], [4, 4],[5, 5],[6, 6]] #poset
#s = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [2, 2], [2, 5], [2, 6], [3, 3], [3, 4], [4, 4],[5, 5]] #not reflexive
#s = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [2, 2], [2, 5], [2, 6], [3, 3], [3, 4], [4, 4],[5, 5],[6, 6]] #not transitive
#s = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [2, 1],[2, 2], [2, 5], [2, 6], [3, 3], [3, 4], [4, 4],[5, 5],[6, 6]] #not anti symmetric

def convert(list):
    return tuple(list)

def is_antisymmetric(relation):
    seen = set()
    for a, b in relation:
        if a == b:
            continue
        if (b, a) in seen:
            print("This element: ", [b,a], "is symmetric of: ", [a,b])
            return False
        seen.add((a, b))
    return True

def is_reflexive(relation, s1):
    for x in s1:
        if [x,x] not in relation:
            print("There isn't a element such: ", [x,x])
            return False
    return True

def is_transitive(relation, s1):
    for a in s1:
        for b in s1:
            if [a,b] in relation:
                for c in s1:
                    if [b,c] in relation and [a,c] not in relation:
                        print("There is  elements such", [b,c],"and", [a,b], "but there isn't a element such", [a,c])
                        return False
    return True

def hasse(relation,s1):
    for x in s1:
        for y in s1:
            if [x,y] in relation and x != y:
                for z in s1:
                    if [y,z] in relation and [x,z] in relation and x != z and y != z:
                        s.remove([x,z])
    return relation
def reflexive_clear(relation, s1):
    for x in relation:
        if x[0] == x[1]:
            pass
        else:
            finalset.append(convert(x))

def graph():
    G = nx.Graph() 
    G.add_edges_from(finalset)
    options = {  #customization
        "font_size": 5,
        "node_size": 15,
        "node_color": "white",
        "edgecolors": "black",
        "linewidths": 2,
        "width": 2,
    }
    nx.draw_networkx(G) 

    ax = plt.gca() #creating axes
    ax.margins(0.20)
    plt.axis("off") #hide axes
    plt.show()

n = int(input("Enter number of elements : "))
s = []
for i in range(0, n):
    print('Element:     ', i+1)
    list = []
    a = int(input('A:   '))
    b = int(input('B:   '))
    list.append(a)
    list.append(b)
    s.append(list)   

s1 = []
finalset = []

for x in s:
    if x[0] not in s1:
        s1.append(x[0])
    if x[1] not in s1:
        s1.append(x[1])

if is_reflexive(s,s1):
    print("Reflexive")
    if is_antisymmetric(s):
        print("Antisymmetric")
        if is_transitive(s,s1):
            print("Transitive")
            hasse(s, s1)
            reflexive_clear(s,s1)
            print("Set of desired relations: ",finalset)
            graph()
        else:
            print('Not transitive')
    else:
        print('Not antisymmetric')        
else:
    print('Not reflexive')
