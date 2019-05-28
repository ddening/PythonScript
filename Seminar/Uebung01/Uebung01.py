# Seminar Uebung 01

import math

def ganzzahlDivision(num1, num2):
    print("\nWir befinden uns in der Fkt: ganzzahlDivision(): \n")
    _temp = num1 / num2
    _temp = math.floor(_temp)
    print(" ", num1, "//" , num2, "=", _temp, " \n")

def DivReal(num1, num2):
    print("\nWir befinden uns in der Fkt: DivReal(): \n")
    _temp = 0;

    if num1 < 0 or num2 < 2:
        _temp = abs(num1) / abs(num2)
        _temp = math.floor(_temp) * (-1)
    else:
        _temp = num1 / num2

    print(" ", num1, "//" , num2, "=", _temp, " \n")

def ModuloReal(num1, num2):
    print("\nWir befinden uns in der Fkt: ModuloReal(): \n")
    _temp = 0;

    if num1 < 0 or num2 < 2:
        _temp = (abs(num1) % abs(num2)) * (-1)
    else:
        _temp = num1 % num2

    print(" ", num1, "%" , num2, "=", _temp, " \n")

def main():
    print("In der main(): \n")
    # Wie lautet das Ergebnis von -10//3
    print("Ganzzahl Divison: ")
    myVar = -10//3      # = -4
    print(" -10 // 3 = ", myVar)

    myVar = 10//3
    print("  10 // 3 = ", myVar)

    print("\nModulo: ")
    myVar = -10 % 3;    # =  2
    print(" -10 % 3 = ", myVar)

    myVar = 10 % 3
    print("  10 % 3 = ", myVar)

    ganzzahlDivision(-10, 3)
    DivReal(-10, 3)
    ModuloReal(-10, 3)

main()
    