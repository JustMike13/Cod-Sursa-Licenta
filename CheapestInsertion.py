import time
import random

from Drawing import drawGraph, drawProgress
from CalculateDistances import calculateDistances
from PointGenerator import generate

distances = None
# l = 0
maxint = 2147483647
def cheapestInsertion(points, x):
    global distances
    global l
    # o lista cu indicele tuturor punctelor care nu au fost adaugate in graf
    remainingPoints = [k for k in range(l)]
    # o lista cu punctele adaugate in graf
    visitedPoints = []
    # lista intermediara de linii
    linesAux = []
    # aleg un punct aleator pentru a fi adaugat in graf
    # x = random.randint(0, l - 1)
    minCost = maxint
    y = None
    # caut cel mai apropiat punct de punctul initial pentru a fi adaugat
    for i in range(l):
        if distances[x][i] < minCost and x != i:
            minCost = distances[x][i]
            y = i
    # elimin punctele din lista de puncte ramase
    remainingPoints.remove(x)
    remainingPoints.remove(y)
    # adaug punctele in graf
    visitedPoints.append(x)
    visitedPoints.append(y)
    # adaug latura in graf
    linesAux.append((x, y))

    # pentru primele 3 puncte vreau sa adaug toate cele 3 laturi care le leaga, mai departe o sa elimin cate o latura si o sa adaug alte doua cu fiecare insertie
    z = None # al treilea punct
    insertionCost = maxint
    for p in remainingPoints:
        # costul reprezinta diferenta dintre suma lungimilor laturilor adaugate si lungimea laturii eliminate
        # din moment ce in fiecare caz eliminam latura XY, am omis scaderea la acest pas
        lenPX = distances[x][p]
        lenPY = distances[y][p]
        cost = lenPX + lenPY
        if cost < insertionCost:
            insertionCost = cost
            z = p
    remainingPoints.remove(z)
    visitedPoints.append(z)
    linesAux.append((x, z))
    linesAux.append((y, z))

    while len(remainingPoints) > 0:
        insertionCost = maxint
        # punctul adaugat si capetele laturii eliminate
        nextPoint = a = b = None
        for p in remainingPoints:
            for line in linesAux:
                l1 = distances[line[0]][p]
                l2 = distances[line[1]][p]
                l3 = distances[line[0]][line[1]]
                cost = l1 + l2 - l3
                if cost < insertionCost:
                    insertionCost = cost
                    nextPoint = p
                    a = line[0]
                    b = line[1]

        remainingPoints.remove(nextPoint)
        visitedPoints.append(nextPoint)
        linesAux.remove((a, b))
        linesAux.append((a, nextPoint))
        linesAux.append((b, nextPoint))

    lines = []
    totalCost = 0

    for line in linesAux:
        p1 = points[line[0]]
        p2 = points[line[1]]
        lines.append((p1, p2))
        totalCost += distances[line[0]][line[1]]

    return lines, totalCost

def cheapestInsertionTSP(points):
    global l
    global distances
    l = len(points)
    distances = calculateDistances(points)
    minCost = maxint
    tour = None
    # x = random.randint(0, l-1)
    # tour, minCost = cheapestInsertion(points, x)
    for i in range(l):
        a, b = cheapestInsertion(points, i)
        if b < minCost:
            minCost = b
            tour = a
    return tour, minCost

if __name__ == "__main__":
    testPoints = [(1, 3), (3, 2), (7, 4), (3, 5), (5.5, 6), (4, 4), (4, 3), (5, 3.5), (5, 2, 5), (3, 4)]
    testLines, testCost = cheapestInsertionTSP(testPoints)
    print(f"     NI result: {testCost}")
    drawProgress(testPoints, testLines)