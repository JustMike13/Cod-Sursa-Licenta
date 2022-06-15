import matplotlib.pyplot as plt
from time import sleep

from Backtracking import backtrackingTSP
from CheapestInsertion import cheapestInsertionTSP
from Drawing import drawGraph, drawCompleteGraf
from FarthestInsertion import farthestInsertionTSP
from Greedy import greedyTSP
from CalculateDistances import calculateDistances
from NearestInsertion import nearestInsertionTSP, nearestInsertion
from NearestNeighbour import nearestNeighbourTSP
from PointGenerator import generate, readPoints
from TwoAproximation import twoAproximationTSP
import time

def nearestInsertionTest():
    print("Datele de intrare de testare si nod de start aleator:\n")
    for nrPoints in [50, 100, 200, 300, 500]:
        print(f"{nrPoints} puncte:")
        sumCost = 0
        sumTime = 0
        for i in range(20):
            print(f"  Multimea de date numarul {i}")
            if i < 10:
                nr = "0" + str(i)
            else:
                nr = str(i)
            points = readPoints("test_points/" + str(nrPoints) + "_test_points_" + nr + ".txt")
            timeStart = time.time()
            a, b = nearestInsertionTSP(points)
            timeEnd = time.time()
            timeDif = timeEnd - timeStart
            print(f"    Cost: {b}\n    Durata: {timeDif}")
            sumCost += b
            sumTime += timeDif
        print(f"      Cost total: {sumCost}\n      Durata medie: {sumTime / 20}\n\n\n")

def test10p():
    testPoints = readPoints("test_points/50_test_points_00.txt")
    # drawCompleteGraf(testPoints, name = "Graf complet")
    # drawCompleteGraf(testPoints, True, name = "Graf complet + Costuri")
    # testLines, testCost = backtrackingTSP(testPoints)
    # print(f"     backtracking result: {testCost}")
    # drawGraph(testPoints, testLines, f"Backtracking, Cost= {testCost}\n")

    testLines, testCost = greedyTSP(testPoints)
    print(f"     greedy result: {testCost}")
    drawGraph(testPoints, testLines, f"Greedy, Cost= {testCost}\n")

    testLines, testCost = nearestNeighbourTSP(testPoints)
    print(f"     nearestNeighbour result: {testCost}")
    drawGraph(testPoints, testLines, f"Nearest Neighbour, Cost= {testCost}\n")

    testLines, testCost = nearestInsertionTSP(testPoints)
    print(f"     NearestInsertion result: {testCost}")
    drawGraph(testPoints, testLines, f"Nearest Insertion, Cost= {testCost}\n")

    testLines, testCost = cheapestInsertionTSP(testPoints)
    print(f"     CheapestInsertion result: {testCost}")
    drawGraph(testPoints, testLines, f"Cheapest Insertion, Cost= {testCost}\n")

    testLines, testCost = farthestInsertionTSP(testPoints)
    print(f"     CheapestInsertion result: {testCost}")
    drawGraph(testPoints, testLines, f"Farthest Insertion, Cost= {testCost}\n")

    testLines, testCost = twoAproximationTSP(testPoints)
    print(f"     CheapestInsertion result: {testCost}")
    drawGraph(testPoints, testLines, f"2-Aproximation, Cost= {testCost}\n")

def nearestNeighbourTest():
    # points = readPoints()
    print("Datele de intrare de testare:\n")
    for nrPoints in [50, 100, 200, 300]:
        print(f"{nrPoints} puncte:")
        sumCost = 0
        sumTime = 0
        for i in range(20):
            print(f"  Multimea de date numarul {i}")
            if i < 10:
                nr = "0" + str(i)
            else:
                nr = str(i)
            points = readPoints("test_points/" + str(nrPoints) + "_test_points_" + nr + ".txt")
            timeStart = time.time()
            a, b = nearestNeighbourTSP(points, "random")
            timeEnd = time.time()
            timeDif = timeEnd - timeStart
            print(f"    Cost: {b}\n    Durata: {timeDif}")
            sumCost += b
            sumTime += timeDif
        print(f"      Cost total: {sumCost}\n      Durata medie: {sumTime / 20}\n\n\n")

    # print("Datele de intrare aleatoare:\n")
    # for nrPoints in [50, 100, 200, 300]:
    #     print(f"{nrPoints} puncte:")
    #     timeTotal = 0
    #     for i in range(100):
    #         print(f"  Incercarea nr {i + 1}:")
    #         points = generate(nrPoints)
    #         timeStart = time.time()
    #         a, b = nearestNeighbourTSP(points, "all")
    #         timeEnd = time.time()
    #         timeDif = timeEnd - timeStart
    #         print(f"     Cost: {b}")
    #         print(f"     Durata: {timeDif}")
    #         timeTotal += timeDif
    #     print(f"     Durata medie: {timeTotal / 100}\n\n")

