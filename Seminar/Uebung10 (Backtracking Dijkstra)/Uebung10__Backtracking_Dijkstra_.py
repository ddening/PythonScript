# Seminar Uebung 10 (Backtracking mit Dijkstra)                         
#  _____________________________________
#                                       
#          /               ,            
#  ----__-/----__----__--------__----__-
#    /   /   /___) /   ) /   /   ) /   )
#  _(___/___(___ _/___/_/___/___/_(___/_
#                                    /  
#                                (_ /   
# Quellen:
# https://de.wikipedia.org/wiki/Dijkstra-Algorithmus


import sys
import colorama
import copy
import time
import cmd
import math
import random


def _searchMaxLine(filename):
    ''' Hilfsfunktion fuer convertFileToField, welche die Laengste Zeile eines Bildes/Feldes ermittelt
        
        Args:
            filename (string): Name der Datei in der sich das Feld befindet
        Returns:
            max (int): Laenge der laengsten Zeile
    '''

    _max = []

    f = open(filename, "r")
    line = f.readline()

    while line:
        # Erzeuge leeres Spielfeld
        _max.append(len(line))
        line = f.readline()

    f.close() 

    return max(_max)
    
def convertFileToField(filename, emptyMarker, filledMarker):
    ''' Erstellt ein Feld als Liste aus einer .txt Datei, welche das Feld beinhaltet
        
        Args:
            filename (string): Dateiname
            emptyMarker (string): Zeichen mit dem <nichts> gefuellt wird
            filledMarker (string): Zeichen mit dem das Feld in der Liste aufgebaut wird
        Returns:
            field (lst): Fertiges Spielfeld als Liste, welche ebenfalls Listen enthaelt (2D-Array)
    '''

    field = []

    f = open(filename, "r")
    line = f.readline()

    _maxLine = _searchMaxLine(filename)

    while line:
        # Erzeuge leeres Spielfeld
        field.append([emptyMarker] * (_maxLine - 1))
        line = f.readline()

    f.close() 

    # Fuelle Feld
    f = open(filename, "r")
    line = f.readline()
    
    counter = 0
    while line:
        for j in range (0, len(line) - 1):
            field[counter][j] = line[j]
        line = f.readline()
        counter = counter + 1

    return field

def isFree(rowNumber, colNumber, arr):
    ''' Ueberprueft Feldposition auf Gueltigkeit
        
        Args:
            rowNumber (int): Zeile 
            colNumber (int): Spalte
            arr (lst): Spielfeld
        Returns:
            bool: True falls Feld leer -- sonst False
    '''
    if arr[rowNumber][colNumber] is not filledMarker:
        return True
    else:
        return False

def isEscape(rowNumber, colNumber, arr):
    ''' Ueberprueft ob Feldposition Ausgang ist
        
        Args:
            rowNumber (int): Zeile 
            colNumber (int): Spalte
            arr (lst): Spielfeld
        Returns:
            bool: True falls Feld Ausgang -- sonst False
    '''
    if arr[rowNumber][colNumber] is escapeSymbol:
        return True
    else:
        return False

def nodeVisited(rowNumber, colNumber, route):
    '''Docstring'''
    if (rowNumber, colNumber) in route:
        return True
    else:
        return False

def dijkstraInit(arr, start):
    ''' Erzeugt <leere> Karte. <-1> symbolisiert dabei ein leeres bzw. nicht besuchtes Feld'''

    # Menge aller Knoten im Graphen
    Q = []

    for i in range(0, len(arr)):
        for j in range(0, len(arr[i])):
            if arr[i][j] is 'x':
                pass
            else:
                # Abstand, Vorgänger, Route
                arr[i][j] = [math.inf, (None), ()]
                Q.append([(i, j), math.inf])
    # Abstand Startposition 0
    arr[start[0]][start[1]] = [0, (None), ()]
    # TODO: Für zufälligen Startpunkt anpassen
    Q[0][1] = 0

    return arr, Q

def _searchNode(Q):
    '''Sucht Knoten mit kürzestem Abstand'''
    mNode = min(Q, key = lambda t: t[1])
    return mNode

def distanz_update(u, v, routeMap, parentNode, Q):
    # Weglaenge bis zum Knoten u
    pathCostToU = u[1]

    # Weglaenge zum Nachbarn -- Kantengewicht immer 1
    pathWeightCost = 1

    alternativ = pathCostToU + pathWeightCost

    if alternativ < routeMap[v[0]][v[1]][0] or routeMap[v[0]][v[1]][0] is math.inf:
        routeMap[v[0]][v[1]][0] = alternativ    # Neue kurze Distanz zum Knoten
        routeMap[v[0]][v[1]][1] = parentNode    # Elterknoten setzen
        routeMap[v[0]][v[1]][2] = routeMap[parentNode[0]][parentNode[1]][2] + (v, )        # Route erweitern

        # Neuer Distanzwert in Q
        for line in Q:
            if line[0] == v:
                line[1] = alternativ
                break

    #cmd.printMap(routeMap)
    return Q

