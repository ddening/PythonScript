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

# Libraries
import random
import time
import matplotlib.pyplot

# Globale scope
MAX_NUMBERS_IN_LIST = 200

''' ======= TODO =======
+ Sortieralgorithmen implementieren

+ Liste mit Listen zu sortierender Elemente erstellen

+ Sichere Kopie dieser Listen erstellen, um diese in den anderen Verfahren zu nutzen,
  damit Sortierung mit den jeweils gleichen Listenelementen in gleicher Reihenfolge stattfindet.

+ Alle Grafen in einem Plot darstellen
'''

def testListsGenerator(MAX_NUMBERS_IN_LIST):
    ''' Docstring '''

    # Definition einer leeren Liste
    myList = []
    # Fülle Liste mit zufälligen Zahlen
    myList = [random.randint(0, 999) for i in range(0, MAX_NUMBERS_IN_LIST)]

    return myList
    
def _plot():
    ''' Docstring '''

    fig = matplotlib.pyplot.figure()
    ax = fig.add_subplot(1,1,1)

    # Erstelle Zufallsliste
    # _temp = testListsGenerator(MAX_NUMBERS_IN_LIST)

    # Funktion [x ; y]
    # x: Anzahl der Elemente -- y: Zeit zum sortieren

    ax.plot([len(testListsGenerator(i)) for i in range(0, MAX_NUMBERS_IN_LIST)], [bubbleSort(testListsGenerator(j)) for j in range(0, MAX_NUMBERS_IN_LIST)], '.', color='c')

    ax.set_xlabel('Anzahl Elemente in Liste')
    ax.set_ylabel('Sortierzeit in s')
    matplotlib.pyplot.show()

def bubbleSort(arr):
    ''' Docstring '''
    n = len(arr)

    start = time.clock()

    for i in range(0, n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    end = time.clock()

    # print("Zeit in s: ", end - start)

    return end-start

def inerstionSort():
    ''' Docstring '''
    pass
    
def selectionSort():
    '''Docstring'''
    pass

def main():
    arr = [1,5,3,12,6,213,12,4,123,12,5]
    #bubbleSort(testListsGenerator(MAX_NUMBERS_IN_LIST))
    #print(r)
    # testListsGenerator(MAX_NUMBERS_IN_LIST)
    _plot()
main()