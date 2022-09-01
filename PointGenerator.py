import random
import glob
import matplotlib.pyplot as plt
from time import sleep
from Drawing import drawProgress
# from Greedy import greedyTSP
from CalculateDistances import calculateDistances

def generate(number = 10, filename = "no_file", interval = (1, 100)):
    list = []
    intervalStart = interval[0]
    intervalEnd = interval[1]
    for i in range(number):
        a = random.randint(intervalStart, intervalEnd)
        b = random.randint(intervalStart, intervalEnd)
        while((a, b) in list):
            a = random.randint(intervalStart, intervalEnd)
            b = random.randint(intervalStart, intervalEnd)
        list.append((a, b))

    if filename != "no_file":
        f = open(filename, "w")
        to_write = str(len(list))
        for point in list:
            to_write = to_write + "\n" + str(point[0]) + " " + str(point[1])
        f.write(to_write)
        f.close()

    return list

def readPoints(filename = None):
    if filename == None:
        D = {}
        for filename in glob.glob("test_points" + '/*.txt'):
            file = open(filename)
            text = file.read()
            lines = text.split("\n")
            nr = float(lines[0])
            points = []
            for i in lines[1:]:
                point = i.split()
                x = float(point[0])
                y = float(point[1])
                points.append((x, y))
            D[nr] = points
        return D
    file = open(filename)
    text = file.read()
    lines = text.split("\n")
    nr = float(lines[0])
    points = []
    for i in lines[1:]:
        point = i.split()
        x = float(point[0])
        y = float(point[1])
        points.append((x, y))
    return points


if __name__ == "__main__":
    # generate(number = 10,    filename = "test_points/10_test_points.txt")
    # generate(number = 50,    filename = "test_points/50_test_points.txt")
    # generate(number = 200,   filename = "test_points/200_test_points.txt")
    # generate(number = 300,   filename = "test_points/300_test_points.txt")
    # generate(number = 1000,  filename = "test_points/1000_test_points.txt")
    # generate(number = 5000,  filename = "test_points/5000_test_points.txt")
    # generate(number = 10000, filename = "test_points/10000_test_points.txt")
    for i in range(20):
        if i < 10:
            nr = "0" + str(i)
        else:
            nr = str(i)
        generate(number = 500, filename = "test_points/500_test_points_" + nr + ".txt")
    # d = readPoints()
    # for i in d:
    #     print(f"{i}:   {d[i]}")
