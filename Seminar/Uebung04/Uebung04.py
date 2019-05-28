# Seminar Uebung 04

import random

def main():
    myListe = []

    for i in range(0, 5):
        myListe.append((random.random(), random.random()))   
    print(myListe)  

main()