from CalculateDistances import calculateDistances
from Drawing import drawGraph, drawProgress
from Greedy import orderAscending

distances = [[]]
l = 0
set = []

def makeUnion(u, v):
    global set
    # mereu pastrez numarul mai mic
    if u < v:
        aux = v
        v = u
        u = aux
    for i in range(l):
        if set[i] == v:
            set[i] = u

def kruskal(points, distances):
    global l
    global set
    l = len(points)
    ordList = orderAscending(distances)
    F = []
    D = [[0 for i in range(l)] for j in range(l)]
    set = [i for i in range(l)]
    for line in ordList:
        a, b = line
        if set[a] != set[b]:
            F.append((a, b))
            D[a][b] = D[b][a] = distances[a][b]
            makeUnion(set[a], set[b])
    return F, D


if __name__ == "__main__":
    testPoints = [(1, 3), (3, 2), (7, 4), (3, 5), (5.5, 6), (4, 4), (4, 3), (5, 3.5), (5, 2), (3, 4)]
    distances = calculateDistances(testPoints)
    linesAux, distancesAux = kruskal(testPoints, distances)
    lines = []
    for line in linesAux:
        p1, p2 = line
        p1 = testPoints[p1]
        p2 = testPoints[p2]
        lines.append((p1, p2))

    drawProgress(testPoints, lines, "kruskal result")