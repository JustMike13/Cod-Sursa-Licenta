from Backtracking import backtrackingTSP
from Drawing import drawGraph, drawProgress
from CalculateDistances import calculateDistances
from Greedy import sortDistances
from PointGenerator import generate, readPoints
import time
maxint = 2147483647

def lowestGroup(x, y):
    if x<y:
        return x, y
    return y, x

def greedyColoringTSP(points):
    distances = calculateDistances(points)
    l = len(points)
    lines = []
    # ordonez muchiile crescator
    orderedDistances = sortDistances(distances)
    # lista de componente conexe(grupari), groups[i] = numarul gruparii din care face parte nodul i, sau 0 daca nu face parte dintr-un grup
    groups = [0 for i in range(l)]
    # lungimea lantului determinat de fiecare grup
    groupLen = [0 for i in range(l)]
    # lista de muchii, edges[i] = numarul de muchii ala nodului i, maxim 2
    edges = [0 for i in range(l)]
    a1, b1 = orderedDistances.pop(0)
    c1 = distances[a1][b1]
    totalCost = c1
    lines.append((points[a1], points[b1]))
    edges[a1] = edges[b1] = 1
    groups[a1] = groups[b1] = 1
    groupLen[1] = 2
    # numarul ce va fi atribuit urmatorului grup, creste la crearea fiecarui grup
    nextGroup = 2
    final = False

    while not final:
        # extrag capetele urmatoarei muchii
        a, b = orderedDistances.pop(0)
        if edges[a] < 2 and edges[b] < 2:
            if groups[a] != groups[b]:
                if groups[a] == 0:
                    edges[a]+=1
                    edges[b]+=1
                    groups[a] = groups[b]
                    groupLen[groups[b]] += 1
                elif groups[b] == 0:
                    edges[a] += 1
                    edges[b] += 1
                    groups[b] = groups[a]
                    groupLen[groups[b]] += 1
                else:
                    lowerGroup, higherGroup = lowestGroup(groups[a], groups[b])
                    for i in range(l):
                        if groups[i] == higherGroup:
                            groups[i] = lowerGroup
                    edges[a] = edges[b] = 2
                    groupLen[lowerGroup] += groupLen[higherGroup]
                lines.append((points[a], points[b]))
                totalCost += distances[a][b]
            elif groups[a] == groups[b] == 0:
                edges[a] = edges[b] = 1
                groups[a] = groups[b] = nextGroup
                groupLen[nextGroup] = 2
                nextGroup += 1
                lines.append((points[a], points[b]))
                totalCost += distances[a][b]
            elif groups[a] == groups[b] == 1 and groupLen[1] == l:
                lines.append((points[a], points[b]))
                totalCost += distances[a][b]
                final = True

    return lines, totalCost

if __name__ == "__main__":
    # testPoints = [(1, 3), (3, 2), (7, 4), (3, 5), (5.5, 6), (4, 4), (4, 3), (5, 3.5), (5, 2), (3, 4)]
    # testPoints = readPoints(filename="test_points/200_test_points_00.txt")
    testPoints = generate(500)
    testDistances = calculateDistances(testPoints)
    timeStart = time.time()
    sortDistances(testDistances)
    timeEnd = time.time()
    timeDif = timeEnd - timeStart
    print(f"ordering time : {timeDif}")
    timeStart = time.time()
    testLines, testCost = greedyColoringTSP(testPoints)
    timeEnd = time.time()
    timeDif = timeEnd - timeStart
    print(f"     Greedy result: {testCost}")
    print(f"     Greedy time : {timeDif}")
    drawGraph(testPoints, testLines, f"Greedy Coloring, {testCost}, {timeDif}")