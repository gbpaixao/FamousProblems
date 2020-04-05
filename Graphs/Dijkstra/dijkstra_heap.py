# Dijkstra algorithm implemented using list

# input where n is weight of each edge
# 0-2-1-0-0
# 2-0-1-2-3
# 1-1-0-0-4
# 0-2-0-0-2
# 0-3-4-2-0

from heapq import heappop, heappush, heapify
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

def getNeighbors (l):
    neighbors = set()

    for i in range(len(l)):
        if (l[i] > 0):
            neighbors.add(i)
    
    return neighbors

# Method Dijkstra returns list containing all the shortest routes to get to any vertex
def dijkstra (g, n):
    dtrot = []
    heap = []
    
    dt = 0  # distance (weight)
    rot = 0 # route (last vertex)

    dtrot.append([dt,rot])

    # set distance to initial as 0, and the others to infinity
    for i in range (2,n+1):
        dt = 9999999
        rot = '#'
        dtrot.append([dt,rot])

    V = {i for i in range(n)}
    A = V.copy()
    F = set()
    v = 0 # initial vertex
  
    while F != V:
        
        F.add(v)
        A.remove(v)        

        N = getNeighbors(g[v])
        N = N - F

        for neighbor in N:
            if dtrot[v][0] + g[v][neighbor] < dtrot[neighbor][0]:
                dtrot[neighbor][0] = dtrot[v][0] + g[v][neighbor]
                dtrot[neighbor][1] = v

            heappush(heap, (dtrot[neighbor][0],dtrot[neighbor][1],neighbor))

        while (v in F and F != V):
            vertex = heappop(heap)
            v = vertex[2]

    return dtrot
    
def nearestRoute (vi, vf, dist_route):
    route = []
    print ("Nearest route between ",vi," and ",vf,": ", sep='')
    route.append(vf)
    dist = dist_route[vf][0]

    while vf != vi:
        vf = dist_route[vf][1]
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
    # # Open file
    # inputfile = "graphs/g1.txt"
    # g, n = fillGraph(inputfile)

    # Generate random G
    n = 10000 # number of vertexes
    g = generateGraph(n) 

    # printGraph (g)
    dist_route = dijkstra(g, n)

    print ("\n-------------------------------")
    nearestRoute (0,n-1,dist_route)

# main()
# By using timeit, the function calls the method main
print("Execution time: %.4f" % round(timeit.timeit(main, number=1),4),"s",sep='')