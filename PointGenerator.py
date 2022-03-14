import random
import matplotlib.pyplot as plt
from time import sleep
from Drawing import drawProgress
from Greedy import greedyTSP
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
        to_write = str(len(list)) + "\n"
        for point in list:
            to_write = to_write + str(point[0]) + " " + str(point[1]) + "\n"
        f.write(to_write)
        f.close()

    return list

# testPoint = generate(100, interval = (1, 1000))
#
# a, b, c = greedyTSP(testPoint)
# print(len(a))
# print(c)
#
# drawProgress(testPoint, a, 5, 0.1)
