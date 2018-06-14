
import csv

def matrixPower (A, p):

    if (len(A) != len(A[0])):
        print("mismatched dimensions")
        return

    length = len(A)
    R = [[[A[row][col],] for row in range(length)] for col in range(length)]

    for h in range (p-1):
        for i in range(length):
            for j in range(length): # for each matrix entry
                entry = R[i][j]
                R[i][j] = []
                for k in range(length): # for each entry in that col in first matrix
                    for l in range(len(entry)): # for each term in that entry of first matrix
                        new = entry[l]+ A[k][j] # need to add something else here?
                        if (('-' not in new) and ('yy' not in new) and ('pp' not in new)) :
                            R[i][j].append(new)
    return R

def findPaths (A):

    if (len(A) != len(A[0])):
        print("mismatched dimensions")
        return

    length = len(A)
    R = [[[A[row][col],] for row in range(length)] for col in range(length)]
    final = [[['',] for row in range(length)] for col in range(length)]
    for i in range(length):
        final[i][i] = ['X']

    full = False
    while (not full):
        for i in range(length):
            for j in range(length): # for each matrix entry
                entry = R[i][j]
                R[i][j] = ['',]
                for k in range(length): # for each entry in that col in first matrix
                    for l in range(len(entry)): # for each term in that entry of first matrix
                        new = entry[l] + A[k][j]
                        if (('-' not in new) and ('yy' not in new) and ('pp' not in new)) :
                            R[i][j].append(new)
                            if (R[i][j][0] == ''):
                                del R[i][j][0]
                if final[i][j] == ['',] and not R[i][j] == ['',]:
                    final[i][j] = R[i][j]
        full = True
        for i in range(length):
            for j in range(length):
                if final[i][j] == ['',] :
                    full = False
        # for row in final :
        #     print(row)
    return final

def readIn(file) :
    with open(file, newline='') as csvFile:
        reader = csv.reader(csvFile)
        graph = []
        for row in reader:
            r = []
            for entry in row :
                r.append(entry)
            graph.append(r)
        print(graph[0])
        for a in graph[0]:
            print(a)
        graph[0][0].replace('\\ufeff0','0')

    return graph

#print(readIn('graph1.csv'))
    # Create the result matrix
    # Dimensions would be rows_A x cols_B
    # C = [['' for row in range(cols)] for col in range(rows)]

    # for h in range (p):


x = [['-','-','-','y','p','y'],
    ['-','-','-','y','y','p'],
    ['-','-','-','y','p','y'],
    ['y','y','y','-','-','-'],
    ['p','y','p','-','-','-'],
    ['y','p','y','-','-','-']]

#y = [[1,2],[1,2],[3,4]]
square = (matrixPower(x,3))
for row in square:
     print(row)
paths = findPaths(x)
for row in paths:
     print(row)
