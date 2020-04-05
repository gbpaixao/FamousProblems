# Floyd-Warshall algorithm

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

def floydWarshall (g,n):

    # Start of L and rot
    L = [[0 for x in range(n)] for i in range(n)]
    rot = [[-1 for x in range(n)] for i in range(n)]

    # Initialization
    for row in range(n):
        for column in range(n):
            if row == column:
                L[row][column] = 0
                rot[row][column] = 0xFFFFFFFF
            else:
                if (g[row][column] != 0):
                    L[row][column] = g[row][column]
                    rot[row][column] = row
                else:
                    L[row][column] = 0xFFFFFFFF
                    rot[row][column] = 0xFFFFFFFF

    # Main Loops
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if L[i][k] + L[k][j] < L[i][j]:
                    L[i][j] = L[i][k] + L[k][j]

                    # if 'k' leads to 'j', then add it to rot
                    if g[k][j] != 0: 
                        rot[i][j] = k   
    return L, rot

def printdtrot (L, rot, n):
    for row in range(n):
        print ('...... Vertex',row,'......')
        print ('dt:  ',L[row],'\n','rot: ',rot[row],'\n', sep='')

def main():
    inputfile = "graphs/g6.txt" # Open file
    g, n = fillGraph(inputfile) # Fill graph
    print ("Grafo Original: ")
    printGraph(g)               # Print graph

    L, rot = floydWarshall(g,n)
    printdtrot (L, rot, n)
main()