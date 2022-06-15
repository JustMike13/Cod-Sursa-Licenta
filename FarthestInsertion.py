import time
import random

from Drawing import drawGraph
from CalculateDistances import calculateDistances
from PointGenerator import generate

distances = None
l = None
maxint = 2147483647

def farthestInsertion(points, x = None):
    global distances
    global l
    # o lista cu indicele tuturor punctelor care nu au fost adaugate in graf
    remainingPoints = [i for i in range(l)]
    # o lista cu cel mai apropiat vecin al fiecarui punct
    closestNeighbor = [0 for i in range(l)]
    # o lista cu punctele adaugate in graf
    visitedPoints = []
    # lista intermediara de linii
    linesAux = []
    # daca nu a fost dat niciun punct de start aleg un punct aleator pentru a fi adaugat in graf
    # if x == None:
    #     x = random.randint(0,  l)
    maxCost = 0
    y = None
    # caut cel mai departat punct de punctul initial pentru a fi adaugat
    for i in range(l):
        if distances[x][i] > maxCost and x != i:
            maxCost = distances[x][i]
            y = i
    # elimin punctele din lista de puncte ramase
    remainingPoints.remove(x)
    remainingPoints.remove(y)
    # adaug punctele in graf
    visitedPoints.append(x)
    visitedPoints.append(y)
    # adaug latura in graf
    linesAux.append((x, y))
    # caut un al treilea punct care sa fie cat mai departe de unul din punctele deja adaugate
    farthestPoint = None
    maxCost = 0
    for newPoint in remainingPoints:
        for oldPoint in visitedPoints:
            if distances[newPoint][oldPoint] > maxCost:
                maxCost = distances[newPoint][oldPoint]
                farthestPoint = newPoint
    # adaug punctul si laturile care i-l leaga de primele doua puncte in graf
    remainingPoints.remove(farthestPoint)
    visitedPoints.append(farthestPoint)
    linesAux.append((x, farthestPoint))
    linesAux.append((y, farthestPoint))
    # in prezent graful reprezinta un triunghi

    # cat timp exista puncte de adaugat
    while len(remainingPoints) > 0:
        # caut punctul cel mai departe de graf
        maxCost = 0
        for newPoint in remainingPoints:
            # pentru fiecare punct caut cel mai apropiat punct din graf
            # aleg punctul cum distanta cea mai mare pana la cel mai apropiat punct
            minCost = maxint
            for oldPoint in visitedPoints:
                if distances[newPoint][oldPoint] < minCost:
                    minCost = distances[newPoint][oldPoint]
            if minCost > maxCost:
                maxCost = minCost
                farthestPoint = newPoint
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
            newLine1 = distances[farthestPoint][p1]
            newLine2 = distances[farthestPoint][p2]
            oldLine = distances[p1][p2]
            totalLineCost = newLine1 + newLine2 - oldLine
            if totalLineCost < minCost:
                minCost = totalLineCost
                a = p1
                b = p2
        # efectuez insertia
        visitedPoints.append(farthestPoint)
        remainingPoints.remove(farthestPoint)
        linesAux.remove((a, b))
        linesAux.append((a, farthestPoint))
        linesAux.append((b, farthestPoint))

    lines = []
    totalCost = 0

    for line in linesAux:
        p1 = points[line[0]]
        p2 = points[line[1]]
        lines.append((p1, p2))
        totalCost += distances[line[0]][line[1]]

    return lines, totalCost


def farthestInsertionTSP(points):
    global distances
    global l
    #calculez distantele dintre puncte
    distances = calculateDistances(points)
    l = len(points)
    cost = maxint
    lines = None
    for i in range(l):
        linesAux, costAux = farthestInsertion(points, i)
        if costAux < cost:
            cost = costAux
            lines = linesAux
    # x = random.randint(0, l - 1)
    # lines, cost = farthestInsertion(points, x)
    return lines, cost


if __name__ == "__main__":
    testPoints = [(1, 3), (3, 2), (7, 4), (3, 5), (5.5, 6), (4, 4), (4, 3), (5, 3.5), (5, 2), (3, 4)]
    testLines, testCost = farthestInsertionTSP(testPoints)
    print(f"     NI result: {testCost}")
    drawGraph(testPoints, testLines)
