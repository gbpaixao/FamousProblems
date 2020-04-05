# Prim algorithm
# The strategy of using heap was to add tuples of (edge_weight, x_position, y_position) in order
# to collect the edge with mininum weight at each iteration

# input where n is weight of each edge
# 0,2,1,0,0
# 2,0,1,2,3
# 1,1,0,0,4
# 0,2,0,0,2
# 0,3,4,2,0

from heapq import heappop, heappush
import random as rand

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

def findEdge (heap, T):
    aux = heappop(heap)
    while aux[2] in T:
        aux = heappop(heap)
    return aux[1],aux[2]

# method to insert the edges of the vertexes on T on the heap
def insertHeap (g, heap, vertex, T):
    for j, element in enumerate(g[vertex]):
        if element != 0 and j not in T: # this is to eliminate the mirror in non directional graphs
            heappush(heap,(element,vertex,j))
    return heap

def prim (g, n):
    Tmin = set() # set of minimum tree
    T = set() # set of visited vertexes
    N = set() # set of non-visited vertexes
    for idx in range(n):
        N.add(idx)

    i = rand.randrange(0,n)

    cost = 0
    heap = []
    heap = insertHeap(g,heap,i,T)

    T.add(i)
    N.remove(i)

    while len(T) != n:
        ex, ey = findEdge(heap,T)
        T.add(ey)
        N.remove(ey)
        Tmin.add(ey)
        Tmin.add(ex)
        heap = insertHeap(g,heap,ey,T)
        print (ex,'->',ey,':',g[ex][ey])
        cost = cost + g[ex][ey]

    print ("Custo da árvore geradora mínima:",cost)

def main():
    inputfile = "graphs/g1.txt" # Open file
    g, n = fillGraph(inputfile) # Fill graph
    print ("Grafo Original: ")
    printGraph(g)               # Print graph

    prim(g,n)
main()