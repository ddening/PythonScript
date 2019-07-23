#  _____________________________________
#                                       
#          /               ,            
#  ----__-/----__----__--------__----__-
#    /   /   /___) /   ) /   /   ) /   )
#  _(___/___(___ _/___/_/___/___/_(___/_
#                                    /  
#                                (_ /   
# Quellen:
#

import colorama
from colorama import Fore as color
import math

def fillField(arr, path):
    ''' Visuelle Darstellung des Loesungspfades'''

    for coord in path:
        arr[coord[0]][coord[1]] = color.RED + 'e' + color.RESET

    arr[path[0][0]][path[0][1]] = color.GREEN + 'A' + color.RESET
    arr[coord[0]][coord[1]] = color.GREEN + 'E' + color.RESET
    return arr

def printField(field):
    ''' Gibt das Spielfeld in der Konsole aus
        
    Args: 
        field (lst): Enthaelt das gesamte Spielfeld
    Returns:
        None
    '''

    for i in range(0, len(field)):
        _string = ""
        for j in range(0, len(field[i])):
            _string = _string + field[i][j]
        print(_string)
    print()
    
def printMap(map):
    '''Gibt Karte mit Farbkodierung aus'''
    for line in map:
        for c in line:
            if type(c) is list:
                if c[0] is math.inf:
                    print(color.CYAN + 'u' + color.RESET, end= ' ')     # unvisited
                elif c[0] is 0:
                    print(color.GREEN + 'A' + color.RESET, end= ' ')    # Anfang
                else:
                    print(color.RED + 'v' + color.RESET, end= ' ')    # visited
            else:
                print(color.LIGHTWHITE_EX + c + color.RESET, end= ' ')
        print()
    print()

def printPathLen(map):
    '''Gibt Karte mit Farbkodierung aus'''
    for line in map:
        for c in line:
            if type(c) is list:
                if c[0] is 0:
                    print(c[0], end= ' ')
                else:
                    print(color.YELLOW + 'i' + color.RESET, end= ' ')
            else:
                print(c, end= ' ')
        print()
    print()

