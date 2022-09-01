import matplotlib.pyplot as plt
from time import sleep

# Parameteres:
#   points: a list of tuples. Each tuple is of form (x, y), where x and y are the coordinates of one point
#   lines: a list of lines. Each line is represented by a list of exactly two tuples [(x1, y1), (x2, y2)], where x1, x2, y1, y2 are the coordinates of the line's ends
from CalculateDistances import calculateDistances


def drawGraph(points, lines, name = ""):
    px = [p[0] for p in points]
    py = [p[1] for p in points]
    sizes = [50 for i in points]
    plt.title(name)
    plt.scatter(px, py, s = sizes, vmin=0, vmax=10)
    for i in range(len(px)):
        plt.annotate(i + 1, (px[i], py[i]))
    for line in lines:
        lx = [l[0] for l in line]
        ly = [l[1] for l in line]
        plt.plot(lx, ly, linewidth = 2, color='#1f77b4')
    plt.show()

def drawProgress(points = [], lines = [], name = "", skip = 1, pause = 0.3):
    for i in range((len(lines) + 1) // skip + 2):
        if i * skip > len(lines) + 1:
            drawGraph(points, lines)
        else:
            drawGraph(points, lines[:i * skip], name)
        sleep(pause)

def drawCompleteGraf(points, cost = False, name = ""):
    lines = []
    lp = len(points)
    D = calculateDistances(points)

    px = [p[0] for p in points]
    py = [p[1] for p in points]
    sizes = [50 for i in points]
    plt.scatter(px, py, s=sizes, vmin=0, vmax=10)
    for i in range(len(px)):
        plt.annotate(i + 1, (px[i], py[i]))
    for i in range(lp - 1):
        for j in range(i + 1, lp):
            lines.append((points[i], points[j]))
            if cost:
                x = (points[i][0] + points[j][0]) / 2
                y = (points[i][1] + points[j][1]) / 2
                a = D[i][j]
                plt.annotate("%.2f" % a, (x, y))
    for line in lines:
        lx = [l[0] for l in line]
        ly = [l[1] for l in line]
        plt.plot(lx, ly, linewidth=2, color='#1f77b4')
    plt.title(name)
    plt.show()

if __name__ == "__main__":
    a = (0, 0)
    b = (2, 0)
    c = (6, 0)
    d = (8, 0)
    x = (4, 3)
    points = [a, b, c, d, x]
    lines = [(a,b), (b,c), (c, d)]
    lines2 = [(a,b), (b,x), (x, c), (c, d)]
    px = [p[0] for p in points]
    py = [p[1] for p in points]
    sizes = [50 for i in points]
    plt.scatter(px, py, s=sizes, vmin=0, vmax=10)
    plt.annotate("A", (px[0], py[0]))
    plt.annotate("B", (px[1], py[1]))
    plt.annotate("C", (px[2], py[2]))
    plt.annotate("D", (px[3], py[3]))
    plt.annotate("X", (px[4], py[4]))
    for line in lines:
        lx = [l[0] for l in line]
        ly = [l[1] for l in line]
        plt.plot(lx, ly, linewidth=2, color='#1f77b4')
    ax = plt.gca()
    ax.set_xlim([-1, 9])
    ax.set_ylim([-4, 4])
    plt.show()
    plt.scatter(px, py, s=sizes, vmin=0, vmax=10)
    plt.annotate("A", (px[0], py[0]))
    plt.annotate("B", (px[1], py[1]))
    plt.annotate("C", (px[2], py[2]))
    plt.annotate("D", (px[3], py[3]))
    plt.annotate("X", (px[4], py[4]))
    for line in lines2:
        lx = [l[0] for l in line]
        ly = [l[1] for l in line]
        plt.plot(lx, ly, linewidth=2, color='#1f77b4')
    plt.plot([b[0],c[0]], [b[1],c[1]], '--', linewidth=1, color='#1f77b4')
    ax = plt.gca()
    ax.set_xlim([-1, 9])
    ax.set_ylim([-4, 4])
    plt.show()