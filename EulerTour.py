from Drawing import drawProgress, drawGraph
from kruskal import kruskal

g = [[]]
circuit = []
l = 0

def visit(current):
    global l
    global g
    global circuit
    tour = [current]
    for x in range(l):
        if g[current][x] > 0:
            g[current][x] = 0
            g[x][current] = 0
            tour = tour + visit(x) + [current]
    return tour

def eulerTour(distances):
    global g
    global l
    l = len(distances)
    g = list(distances)
    # for j in g:
    #     print(j)
    finalTour = visit(0)

    return finalTour


if __name__ == "__main__":
    testPoints = [(1, 3), (3, 2), (7, 4), (3, 5), (5.5, 6), (4, 4), (4, 3), (5, 3.5), (5, 2), (3, 4)]
    linesAux, distancesAux = kruskal(testPoints)
    lines = []
    for line in linesAux:
        p1, p2 = line
        p1 = testPoints[p1]
        p2 = testPoints[p2]
        lines.append((p1, p2))

    drawGraph(testPoints, lines, "kruskal result")
    print(eulerTour(distancesAux))