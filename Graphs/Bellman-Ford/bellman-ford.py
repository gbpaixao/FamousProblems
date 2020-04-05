# Bellman-ford algorithm

# input where n is weight of each edge
# 0,2,1,0,0
# 2,0,1,2,3
# 1,1,0,0,4
# 0,2,0,0,2
# 0,3,4,2,0

def printGraph(g):
    print ("Grafo Original: ")
    for row in g:
        print (row)
    print ("---------------------------")

def printdtrot(dt, rot):
    print("\nDistância entre os vértices:\n")
    for i in range(len(dt)):
        print ("Vértice ",i," - rot: ",rot[i],", dist: ",dt[i],";", sep='')

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

def getPredecessors (g, vertex):
    predecessors = []
    for i, row in enumerate(g):
        if row[vertex] != 0:
            predecessors.append(i)
    
    return predecessors

def bellmanFord (g,n): 
    dt = [] # distance between first vertex (root) and current vertex
    rot = [] # previous vertex, so that current vertex has minimum distance from root
    changes = False

    # set first vertex
    dt.append(0)
    rot.append(0xFFFFFFFF)

    # set distance to infinity
    for i in range (2,n+1):
        dt.append(0xFFFFFFFF)
        rot.append(0)

    # Main loop
    for k in range (0, n-1):
        changes = False
        for i in range(1,n):
            pred = getPredecessors(g,i) # Represented by gamma
            for j in pred:
                # print ("dist: ",g[j][i])
                if dt[j] + g[j][i] < dt[i]:
                    
                    dt[i] = dt[j] + g[j][i]
                    rot[i] = j
                    changes = True # houve alteração
            
        # break
    if changes == False: k = n

    return dt, rot

def main():
    inputfile = "graphs/g5.txt" # Open file
    g, n = fillGraph(inputfile) # Fill graph
    printGraph(g)               # Print graph

    dt, rot = bellmanFord(g,n)

    printdtrot (dt, rot)

main()