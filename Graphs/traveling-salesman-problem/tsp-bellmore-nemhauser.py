# TSP algorithm

def printGraph(g):
    for row in g:
        print (row)
    print ("---------------------------\n")

# This is used in https://people.sc.fsu.edu/~jburkardt/datasets/tsp/tsp.html datasets model of entry
def fillGraph (inputfile):
    graph = []
    f = open(inputfile,"r+")

    numberOfVertexes = 0
    for row in f:
        row = row.split('  ')
        row = [float(x.strip('\n')) for x in row]
        graph.append(row)
        numberOfVertexes += 1

    f.close() 
    return graph, numberOfVertexes

# Find edge with lowest cost that is not in H
def findEdge(g,n,v,H):
    menor = 0xFFFFFFFF
    menor_idx = 0

    for i in range(n):
        if i != v and g[v][i] < menor and i not in H:
            menor = g[v][i]
            menor_idx = i
    
    return menor_idx

def tsp(g,n):
    H = []
    hi = 0
    H.append(hi)

    while len(H) < n:
        hk = findEdge(g,n,hi,H)
        H.append(hk)
        hi = hk

    return H

def printH(H,n):
    for i in range(n-1):
        print (H[i],"->",end=' ')
    print (H[i+1])

def main():
    # Pelo dataset
    inputfile = "dataset/26cities.txt" # Open file
    g, n = fillGraph(inputfile) # Fill graph

    print ("Grafo Original: ")
    printGraph(g)               # Print graph

    H = tsp(g,n)
    printH(H,n)
main()
