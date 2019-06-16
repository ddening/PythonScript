import random
import time
import matplotlib.pyplot
import copy

def bubbleSort(alist):
    #Zeit starten
    startTime = time.perf_counter()
    #Schleife für die Länge des übergebenen Arrays
    for j in range(len(alist)):
        #Hilfsvariable für fertige Sortierung
        swapFlag = False
        i = 0
        while i<len(alist)-1:
            #Vergleiche, ob nächstes Element ist größer als aktuelles
            if alist[i]>alist[i+1]:
                #Tausche und setzte Hilfsvariable
                alist[i],alist[i+1] = alist[i+1],alist[i]
                swapFlag = True
            i = i+1
        #Wenn Hilfsvariable swapFlag == False ist Liste sortiert und Schleife kann abgebrochen werden
        #Zeit wird errechnet und in die Liste geschrieben
        if swapFlag == False:
            elapsedTime = time.perf_counter() - startTime
            bubbleSortTimes.append(elapsedTime)
            break


def insertionSort(alist):
    #Siehe: http://interactivepython.org/runestone/static/pythonds/SortSearch/TheInsertionSort.html
    #Zeit starten
    startTime = time.perf_counter()

    #Schleife über die Länge des Arrays
    for index in range(1,len(alist)):
        #Position und Wert zwischenspeichern
        currentvalue = alist[index]
        position = index

        #Elemente vergleichen, wenn kleiner dann shifte nach rechts solange bis daa aktuelle Element kleiner ist
        #als dasjeneige in der Liste
        while position > 0 and alist[position - 1] > currentvalue:
            alist[position] = alist[position - 1]
            position = position - 1
        #Setzte das aktuelle Element
        alist[position] = currentvalue
    
    #Zeit errechnen und in Liste schreiben
    elapsedTime = time.perf_counter() - startTime
    insertionSortTimes.append(elapsedTime)

    

def selectionSort(alist):
    #Siehe: http://interactivepython.org/runestone/static/pythonds/SortSearch/TheSelectionSort.html
    #Zeit starten
    startTime = time.perf_counter()

    for fillslot in range(len(alist) - 1,0,-1):
        positionOfMax = 0
        for location in range(1,fillslot + 1):
            if alist[location] > alist[positionOfMax]:
                positionOfMax = location

        temp = alist[fillslot]
        alist[fillslot] = alist[positionOfMax]
        alist[positionOfMax] = temp

    elapsedTime = time.perf_counter() - startTime
    selectionSortTimes.append(elapsedTime)
    #print("Selections Sort: ", elapsedTime)
    #return alist

def testListsGenerator(maxLength):
    listStart = 0
    listEnd = 99
    rand_list =[]
    rand_nums =[]

    for i in range(1, maxLength+1):
        for j in range(1, i+1):
            rand_nums.append(random.randint(listStart, listEnd))

        rand_list.append(rand_nums)
        rand_nums = []

    return rand_list 


#
#------
#
bubbleSortTimes = []
insertionSortTimes = []
selectionSortTimes = []
xNumbers = []
maxLength = 1000


fig = matplotlib.pyplot.figure()
# Erzeugen eines axes-Objekts in figure. Dies entspricht der Funktion subplot in Matlab.
ax = fig.add_subplot(1,1,1)

randList = testListsGenerator(maxLength)
print(randList)
for o in range(1,maxLength):
    xNumbers.append(o)

    bubbleSort(copy.copy(randList[o]))
    insertionSort(copy.copy(randList[o]))
    selectionSort(copy.copy(randList[o]))
    # bubbleSort(randList[o].copy())
    # insertionSort(randList[o].copy())
    # selectionSort(randList[o].copy())

#print(bubbleSortTimes)

ax.plot(xNumbers, bubbleSortTimes, xNumbers, insertionSortTimes, xNumbers, selectionSortTimes)
ax.legend(['Bubble Sort', 'Insertion Sort', 'Selection Sort'])

# Erzeugen der x-Achsen-Beschriftung. Dies entspricht der Funktion xlabel in Matlab.
ax.set_xlabel('Listengröße')#
# Erzeugen der y-Achsen-Beschriftung. Dies entspricht der Funktion ylabel in Matlab.
ax.set_ylabel('Zeit')
# Anzeigen der Grafik in einem Fenster.
matplotlib.pyplot.show()
#print()
#print(randList)
#print(insertionSort(randList.copy()))
#print(randList)
#print(selectionSort(randList.copy()))

