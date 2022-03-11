import math

# Parameteres:
#   points: a list of tuples. Each tuple is of form (x, y), where x and y are the coordinates of one point
def calculateDistances(points):
    nrPoints = len(points)
    distances = [[0 for i in range(nrPoints)] for i in range(nrPoints)]
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            x1 = points[i][0]
            y1 = points[i][1]
            x2 = points[j][0]
            y2 = points[j][1]
            if x1 > x2:
                xDif = x1 - x2
            else:
                xDif = x2 - x1
            if y1 > y2:
                yDif = y1 - y2
            else:
                yDif = y2 - y1
            dist = math.sqrt(xDif ** 2 + yDif ** 2)
            distances[i][j] = distances[j][i] = dist
    return distances
