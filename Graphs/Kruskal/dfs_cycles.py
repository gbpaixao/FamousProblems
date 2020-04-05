# Prim algorithm

# input where n is weight of each edge
# 0,2,1,0,0
# 2,0,1,2,3
# 1,1,0,0,4
# 0,2,0,0,2
# 0,3,4,2,0

def printGraph(g):
    for row in g:
        print (row)
    print ("---------------------------\n")

def fillGraph (inputfile):
    graph = []
    f = open(inputfile,"r+")

    numberOfVertexes = 0
    for row in f:
        row = row.split(',')
        row = [int(x) for x in row]
        graph.append(row)
        numberOfVertexes += 1

    f.close() 
    return graph, numberOfVertexes

def getFirstNeighbor(g,n,v):
    vert = -1
    for i in range(n):
        if g[i] != 0:
            vert = i
            break
    return vert

def getAnyNeighbor(g,n):
    for i in range(n):
        for j in range(n):
            if g[i][j] != 0:
                return i, j
    return -1, -1

def visitEdge (g, v, w):
    g[v][w] = g[v][w] - g[v][w]
    g[w][v] = g[w][v] - g[w][v] 
    return g

def sumEdges (g,n):
    sum_edges = 0
    for i in range(n):
        for j in range(n):
            sum_edges += g[i][j]
    return sum_edges

def dfs_cycle(g,n,v):
    g = g.copy()
    visited = [False for i in range(n)]  
    visited[v] = True
    
    w = getFirstNeighbor(g[v],n,v)
    while (w != -1):
        w = getFirstNeighbor(g[v],n,v)
        if w == -1:
            v, w = getAnyNeighbor(g,n)
        if v == -1 and w == -1: break

        if visited[w] == False:
            g = visitEdge(g,v,w)
            visited[w] = True
            # dfs_cycle(g,n,w)
        else:
            print ("CICLO")
            if g[v][w] >= 1:
                visitEdge(g,v,w)
            print(v,'->',w)
            # if False in visited: return True, 0
            # else: return False, 1

            # if sumEdges(g,n) != 0: return True, 0
            # else: return False, 1
            return True
        
        print(visited)
        print(v,'->',w)
        print(g)
        # If w doesn't have neighbors, visit w. Else, go to neighbor.
        if getFirstNeighbor(g[w],n,w) == -1 :
            visited[w] == True
        else:
            v = w
    return False, 0

inputfile = "graphs/g1.txt" # Open file
g, n = fillGraph(inputfile) # Fill graph
print ("Grafo Original: ")
g = [[0, 1, 0, 0, 0, 0], [1, 0, 1, 1, 0, 0], [0, 1, 0, 0, 0, 0], [0, 1, 0, 0, -2, 1], [0, 0, 0, -2, 0, 0], [0, 0, 0, 1, 0, 0]]
printGraph(g)               # Print graph

print (dfs_cycle(g,n,0))