def greedyTest():
    for nrPoints in [50, 100]:
        print(f"{nrPoints} puncte:")
        sumCost = 0
        sumTime = 0
        for i in range(20):
            print(f"  Multimea de date numarul {i}")
            if i < 10:
                nr = "0" + str(i)
            else:
                nr = str(i)
            points = readPoints("test_points/" + str(nrPoints) + "_test_points_" + nr + ".txt")
            timeStart = time.time()
            a, b = greedyTSP(points)
            timeEnd = time.time()
            timeDif = timeEnd - timeStart
            print(f"    Cost: {b}\n    Durata: {timeDif}")
            sumCost += b
            sumTime += timeDif
        print(f"      Cost total: {sumCost}\n      Durata medie: {sumTime / 20}\n\n\n")

def cheapestInsertionTest():
    print("Cheapest insertion")
    print("Datele de intrare de testare aleatoare si toate nodurile de start:\n")
    for nrPoints in [50, 100, 200, 300]:
        print(f"{nrPoints} puncte:")
        sumCost = 0
        sumTime = 0
        if nrPoints < 300:
            nrIter = 20
        else:
            nrIter = 5
        for i in range(nrIter):
            print(f"  Multimea de date numarul {i}")
            # if i < 10:
            #     nr = "0" + str(i)
            # else:
            #     nr = str(i)
            # points = readPoints("test_points/" + str(nrPoints) + "_test_points_" + nr + ".txt")
            points = generate(nrPoints)
            timeStart = time.time()
            a, b = cheapestInsertionTSP(points)
            timeEnd = time.time()
            timeDif = timeEnd - timeStart
            print(f"    Cost: {b}\n    Durata: {timeDif}")
            sumCost += b
            sumTime += timeDif
        print(f"      Cost total: {sumCost}\n      Durata medie: {sumTime / nrIter}\n\n\n")

def farthestInsertionTest():
    print("\n\nFarthest insertion")
    print("Datele de intrare aleatoare si nod de start aleator:\n")
    for nrPoints in [50, 100, 200, 300]:
        print(f"{nrPoints} puncte:")
        sumCost = 0
        sumTime = 0
        nrIter = 20
        for i in range(nrIter):
            print(f"  Multimea de date numarul {i}")
            # if i < 10:
            #     nr = "0" + str(i)
            # else:
            #     nr = str(i)
            # points = readPoints("test_points/" + str(nrPoints) + "_test_points_" + nr + ".txt")
            points = generate(nrPoints)
            timeStart = time.time()
            a, b = farthestInsertionTSP(points)
            timeEnd = time.time()
            timeDif = timeEnd - timeStart
            print(f"    Cost: {b}\n    Durata: {timeDif}")
            sumCost += b
            sumTime += timeDif
        print(f"      Cost total: {sumCost}\n      Durata medie: {sumTime / nrIter}\n\n\n")

def twoAproximationTest():
    print("Datele de intrare aleatoare:\n")
    for nrPoints in [50, 100, 200, 300]:
        print(f"{nrPoints} puncte:")
        sumCost = 0
        sumTime = 0
        nrIter = 20
        for i in range(nrIter):
            print(f"  Multimea de date numarul {i}")
            # if i < 10:
            #     nr = "0" + str(i)
            # else:
            #     nr = str(i)
            # points = readPoints("test_points/" + str(nrPoints) + "_test_points_" + nr + ".txt")
            points = generate(nrPoints)
            timeStart = time.time()
            a, b = twoAproximationTSP(points)
            timeEnd = time.time()
            timeDif = timeEnd - timeStart
            print(f"    Cost: {b}\n    Durata: {timeDif}")
            sumCost += b
            sumTime += timeDif
        print(f"      Cost total: {sumCost}\n      Durata medie: {sumTime / nrIter}\n\n\n")


if __name__ == "__main__":
    test10p()
    # greedyTest()
    # nearestNeighbourTest()
    # nearestInsertionTest()
    # cheapestInsertionTest()
    # farthestInsertionTest()
    # twoAproximationTest()








