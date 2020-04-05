def merge(l1,l2):
    i = 0
    j = 0
    idx = 0
    l3 = []

    while i < len(l1) and j < len(l2):
        if l1[i] <= l2[j]:
            l3.append(l1[i])
            i += 1
        else: 
            l3.append(l2[j])
            j += 1

    if i == len(l1): # l1 is over
        for idx in range(j,len(l2)): # complete with the rest of l2
            l3.append(l2[idx])
    else: # l2 is over
        for idx in range(i,len(l1)): # complete with the rest of l1
            l3.append(l1[idx])
    return l3

def mergeSort(l):
    if len(l) < 2:
        return l
    else:
        middle = len(l)//2
        l1 = mergeSort(l[:middle])
        l2 = mergeSort(l[middle:])
        l = merge(l1,l2)
    return l

def main():
    l = [6,5,4,3,2,1]
    print(mergeSort(l))
main()