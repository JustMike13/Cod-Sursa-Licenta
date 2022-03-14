import matplotlib.pyplot as plt
from time import sleep
from Drawing import drawGraph
from Greedy import greedyTSP
from CalculateDistances import calculateDistances
from NearestNeighbour import nearestNeighbourTSP
from PointGenerator import generate
import time
testPoints = generate(100)

greedystart = time.time()
a, b, c = greedyTSP(testPoints)
greedyend = time.time()
print("Greedy cost:                   ", c)
print("Greedy time:                   ", greedyend - greedystart)
print("")
nnrstart = time.time()
d, e = nearestNeighbourTSP(testPoints, "random")
nnrend = time.time()
print("Nearest Neighbour random cost: ", e)
print("Nearest Neighbour random time: ", nnrend - nnrstart)
print("")


nnastart = time.time()
f, g = nearestNeighbourTSP(testPoints, "all")
nnaend = time.time()
print("Nearest Neighbour all cost:    ", g)
print("Nearest Neighbour all time:    ", nnaend - nnastart)


