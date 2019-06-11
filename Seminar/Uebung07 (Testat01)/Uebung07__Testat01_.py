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

# Globale scope
MAX_LEN = 10

def testListsGenerator(MAX_LEN):
    pass

def myPrint(arr):
    print("______" * len(arr))
    print("| ", end = "")
    for i in arr:
        print(i , " | ", end="")
    #print("______" * len(arr))

def bubbleSort(unsortedList):
    ''' Docstring '''
    n = len(unsortedList)

    for i in range(0, n):
        for j in range(0, n-i-1):
            if unsortedList[j] > unsortedList[j+1]:
                unsortedList[j], unsortedList[j+1] = unsortedList[j+1], unsortedList[j]
                myPrint(unsortedList)
    return unsortedList

def inerstionSort():
    ''' Docstring '''
    pass
    
def selectionSort():
    '''Docstring'''
    pass

def main():
    arr = [1,5,3,12,6,213,12,4,123,12,5]
    r = bubbleSort(arr)
    pass
main()