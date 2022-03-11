import matplotlib.pyplot as plt
from time import sleep
from Drawing import drawGraph
from GreedyTSP import greedyTSP
from CalculateDistances import calculateDistances

# testPoints = [(1, 5), (2, 1), (3, 4)]
# testLines = [[(1, 5), (2, 1)], [(2, 1), (3, 4)], [(3, 4), (1, 5)]]
#
# for i in range(len(testLines) + 1):
#     drawGraph(testPoints, testLines[:i])
#     sleep(1)


testPoints = [(1, 3), (7, 3), (7, 7), (1, 7), (5, 4), (5, 6), (3, 6), (3, 4)]
testDistances = calculateDistances(testPoints)
for i in testDistances:
    print(i)

testLines, testNeighbors, testCost = greedyTSP(testPoints)
print(testLines)
print(testDistances)
print("Cost total:", testCost)
for i in range(len(testLines) + 1):
    drawGraph(testPoints, testLines[:i])
    sleep(0.3)