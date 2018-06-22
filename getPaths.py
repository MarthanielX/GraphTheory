import queue as q

def getPaths(A):

    power = [[[A[row][col],] for row in range(len(A))] for col in range(len(A))]
    final = [[['',] for row in range(len(A))] for col in range(len(A))]
    for i in range(len(A)):
        final[i][i] = ['X']
    for row in range(len(final)) :
        for col in range(len(final)):
            if A[row][col] != '-':
                final[row][col] = A[row][col]
    while (not isFull(final)) :
        power = multiply(power,A)
        for row in range(len(final)) :
            for col in range(len(final)):
                if final[row][col][0] == '' and power[row][col]:
                    final[row][col] = power[row][col]
    return final

def isFull(A):
    full = True
    for row in A:
        for col in row:
            if col[0] == '':
                full = False
    return full

# Matrix Multiplication
def multiply(A, B):
    result = [[[] for row in range(len(A))] for col in range(len(A))]
    for row in range(len(A)):
        for col in range(len(A)): # for each matrix entry
            for k in range(len(A)): # for each term in the dot product
                for a in range(len(A[k][col])): # for each term in the first part of the dot product
                    for b in range(len(B[row][k])): # for each term in the second part of the dot product
                        new = A[k][col][a] + B[row][k][b]
                        if (('-' not in new) and ('yy' not in new) and ('pp' not in new)) :
                            result[row][col].append(new)
    return result

# turns adjacency matrix into list of dicts mapping edge colors to vertex indcices
def matrixToList(A):
    adjacencyList = []
    for row in A:
        dict = {}
        for index, entry in enumerate(row):
            if entry != '-':
            # if want to label vertices starting at 1, add , start=1 to enumerate params
                if entry not in dict:
                    dict[entry] = []
                dict[entry].append(index)
        adjacencyList.append(dict)
    return adjacencyList

# returns proper distance between two integers representing the indcices of vertices
def getProperDistance(a, b):
    queue = q.Queue(-1)
    # triples represent vertex and color previously used
    queue.put((a,'y', 0))
    queue.put((a,'p', 0))
    while (not queue.empty()):
        get = queue.get()
        if (get[0] == b):
            return get[2]
        nextColor = 'p' if get[1] == 'y' else 'y'
        if nextColor in adjacencyList[get[0]]:
            for vertex in adjacencyList[get[0]][nextColor]:
                queue.put((vertex,nextColor,get[2]+1))
    return -1

# returns list of proper distances to all other vertices from given vertex
def getProperDistances(a):
    result = [-1 for index in range(len(adjacencyList))]
    queue = q.Queue(-1)
    # triples represent vertex and color previously used
    queue.put((a,'y', 0))
    queue.put((a,'p', 0))
    while (-1 in result and not queue.empty()):
        get = queue.get()
        if (result[get[0]] == -1):
            result[get[0]] = get[2]
        nextColor = 'p' if get[1] == 'y' else 'y'
        if nextColor in adjacencyList[get[0]]:
            for vertex in adjacencyList[get[0]][nextColor]:
                queue.put((vertex,nextColor,get[2]+1))
    return result

x = [['-','-','-','y','p','y'],
    ['-','-','-','y','y','p'],
    ['-','-','-','y','p','y'],
    ['y','y','y','-','-','-'],
    ['p','y','p','-','-','-'],
    ['y','p','y','-','-','-']]

for row in x :
    print(row)

print('')

result = getPaths(x)
for row in result :
    print(row)

print('')

adjacencyList = matrixToList(x)
for vertex in adjacencyList:
    print(vertex)

print(getProperDistances(0))
