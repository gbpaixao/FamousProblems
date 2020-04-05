# Dijkstra algorithm implemented using list

# input where n is weight of each edge
# 0-2-1-0-0
# 2-0-1-2-3
# 1-1-0-0-4
# 0-2-0-0-2
# 0-3-4-2-0

import random as rand
import timeit

def printGraph (g):
    print ('Vertex   List of Neighbors')
    i = 0
    for row in g:
        print (" '",i,"'  :",sep='', end='')
        print ("  [",*row,"]")
        i += 1

def fillGraph (inputfile):
    graph = []
    f = open(inputfile,"r+")

    numberOfVertexes = 0
    for row in f:
        row = row.split('-')
        row = [int(x) for x in row]
        graph.append(row)
        numberOfVertexes += 1

    f.close() 
    return graph, numberOfVertexes

# Find rout with shortest distance
def cheapestEdge (A, rotdt):
    menor = [0,999999]
    for vertex in A:

        if rotdt[vertex][1] < menor[1]:
            menor = rotdt[vertex]
            v = vertex

    return v

def getNeighbors (l):
    neighbors = set()

    for i in range(len(l)):
        if (l[i] > 0):
            neighbors.add(i)
    
    return neighbors
        
# Method Dijkstra returns list containing all the shortest routes to get to any vertex
def dijkstra (g, n):
    rotdt = []
    
    dt = 0  # distance (weight)
    rot = 0 # route (last vertex)

    rotdt.append([rot,dt])

    # set distance to initial as 0, and the others to infinity
    for i in range (2,n+1):
        dt = 9999999
        rot = '#'
        rotdt.append([rot,dt])
    
    V = {i for i in range(n)}
    A = V.copy()
    F = set()
  
    while F != V:
        v = cheapestEdge(A, rotdt)
        F.add(v)
        A.remove(v)        

        N = getNeighbors(g[v])
        N = N - F

        for i in N:
            # if dt already in vertex v + value of edge < dt in i, update distance
            if rotdt[v][1] + g[v][i] < rotdt[i][1]:
                rotdt[i][1] = rotdt[v][1] + g[v][i]
                rotdt[i][0] = v
    
    return rotdt
    
def nearestRoute (vi, vf, route_dist):
    route = []
    print ("Nearest route between ",vi," and ",vf,": ", sep='')
    route.append(vf)
    dist = route_dist[vf][1]

    while vf != vi:
        vf = route_dist[vf][0]
        route.append(vf)
    route.reverse()

    print (route)
    print ("Distance:",dist)
    print ("\n-------------------------------")

def generateGraph (n):
    graph = []

    for row in range(n):
        row = [rand.randrange(20,100) for x in range(n)]
        graph.append(row)
        
    return graph

def main ():
    # Open file
    inputfile = "graphs/g2.txt"
    g, n = fillGraph(inputfile)
    
    # # Generate random G
    # n = 10000 # number of vertexes
    # g = generateGraph(n) 
    
    # printGraph (g)
    route_dist = dijkstra(g, n)

    print ("\n-------------------------------")
    # nearestRoute (0,n-1,route_dist) # find best route from first to last vertexes 
    
    for i, rotdt in enumerate(route_dist):
        print ("Vértice ",i," - rot: ",rotdt[0],", dist: ",rotdt[1],";", sep='')

# main()
# By using timeit, the function calls the method main
print("Execution time: %.4f" % round(timeit.timeit(main, number=1),4),"s",sep='')