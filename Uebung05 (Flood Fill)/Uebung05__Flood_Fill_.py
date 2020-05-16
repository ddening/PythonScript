# Seminar Uebung 05 (Flood Fill)                         
#  _____________________________________
#                                       
#          /               ,            
#  ----__-/----__----__--------__----__-
#    /   /   /___) /   ) /   /   ) /   )
#  _(___/___(___ _/___/_/___/___/_(___/_
#                                    /  
#                                (_ /   
# Quellen:
# https://stackoverflow.com/questions/7370801/measure-time-elapsed-in-python

import copy
import colorama
import sys
from timeit import default_timer as timer

import control
import model

def main():
    ''' Docstring'''

    # === INIT ===
    colorama.init()
    sys.setrecursionlimit(10000)
    
    emptyMarker = " "
    filledMarker = "e"
    _emptyFieldCounter = 0

    # Felder Listen Definition
    emptyFields = []
    filledFields = []

    # Liste mit vorgefertigten Feldern und Startpunkt 
    fieldList = [("field.txt", (14, 39)), ("field2.txt", (7, 3)), ("field3.txt", (15, 20)), ("monalisa.txt", (41, 65)), ("laby1.txt", (7, 22))]

    # Erzeuge erstes "default" Feld aus Seminaraufgabe
    emptyFields.append(model.defaultField())
    filledFields.append(control.fillFlood(emptyFields[0], control.randomStartPoint(emptyFields[_emptyFieldCounter]), emptyMarker, filledMarker))
    _emptyFieldCounter = _emptyFieldCounter + 1
    
    # Erzeuge und fülle Felder aus .txt Dateien
    for filename in fieldList:
  
        start = timer()

        # Liste mit leerem Feld erweitern
        emptyFields.append(control.convertFileToField(filename[0], emptyMarker, filledMarker))

        end = timer()
        print("Zeit convertFiletoField für Feld Nr. %i [in s]: " % _emptyFieldCounter, end - start)
        

        try:
            # Liste mit gefülltem Feld erweitern
            filledFields.append(control.fillFlood(emptyFields[_emptyFieldCounter], control.randomStartPoint(emptyFields[_emptyFieldCounter]), emptyMarker, filledMarker))
            #control.randomStartPoint(emptyFields[_emptyFieldCounter])
            _emptyFieldCounter = _emptyFieldCounter + 1
        except:
             e = sys.exc_info()[0]
             print(e)
             e = sys.exc_info()[1]
             print(e)
             e = sys.exc_info()[2]
             print(e)
    
    # Ausgabe der Felder
    if not control.VISUAL:
        for i,j in zip(filledFields, emptyFields):
            print("\n\n\n")
            control.printField(i)
            #control.doublePrint(j, i)
   
main()