from Drawing import drawGraph
from CalculateDistances import calculateDistances
from time import sleep


maxint = 2147483647
def greedyTSP(points):
    print("testGreedy1")
    distances = calculateDistances(points)
    print("testGreedy2")
    l = len(points)
    lines = []

    neighbors = [[0 for i in range(l)] for i in range(l)]
    a1, b1, c1 = smallest(distances)
    print("testGreedy3")
    lines.append((a1, b1, c1))
    neighbors[a1][b1] = neighbors[b1][a1] = 1
    notFinal = True
    while notFinal:
        print("testGreedy4")
        existingCycle = True
        while existingCycle:
            print("testGreedy5")
            a, b, c = smallest(distances)
            sa = 0
            sb = 0
            for si in range(len(neighbors[a1])):
                sa += neighbors[a][si]
                sb += neighbors[b][si]
            if sa == sb == 0:
                existingCycle = False
            elif sa < 2 and sb < 2:
                found = False
                ranks = [0 for i in range(l)]
                ranks[b] = 1
                nextPoints = [b]
                checked = []
                while len(nextPoints) >= 1:
                    point = nextPoints[0]
                    nextPoints = nextPoints[1:]
                    nb = neighbors[point]
                    for n in range(len(nb)):
                        if nb[n] == 1 and n not in checked:
                            if n == a:
                                found = True
                                if ranks[point] + 1 == l:
                                    notFinal = False
                                    existingCycle = False
                            else:
                                nextPoints.append(n)
                                checked.append(n)
                                ranks[n] = ranks[point] + 1
                if not found:
                    existingCycle = False
        lines.append((a, b, c))
        neighbors[a][b] = neighbors[b][a] = 1
    linesSecond = []
    totalCost = 0
    for line in lines:
        a = line[0]
        b = line[1]
        c = line[2]
        totalCost += c
        auxLine = [points[a], points[b]]
        linesSecond.append(auxLine)
    return linesSecond, neighbors, totalCost

def smallest(dist):
    l = len(dist)
    min = maxint
    mini = 0
    minj = 0
    for i in range(l - 1):
        for j in range(i + 1, l):
            if dist[i][j] < min:
                min = dist[i][j]
                mini = i
                minj = j
    dist[mini][minj] = dist[minj][mini] = maxint
    return mini, minj, min

def orderAscending(dist):
    l = len(dist)
    orderedList = []
    for i in range(l - 1):
        for j in range(i + 1, l):
            if len(orderedList) == 0:
                orderedList.append((i, j))
            else:
                firstElem = orderedList[0]
                lastElem = orderedList[-1]
                if dist[i][j] <= dist[firstElem[0]][firstElem[1]]:
                    orderedList.insert(0, (i, j))
                elif dist[i][j] >= dist[lastElem[0]][lastElem[1]]:
                    orderedList.append((i, j))
                else:
                    for k in range(len(orderedList) - 1):
                        listElem = orderedList[k]
                        nextElem = orderedList[k + 1]
                        if dist[listElem[0]][listElem[1]] < dist[i][j] and dist[nextElem[0]][nextElem[1]] > dist[i][j]:
                            orderedList.insert(k + 1, (i, j))
                            break
    return orderedList

testPoints = [(1, 3), (3, 2), (7, 4), (3, 5), (5.5, 6)]
testDistances = calculateDistances(testPoints)
print(orderAscending(testDistances))
# for i in testDistances:
#     print(i)
# for i in range(5):
#     print(i,":    ",smallest(testDistances))
# for i in testDistances:
#     print(i)

# testLines, testNeighbors, testCost = greedyTSP(testPoints, testDistances)
# print(testLines)
# print(testDistances)
# print("Cost total:", testCost)
# for i in range(len(testLines) + 1):
#     drawGraph(testPoints, testLines[:i])
#     sleep(1)