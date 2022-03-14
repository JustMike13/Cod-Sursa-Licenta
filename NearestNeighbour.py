from Drawing import drawGraph
from CalculateDistances import calculateDistances
from time import sleep
import random

maxint = 2147483647
def randomStartingPoint(points):
    distances = calculateDistances(points)
    l = len(points)
    lines = []
    totalCost = 0
    currPoint = random.randint(0, l)
    visitedPoints = [currPoint]
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

    currPoint = visitedPoints[0]
    for point in visitedPoints[1:]:
        a = points[currPoint]
        b = points[point]
        lines.append((a, b))
    a = points[visitedPoints[-1]]
    b = points[visitedPoints[0]]
    lines.append((a, b))
    # print("Random starting point:", visitedPoints[0], ",    Cost:", totalCost)

    return lines, totalCost

def allStartingPoints(points):
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
    for point in bestRoute[1:]:
        a = points[currPoint]
        b = points[point]
        lines.append((a, b))
    a = points[bestRoute[-1]]
    b = points[bestRoute[0]]
    lines.append((a, b))
    return lines, minCost

def nearestNeighbourTSP(points, startingPoint = "random"):
    if startingPoint == "random":
        return randomStartingPoint(points)
    elif startingPoint == "all":
        return allStartingPoints(points)