def dijkstra(arr, start, exitCoord):
    ''' Baue Karte mit Weglängen auf'''
    # Abstand, Vorgänger, Route
    routeMap, Q = dijkstraInit(arr, start)

    # Testfelder
    # cmd.printMap(routeMap)
    # cmd.printPathLen(routeMap)

    # Startpunkt von dem aus Karte aufgebaut wird
    u = [(start[0], start[1]), 0]
    routeMap[start[0]][start[1]][2] = (u[0],)

    while Q:
        u = _searchNode(Q)  # Suche Knoten mit kleinstem Abstand
        
        # Definition
        rowNumber = u[0][0]
        colNumber = u[0][1]
        nNodes = list()     # Liste mit Nachbarknoten um naechstes u zu bestimmen
        currentNode = (rowNumber, colNumber) # Vorgaengerknoten
        parentNode = routeMap[rowNumber][colNumber][1]

        Q.remove(u)         # Entferne Knoten aus Menge Q

        if u[0] == exitCoord:
            break

        # Besuche alle Nachbarn vom Knoten
        steps = ((0,1), (0, -1), (1, 0), (-1, 0))
        for s in steps:
            rN = rowNumber + s[0]
            cN = colNumber + s[1]

            v = (rN, cN)    # Nachbarknoten          

            _tempDict = dict(Q) # Trick um Knoten zu suchen
            # Falls Nachbarsknoten in Q verfuegbar
            if v in _tempDict:
                Q = distanz_update(u, v, routeMap, currentNode, Q)

            # Ausserhalb des Feldes
            if rowNumber < 0 or rowNumber >= len(arr) - 1 or colNumber < 0 or colNumber >= len(arr[rowNumber]) - 1:
                pass
            else:
                # Nehme Knoten nur auf wenn dieser auch besucht werden kann
                if isFree(rN, cN, arr) and v != parentNode:
                    nNodes.append((v, routeMap[rN][cN][0])) 

    return routeMap  
 
def searchExit(arr, start, route=()):
    '''Such die Koordinaten vom Ausgang'''

    # Definition
    rowNumber = start[0]
    colNumber = start[1]
    exitCoord = ()

    # Ausserhalb des Feldes
    if rowNumber < 0 or rowNumber >= len(arr) - 1 or colNumber < 0 or colNumber >= len(arr[rowNumber]):
        return

    route += ((rowNumber, colNumber),)

    # Ist aktuelle Zelle Ausgang? -> Ja: Speicher Pfad ab und return
    if isEscape(rowNumber, colNumber, arr):
        exitCoord = (rowNumber, colNumber)
        return exitCoord

    steps = ((0, 1), (0, -1), (1, 0), (-1, 0))
    myRoutes = []

    for s in steps:
        newRow = rowNumber + s[0]
        newCol = colNumber + s[1]

        if isFree(newRow, newCol, arr) and not nodeVisited(newRow, newCol, route):
            _route = copy.deepcopy(route)
            exitCoord = searchExit(arr, (newRow, newCol), _route)
            if exitCoord:
                return exitCoord

    return exitCoord
           
def main():
    '''Main Fkt'''

    colorama.init()

    # Globale Variablen
    global filledMarker
    global escapeSymbol

    # Definition der Variablen
    emptyMarker = ''
    filledMarker = 'x'
    escapeSymbol = 'E'
    startPos = (1, 1)

    # Erstelle Feld
    arr = convertFileToField("field3.txt", emptyMarker, filledMarker)

    print("Suche Ausganskoordinaten...")
    #exitCoord = searchExit(arr, startPos)
    #print(exitCoord)

    print("Berechne Ausgangspfad...")
    
    # 
    exitCoord = (15, 46)

    s = time.perf_counter()
    solution_full = dijkstra(copy.deepcopy(arr), startPos, exitCoord)
    e = time.perf_counter()
    solution_path = solution_full[exitCoord[0]][exitCoord[1]][2]

    print("Berechnungszeit in [s]: ", e-s)
    print()

    solution_field = cmd.fillField(arr, solution_path)
    cmd.printField(solution_field)


if __name__ == "__main__":
    main()