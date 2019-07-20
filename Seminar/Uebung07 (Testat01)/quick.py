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

import time

def quickSort(A):

    _start = time.perf_counter()

    n = len(A)
    recQuickSort(A, 0, n-1)

    _end = time.perf_counter()

    return _end - _start

def recQuickSort(A, first, last):
    if first >= last:
        return
    else:
        pivot= A[first]
        pivotPos= partitionArray(A, first, last)
        recQuickSort(A, first, pivotPos-1)
        recQuickSort(A, pivotPos+ 1, last)

def partitionArray(A, first, last):
    pivot = A[first]
    left = first + 1
    right = last
    while left <= right: # solange Partitionierung nicht abgeschlossen
        while (left <= right) and (A[left] < pivot):# finde Schl�ssel gr��er Pivot
            left += 1
        while (right >= left) and (A[right] >= pivot): # finde Schl�ssel kleiner Pivot
            right -= 1
        if left < right:# vertausche beide Schl�ssel falls Partitionierung noch nicht beendet
            A[left], A[right] = A[right], A[left]
    if right != first: # Pivot-Element an die richtigeStellebringen
        A[first] = A[right]
        A[right] = pivot

    return right # liefere Position des Pivot-Elements zur�ck