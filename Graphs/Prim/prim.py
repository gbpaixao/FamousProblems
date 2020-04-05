# Prim algorithm

# input where n is weight of each edge
# 0,2,1,0,0
# 2,0,1,2,3
# 1,1,0,0,4
# 0,2,0,0,2
# 0,3,4,2,0

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

def findEdge (g,n,T,N):
    menor = 0xFFFFFFFF
    for row in T:
        for column in N: 

            element = g[row][column]
            if element < menor and element != 0:
                menor = element
                y = row 
                x = column

    return x,y

def prim (g, n):
    Tmin = set() # set of minimum tree
    T = set() # set of visited vertexes
    N = set() # set of non-visited vertexes
    for idx in range(n):
        N.add(idx)

    i = rand.randrange(0,n) 
    cost = 0

    T.add(i)
    N.remove(i)

    while len(T) != n:
        ex, ey = findEdge(g,n,T,N)
        T.add(ex)
        N.remove(ex)
        Tmin.add(ex)
        Tmin.add(ey)
        print (ey,'->',ex,':',g[ex][ey])
        cost = cost + g[ex][ey]

    print ("Custo da árvore geradora mínima:",cost)

def main():
    inputfile = "graphs/g3.txt" # Open file
    g, n = fillGraph(inputfile) # Fill graph
    print ("Grafo Original: ")
    printGraph(g)               # Print graph

    prim(g,n)
main()