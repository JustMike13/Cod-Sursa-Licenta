from CalculateDistances import calculateDistances
from Drawing import drawGraph
from EulerTour import eulerTour
from kruskal import kruskal

distances = [[]]
l = 0

def twoAproximationTSP(points):
    global distances
    distances = calculateDistances(points)
    kruskalLines, kruskatMatrix = kruskal(points, distances)
    eulerTourList = eulerTour(kruskatMatrix)
    visited = []
    lines = []
    cost = 0
    while len(eulerTourList) > 2:
        a = eulerTourList[0]
        b = eulerTourList[1]
        c = eulerTourList[2]
        if b in visited:
            eulerTourList.pop(1)
        else:
            lines.append((points[a], points[b]))
            cost += distances[a][b]
            visited.append(b)
            eulerTourList.pop(0)
    a = eulerTourList[0]
    b = eulerTourList[1]
    lines.append((points[a], points[b]))

    return lines, cost


if __name__ == "__main__":
    testPoints = [(1, 3), (3, 2), (7, 4), (3, 5), (5.5, 6), (4, 4), (4, 3), (5, 3.5), (5, 2), (3, 4)]
    a, b = twoAproximationTSP(testPoints)
    drawGraph(testPoints, a, f"2-Aproximation, {b}")