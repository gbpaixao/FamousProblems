def euclideanDistance (p1, p2):
    return ( (p2[0]-p1[0])**2 + (p2[1]-p1[1])**2 ) **0.5

def min (a, b):
    if a <= b: return a
    else: return b

def sortpoints(points):
    points.sort()
    return points

def bruteforce(points,n):
    minimum = 10000
    p = 0
    for i in range(n):
        for j in range(n):
            if i != j:
                d = euclideanDistance(points[i],points[j])
                if d < minimum: 
                    minimum = d
                    p = (points[i],points[j])
    return minimum, p

def nearestPairs(points, n):
    if n <= 3:
        d, p = bruteforce(points,n)
    else:
        middle = n//2
        dl = nearestPairs(points[:middle],len(points[:middle]))
        dr = nearestPairs(points[middle:],len(points[middle:]))
        d = min(dl,dr) 

        S = []
        m = 0 # size of S
        for i in range(n):
            if points[i][0] - points[middle][0] < d: 
                S.append(points[i])
                m += 1
        S.sort(key = lambda x: x[1])

        for i in range(m):
            k = 1
            while i+k < m and S[i+k][1] - S[i][1] < d:
                dist = euclideanDistance(S[i],S[i+k])
                d = min(d, dist)
                k += 1
    return d

def main():
    inputs = int(input())
    size = inputs

    while inputs != 0:
        listofpoints = []
        for i in range (inputs):
            point = input().split()
            x, y = float(point[0]), float(point[1])
            listofpoints.append([x,y])

        d = nearestPairs(sortpoints(listofpoints), size)
        
        if d >= 10000: print ('INFINITY')
        else: print(str('%.4f' % d))

        inputs = int(input())
        size = inputs
main()