# Seminar Uebung 03

def main():
    # Lese Liste von Zahlen ein
    print("Bilde Mittelwert ueber die eingegebene Zahlen \n")
    print("Zum Beenden < -1 eingeben>")
 
    x = 0

    myList = []
    while x is not -1:
        x = int(input("Geben Sie eine Zahl ein: "))

        if x is -1:
            pass
        else:
            myList.append(x)

    # Bilde Mittelwert
    gesamt = 0

    for i in myList:
        gesamt += i
    gesamt = gesamt / len(myList)
    print("Mittelwert: ", gesamt)

main()