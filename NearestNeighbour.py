import time
import random

from Backtracking import backtrackingTSP
from Drawing import drawGraph, drawProgress
from CalculateDistances import calculateDistances

from PointGenerator import generate
distances = None
maxint = 2147483647
def randomStartingPoint(points):
    global distances
    distances = calculateDistances(points)
    l = len(points)
    lines = []
    cost = 0
    currPoint = random.randint(0, l-1)
    visitedPoints = [currPoint]
    while(len(visitedPoints) < l):
        minDist = maxint
        minIndex = -1
        for i in range(l):
            if i != currPoint :
                if distances[currPoint][i] < minDist:
                    if i not in visitedPoints:
                        minDist = distances[currPoint][i]
                        minIndex = i
        visitedPoints.append(minIndex)
        currPoint = minIndex
        cost += minDist

    currPoint = visitedPoints[0]
    costTotal = 0
    for point in visitedPoints[1:]:
        a = points[currPoint]
        b = points[point]
        lines.append((a, b))
        costTotal = costTotal + distances[currPoint][point]
        currPoint = point
    a = points[visitedPoints[-1]]
    b = points[visitedPoints[0]]
    lines.append((a, b))
    costTotal = costTotal + distances[visitedPoints[-1]][visitedPoints[0]]
    # print("Random starting point:", visitedPoints[0], ",    Cost:", totalCost)

    return lines, costTotal

def allStartingPoints(points):
    global distances
    distances = calculateDistances(points)
    l = len(points)
    lines = []
    minCost = maxint
    bestRoute = []
    for startingPoint in range(l):
        currPoint = startingPoint
        visitedPoints = [currPoint]
        totalCost = 0
        while(len(visitedPoints) < l):
            min = maxint
            minIndex = -1
            for i in range(l):
                if i != currPoint and distances[currPoint][i] < min and i not in visitedPoints:
                    min = distances[currPoint][i]
                    minIndex = i
            visitedPoints.append(minIndex)
            currPoint = minIndex
            totalCost += min

        if totalCost < minCost:
            minCost = totalCost
            bestRoute = visitedPoints

    currPoint = bestRoute[0]
    # print("Random starting point:", visitedPoints[0], ",    Cost:", totalCost)
    # print(bestRoute)
    costTotal = 0
    for point in bestRoute[1:]:
        a = points[currPoint]
        b = points[point]
        lines.append((a, b))
        costTotal = costTotal + distances[currPoint][point]
        currPoint = point
    a = points[bestRoute[-1]]
    b = points[bestRoute[0]]
    costTotal = costTotal + distances[bestRoute[-1]][bestRoute[0]]
    lines.append((a, b))
    return lines, costTotal

def nearestNeighbourTSP(points, startingPoint = "random"):
    if startingPoint == "random":
        return randomStartingPoint(points)
    elif startingPoint == "all":
        return allStartingPoints(points)


if __name__ == "__main__":
    # points = [(1, 3), (3, 2), (7, 4), (3, 5), (5.5, 6), (4, 4), (4, 3), (5, 3.5), (5, 2), (3, 4)]
    points = generate(20)
    a, b = nearestNeighbourTSP(points, "all")
    print(f"Cost: {b}")
    drawProgress(points, a, f"Cost: {b}")
    # nr = 10
    # results = []
    # for i in range(10):
    #     print(f"setul de date nr {i}")
    #     points = generate(nr)
    #     BTStart = time.time()
    #     a, b = backtrackingTSP(points)
    #     BTEnd = time.time()
    #     BTDif = BTEnd - BTStart
    #     print(f"     BT result: {b}")
    #     print(f"     BT time: {BTDif}")
    #     # drawGraph(points, a)
    #     timeStart = time.time()
    #     testLines, testCost = nearestNeighbourTSP(points, "all")
    #     timeEnd = time.time()
    #     timeDif = timeEnd - timeStart
    #     print(f"     nn result: {testCost}")
    #     print(f"     nn time : {timeDif}\n\n")
    #     # drawGraph(points, testLines)
    #     results.append((b, testCost))
    # sum = 0
    # for r in results:
    #     btr, nnr = r
    #     dif = nnr - btr
    #     procent = (dif * 100) / btr
    #     sum += procent
    # print(f"\n\n\nCrestere medie de {sum / len(results)} procente")