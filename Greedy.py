from Backtracking import backtrackingTSP
from Drawing import drawGraph, drawProgress
from CalculateDistances import calculateDistances
from PointGenerator import generate
import time

maxint = 2147483647
def greedyTSP(points):
    distances = calculateDistances(points)
    l = len(points)
    lines = []
    # ordonez muchiile crescator
    orderedDistances = orderAscending(distances)
    # matrice de vecini
    neighbors = [[0 for i in range(l)] for i in range(l)]
    # salvez cea mai scurta muchie si distanta ei
    a1, b1 = orderedDistances.pop(0)
    c1 = distances[a1][b1]
    # o adaug in lista de linii
    lines.append((a1, b1, c1))
    # adaug muchia in matricea de vecini
    neighbors[a1][b1] = neighbors[b1][a1] = 1
    # final == True => am gasit un tur care se termina la punctul de start (care este ciclu) si are lungime l
    final = False
    while not final:
        existingCycle = True
        # presupun ca exista ciclu in graf, adaug o muchie si apoi verific daca exista ciclul
        # daca exista, adaug alta muchie si repet
        # in caz contrat, ma opresc
        while existingCycle:
            # extrag cea mai scurta muchie ramasa
            a, b = orderedDistances.pop(0)
            c = distances[a][b]
            # grad = numarul de vecini
            grad_a = 0
            grad_b = 0
            # calculez numarul de vecini al fiecarui capat al muchiei
            for v in range(l):
                grad_a += neighbors[a][v]
                grad_b += neighbors[b][v]
            # daca cel putin unul din noduri are grad 2, nu putem adauga muchia
            # altfel, daca cel putin unul din noduri are grad 0, muchia nu poate forma un ciclu, deci o adaugam
            # altfel, daca ambele noduri au grad 1, verificam daca muchia formeaza un ciclu
            if (grad_a == grad_b == 0) or (grad_a == 0 and grad_b == 1) or (grad_a == 1 and grad_b == 0):
                # daca putem garanta ca nu formeaza un ciclu, ne oprim si adaugam muchia (a, b)
                existingCycle = False
            elif grad_a == grad_b == 1:
                # daca, parcurgand graful incepand din nodul b, gasim nodul a, inseamna ca muchia (a, b) formeaza un ciclu
                found = False
                # gradul fiecarui nod
                ranks = [0 for i in range(l)]
                ranks[b] = 1
                # parcurgem in latime, incepand cu nodul b
                nextPoints = [b]
                checked = [b]
                while len(nextPoints) >= 1:
                    point = nextPoints.pop(0)
                    nb = neighbors[point]
                    for n in range(len(nb)):
                        if nb[n] == 1 and n not in checked:
                            # daca am gasit punctul de start
                            if n == a:
                                # formeaza ciclu
                                found = True
                                # daca ciclul are lungimea l
                                if ranks[point] + 1 == l:
                                    # adaugam muchia si returnam graful
                                    final = True
                                    existingCycle = False
                            else:
                                nextPoints.append(n)
                                checked.append(n)
                                ranks[n] = ranks[point] + 1
                if not found:
                    # Daca nu am gasit nodul a, inseamna ca nu formeaza un ciclu
                    existingCycle = False
        # adaugam muchia (a, b)
        lines.append((a, b, c))
        neighbors[a][b] = neighbors[b][a] = 1
    # in lista lines, fiecare element esta un tuplu format din indicele capetelor unei muchii si lungimea ei
    # in linesFinal, fiecare element este un tuplu format din doua puncte, fiecare reprezentat de o pereche de coordonate
    linesFinal = []
    totalCost = 0
    # pentru fiecare linie
    for line in lines:
        a = line[0]
        b = line[1]
        c = line[2]
        # incrementez costul cu lungimea acesteia
        totalCost += c
        auxLine = [points[a], points[b]]
        # adaug linia
        linesFinal.append(auxLine)
    return linesFinal, totalCost

def orderAscending(dist):
    l = len(dist)
    orderedList = []
    for i in range(l - 1):
        for j in range(i + 1, l):
            # daca orderedList nu are elemente, inserez elementul curent
            if len(orderedList) == 0:
                orderedList.append((i, j))
            else:
                firstElem = orderedList[0]
                lastElem = orderedList[-1]
                # daca elementul curent este mai scurt decat primul element din lista, inserez elementul curent pe prima pozitie
                if dist[i][j] <= dist[firstElem[0]][firstElem[1]]:
                    orderedList.insert(0, (i, j))
                # daca elementul curent este mai lung decat ultimul element din lista, inserez elementul curent pe ultima pozitie
                elif dist[i][j] >= dist[lastElem[0]][lastElem[1]]:
                    orderedList.append((i, j))
                else:
                    # daca elementul este mai mare decat elementul k, dar mai mic decat elementul k + 1, inserez pe pozitia k + 1
                    for k in range(len(orderedList) - 1):
                        listElem = orderedList[k]
                        nextElem = orderedList[k + 1]
                        if dist[listElem[0]][listElem[1]] < dist[i][j] and dist[nextElem[0]][nextElem[1]] >= dist[i][j]:
                            orderedList.insert(k + 1, (i, j))
                            break
    return orderedList


if __name__ == "__main__":
    testPoints = [(1, 3), (3, 2), (7, 4), (3, 5), (5.5, 6), (4, 4), (4, 3), (5, 3.5), (5, 2), (3, 4)]
    # testDistances = calculateDistances(testPoints)
    # timeStart = time.time()
    testLines, testCost = greedyTSP(testPoints)
    # timeEnd = time.time()
    # timeDif = timeEnd - timeStart
    print(f"     Greedy result: {testCost}")
    # print(f"     Greedy time : {timeDif}")
    drawGraph(testPoints, testLines, f"Greedy, {testCost}")