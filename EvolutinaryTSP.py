import math
import random
import time

from Backtracking import backtrackingTSP
from CalculateDistances import calculateDistances
from Drawing import drawGraph
from Greedy import greedyTSP
from PointGenerator import generate, readPoints

limitAchieved = False
bestCromozomes = [] # best 3 cromozomes
bestFitnesses = [] # fitness of best 3 cromozones
points = []
generationLen = 100
selectedForNextGen = generationLen//10
bestLen = 3
oldGeneration = []
currGeneration = []
nextGen = []
# l = None
genNumber = 0

def generateCromozome(points):
    l = len(points)
    pointsCopy = points.copy()
    c = []
    last = random.randint(0, l - 1)
    c.append(last)
    last = pointsCopy.pop(last)
    for i in range(l-2):
        bestGene = None
        minLen = 10000
        for j in range(l//5):
            gene = random.randint(0, l-i-2)
            if dist(last, pointsCopy[gene]) < minLen:
                bestGene = gene
                minLen = dist(last, pointsCopy[gene])
        c.append(bestGene)
        last = pointsCopy.pop(bestGene)
    c.append(0)
    return c

def dist(a, b):
    x1 = a[0]
    y1 = a[1]
    x2 = b[0]
    y2 = b[1]
    if x1 > x2:
        xDif = x1 - x2
    else:
        xDif = x2 - x1
    if y1 > y2:
        yDif = y1 - y2
    else:
        yDif = y2 - y1
    dist = math.sqrt(xDif ** 2 + yDif ** 2)

    return dist

def fitness(cromozome):
    pointsCopy = points.copy()
    c = cromozome.copy()
    a = c.pop(0)
    first = p1 = pointsCopy.pop(a)
    lines = []
    cost = 0
    for i in range(len(c)):
        b = c.pop(0)
        p2 = pointsCopy.pop(b)
        cost += dist(p1, p2)
        lines.append((p1, p2))
        p1 = p2

    cost += dist(first, p1)
    lines.append((p1, first))
    return cost

def selectBest(list):
    global points
    for c in list:
        f = fitness(c)
        if f < bestFitnesses[0]:
            bestCromozomes[2] = bestCromozomes[1]
            bestCromozomes[1] = bestCromozomes[0]
            bestCromozomes[0] = c

            bestFitnesses[2] = bestFitnesses[1]
            bestFitnesses[1] = bestFitnesses[0]
            bestFitnesses[0] = f
        elif f < bestFitnesses[1]:
            bestCromozomes[2] = bestCromozomes[1]
            bestCromozomes[1] = c

            bestFitnesses[2] = bestFitnesses[1]
            bestFitnesses[1] = f
        elif f < bestFitnesses[2]:
            bestCromozomes[2] = c
            bestFitnesses[2] = f

def selectCromozome(intervals):
    x = random.uniform(0, 1)
    for i in range(1, len(intervals)):
        if intervals[i] > x:
            return i-1

def runGeneration():
    global l
    global genNumber
    global oldGeneration
    genNumber+=1
    nextGen = []
    currGeneration = bestCromozomes + oldGeneration
    genFitness = [fitness(c) for c in currGeneration]
    sumFitness = 0
    for f in genFitness:
        sumFitness += f
    probabilities = [genFitness[i]/sumFitness for i in range(generationLen)]
    sumProbabilities = 0
    for i in probabilities:
        sumProbabilities += i
    intervals = [0]
    index = 0
    for i in probabilities:
        index += i
        intervals.append(index)
    intervals.pop()
    intervals.append(1)

    crossMutating = []
    for c in currGeneration:
        x = random.uniform(0, 1)
        if x < 0.4:
            crossMutating.append(c)
    while len(crossMutating) > 3:
        c1 = crossMutating.pop(0)
        c2 = crossMutating.pop(0)
        x = random.randint(0, l-3)
        y = random.randint(x+2, l-1)
        newC1 = c1[:x] + c2[x:y] + c1[y:]
        newC2 = c2[:x] + c1[x:y] + c2[y:]
        nextGen.append(newC1)
        nextGen.append(newC2)
    if len(crossMutating) == 3:
        c1 = crossMutating.pop(0)
        c2 = crossMutating.pop(0)
        c3 = crossMutating.pop(0)
        x = random.randint(0, l-3)
        y = random.randint(x+2, l-1)
        newC1 = c1[:x] + c2[x:y] + c1[y:]
        newC2 = c2[:x] + c3[x:y] + c2[y:]
        newC3 = c3[:x] + c1[x:y] + c3[y:]
        nextGen.append(newC1)
        nextGen.append(newC2)
        nextGen.append(newC3)
    elif len(crossMutating) == 2:
        c1 = crossMutating.pop(0)
        c2 = crossMutating.pop(0)
        x = random.randint(0, l-3)
        y = random.randint(x+2, l-1)
        newC1 = c1[:x] + c2[x:y] + c1[y:]
        newC2 = c2[:x] + c1[x:y] + c2[y:]
        nextGen.append(newC1)
        nextGen.append(newC2)

    selfMutating = []
    for c in currGeneration:
        x = random.uniform(0, 1)
        if x < 0.4:
            selfMutating.append(c)
    for c in selfMutating:
        for i in range(l):
            x = random.uniform(0, 1)
            if x < 0.4:
                c[i] = random.randint(0, l-i-1)
        nextGen.append(c)

    toBeSelected = generationLen - bestLen - len(nextGen)
    if toBeSelected > selectedForNextGen:
        for i in range(selectedForNextGen):
            x = selectCromozome(intervals)
            nextGen.append(currGeneration[x])
        for i in range(toBeSelected - selectedForNextGen):
            c = generateCromozome(points)
            nextGen.append(c)

    else:
        for i in range(toBeSelected):
            x = selectCromozome(intervals)
            nextGen.append(currGeneration[x])

    selectBest(nextGen)
    oldGeneration = nextGen
    if(genNumber%50 == 0):
        print(f"Generation {genNumber}: best fitness: {bestFitnesses[0]}")


if __name__ == "__main__":
    # global points
    # global l
    # global bestCromozomes
    l = 100
    # points = generate(l)
    points = readPoints(filename="test_points/100_test_points_00.txt")

    bestCromozomes = [generateCromozome(points) for i in range(3)]
    bestFitnesses = [fitness(c) for c in bestCromozomes]
    oldGeneration = [generateCromozome(points) for i in range(generationLen - bestLen)]
    for i in range(1000):
        runGeneration()

    a, b = greedyTSP(points)
    print(f"Cost greedy: {b}")


# if __name__ == "__main__":# global points
#     l = 100
#     points = readPoints(filename="test_points/100_test_points_00.txt")
#     c = generateCromozome(points)
#     print(len(c))

