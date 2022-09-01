import time
import random

from Drawing import drawGraph
from CalculateDistances import calculateDistances
from PointGenerator import generate, readPoints

distances = None
l = None
maxint = 2147483647

def nearestInsertion(points, x = None):
    global distances
    global l
    # o lista cu indicele tuturor punctelor care nu au fost adaugate in graf
    remainingPoints = [i for i in range(l)]
    # o lista cu punctele adaugate in graf
    visitedPoints = []
    # lista intermediara de linii
    linesAux = []
    # daca nu a fost dat niciun punct de start aleg un punct aleator pentru a fi adaugat in graf
    # if x == None:
    #     x = random.randint(0,  l)
    # o lista cu distanta dintre fiecare punct si graf
    nearestNeighbor = distances[x].copy()
    nearestNeighbor[x] = -1
    minCost = maxint
    y = None
    # caut cel mai apropiat punct de punctul initial pentru a fi adaugat
    for i in range(l):
        if distances[x][i] < minCost and x != i:
            minCost = distances[x][i]
            y = i
    # vizitez y
    nearestNeighbor[y] = -1
    for i in range(l):
        if distances[i][y] < nearestNeighbor[i] and i!=y:
            nearestNeighbor[i] = distances[i][y]
    # elimin punctele din lista de puncte ramase
    remainingPoints.remove(x)
    remainingPoints.remove(y)
    # adaug punctele in graf
    visitedPoints.append(x)
    visitedPoints.append(y)
    # adaug latura in graf
    linesAux.append((x, y))
    # caut un al treilea punct care sa fie cat mai aproape de unul din punctele deja adaugate
    z = None
    minCost = maxint
    for i in range(l):
        if nearestNeighbor[i] < minCost and nearestNeighbor[i] != -1:
            minCost = nearestNeighbor[i]
            z = i
    # vizitez z
    nearestNeighbor[z] = -1
    for i in range(l):
        if distances[i][z] < nearestNeighbor[i] and i != z:
            nearestNeighbor[i] = distances[i][z]
    # adaug punctul si laturile care i-l leaga de primele doua puncte in graf
    remainingPoints.remove(z)
    visitedPoints.append(z)
    linesAux.append((x, z))
    linesAux.append((y, z))
    # in prezent graful reprezinta un triunghi

    # cat timp exista puncte de adaugat
    while len(remainingPoints) > 0:
        # caut punctul cel mai aproape de graf
        minCost = maxint
        for i in range(l):
            if nearestNeighbor[i] < minCost and nearestNeighbor[i] != -1:
                minCost = nearestNeighbor[i]
                closestPoint = i
        # vizitez closestPoint
        nearestNeighbor[closestPoint] = -1
        for i in range(l):
            if distances[i][closestPoint] < nearestNeighbor[i] and i != closestPoint:
                nearestNeighbor[i] = distances[i][closestPoint]
        # caut cea mai profitabila insertie
        # insertie inseamna ca aleg o latura din graf, conectez noul punct de capetele laturii si elimin latura initiala
        # avand sirul a - b - c - d, daca vreau sa adaug punctul x intre nodurile b si c
        # sirul devine a - b - c - d
        #                  \  /
        #                    x
        # si apoi a - b - x - c - d
        a = b = None
        minCost = maxint
        for line in linesAux:
            p1, p2 = line # capetele liniei
            newLine1 = distances[closestPoint][p1]
            newLine2 = distances[closestPoint][p2]
            oldLine = distances[p1][p2]
            totalLineCost = newLine1 + newLine2 - oldLine
            if totalLineCost < minCost:
                minCost = totalLineCost
                a = p1
                b = p2
        # efectuez insertia
        visitedPoints.append(closestPoint)
        remainingPoints.remove(closestPoint)
        linesAux.remove((a, b))
        linesAux.append((a, closestPoint))
        linesAux.append((b, closestPoint))

    lines = []
    totalCost = 0

    for line in linesAux:
        p1 = points[line[0]]
        p2 = points[line[1]]
        lines.append((p1, p2))
        totalCost += distances[line[0]][line[1]]

    return lines, totalCost


def nearestInsertionTSP(points):
    global distances
    global l
    #calculez distantele dintre puncte
    distances = calculateDistances(points)
    l = len(points)
    cost = maxint
    lines = None
    for i in range(l):
        linesAux, costAux = nearestInsertion(points, i)
        if costAux < cost:
            cost = costAux
            lines = linesAux
    # x = random.randint(0, l - 1)
    # lines, cost = nearestInsertion(points, x)
    return lines, cost

if __name__ == "__main__":
    # testPoints = [(1, 3), (3, 2), (7, 4), (3, 5), (5.5, 6), (4, 4), (4, 3), (5, 3.5), (5, 2,5), (3, 4)]
    testPoints = readPoints(filename="test_points/100_test_points_00.txt")
    testLines, testCost = nearestInsertionTSP(testPoints)
    print(f"     NI result: {testCost}")
    drawGraph(testPoints, testLines, f"Cost: {testCost}")
