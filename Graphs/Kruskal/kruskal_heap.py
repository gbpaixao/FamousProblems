# Prim algorithm

# input where n is weight of each edge
# 0,2,1,0,0
# 2,0,1,2,3
# 1,1,0,0,4
# 0,2,0,0,2
# 0,3,4,2,0

import copy
from heapq import heappop, heappush

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

def getEdges(g):
    edges = []
    for i, row in enumerate(g):
        for j, element in enumerate(row):
            if int(element != 0) and j >= i:
                heappush(edges,([int(element),i,j]))
    return edges

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

def dfs_cycle(g,n,v):
    visited = [False for i in range(n)]  
    visited[v] = True
    
    w = getFirstNeighbor(g[v],n,v)
    while (w != -1):
        w = getFirstNeighbor(g[v],n,v) # get neighbor of current vertex
        if w == -1: # if current vertex doesn't have neighbors, get any neighbor from any vertex
            v, w = getAnyNeighbor(g,n)
        if v == -1 and w == -1: break # if graph is empty, break loop

        if visited[w] == False:
            g = visitEdge(g,v,w)
            visited[w] = True
        else:
            if g[v][w] >= 1:
                visitEdge(g,v,w)
            return True
        
        # If w doesn't have neighbors, visit w. Else, go to neighbor.
        if getFirstNeighbor(g[w],n,w) == -1 :
            visited[w] == True
        else:
            v = w
    return False

def kruskal(g,n):
    edges = getEdges(g)

    T = [] # list of edges of minimum tree
    for i in range(n):
        aux = [0 for j in range(n)] 
        T.append(aux)
    
    elem, x, y = heappop(edges)
    print ('x',x,'y',y,'elem',elem)
    T[x][y] = elem
    T[y][x] = elem
    print (x,'->',y,':',g[x][y])
    i = 1
    j = 0

    while j < n-1:
        if len(edges) == 0: break
        elem, x, y = heappop(edges)
        Taux = copy.deepcopy(T)
        Taux[x][y] = elem
        Taux[y][x] = elem
        
        q = dfs_cycle(Taux,n,0)

        if q == False: # if Taux is acyclic
            print (x,'->',y,':',g[x][y])
            T[x][y] = elem
            T[y][x] = elem
            j += 1
        i += 1

def main():
    inputfile = "graphs/g3.txt" # Open file
    g, n = fillGraph(inputfile) # Fill graph
    print ("Grafo Original: ")
    printGraph(g)               # Print graph
    
    kruskal(g,n)
main()