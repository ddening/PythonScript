# Seminar Uebung 07 (Testa01)                         
#  _____________________________________
#                                       
#          /               ,            
#  ----__-/----__----__--------__----__-
#    /   /   /___) /   ) /   /   ) /   )
#  _(___/___(___ _/___/_/___/___/_(___/_
#                                    /  
#                                (_ /   
# Quellen:
# https://www.geeksforgeeks.org/bubble-sort/
# https://en.wikipedia.org/wiki/Bubble_sort

import time


def merge(arr, left, right, mid):
    '''Fuegt Listen zu einer gesamten Liste zusammen

    Args:
        arr     (lst)   : Unsortierte Liste mit Datensaetzen
        left    (int)   : Linke Seite des Arrays
        right   (int)   : Rechte Seite des Arrays
        mid     (int)   : Mitte des Arrays

    Returns:
        lst             : Liste mit allen Elementen
    '''

    pass

def mergeSort(arr, left, right):
    '''Sortiert eine uebergebene Liste mit dem MergeSort Algorithmus

    Args:
        arr     (lst) : Unsortierte Liste mit Datensaetzen
        left    (int) : Linke Seite des Arrays
        right   (int) : Rechte Seite des Arrays

    Returns:
        time (float): Benoetigte Zeit um Liste zu sortieren
    '''

    if left < right:   
        # Mitte des Arrays
        mid = (left + right)/2

        # Rekursiver Aufruf fuer linke Seite
        mergeSort(arr, left, m)
        # Rekursiver Aufruf fuer rechte Seite
        mergeSort(arr, right, m + 1)
