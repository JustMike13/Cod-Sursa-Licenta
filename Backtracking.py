from Drawing import drawProgress
from CalculateDistances import calculateDistances
from PointGenerator import readPoints, generate
import time

maxint = 2147483647
distances = None
l = None

index = 0

def backtrackingTSP(points):
    global minCost
    global minTour
    global distances
    global index
    distances = calculateDistances(points)
    l = len(points)
    minCost = maxint
    minTour = None
    pointsAux = [i for i in range(l)]
    linesAux, totalCost = backtrackingRecursive(pointsAux)
    lines = []
    linesAux = list(linesAux)
    p1 = linesAux.pop(0)
    initPoint = p1
    for i in range(len(linesAux)):
        p2 = linesAux.pop(0)
        lines.append((points[p1], points[p2]))
        p1 = p2
    lines.append((points[p1], points[initPoint]))
    return lines, totalCost

def backtrackingRecursive(list, tour = ()):
    global minCost
    global minTour
    global distances
    global l
    global index
    for i in range(len(list)):
        aux = tour + (list[i],)
        if len(list) == 1:
            tourLen = tourLength(aux)
            index+=1
            if tourLen < minCost:
                minCost = tourLen
                minTour = aux
        else:
            recursiveList = list[:i] + list[i + 1:]
            backtrackingRecursive(recursiveList, aux)
    if(index%1000 == 0):
        print(index)
    return minTour, minCost


def tourLength(tour):
    global distances
    cost = 0
    tour = list(tour)
    a = tour.pop(0)
    initElem = a
    for i in range(len(tour)):
        b = tour.pop(0)
        cost += distances[a][b]
        a = b
    cost += distances[initElem][a]
    return cost

if __name__ == "__main__":
    # testPoints = [(1, 3), (3, 2), (7, 4), (3, 5), (5.5, 6), (4, 4), (4, 3), (5, 3.5)]
    # testLines, testCost = backtrackingTSP(testPoints)
    # print(f"Cost: {testCost}")
    # drawProgress(testPoints, testLines)
    nr = 10
    results = []

    points = [(1, 3), (3, 2), (7, 4), (3, 5), (5.5, 6), (4, 4), (4, 3), (5, 3.5), (8, 9), (3, 9)]
    BTStart = time.time()
    a, b = backtrackingTSP(points)
    BTEnd = time.time()
    BTDif = BTEnd - BTStart
    print(f"     BT result: {b}")
    print(f"     BT time: {BTDif}")


