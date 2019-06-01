# Seminar Uebung 06 (Golden Section Search)                         
#  _____________________________________
#                                       
#          /               ,            
#  ----__-/----__----__--------__----__-
#    /   /   /___) /   ) /   /   ) /   )
#  _(___/___(___ _/___/_/___/___/_(___/_
#                                    /  
#                                (_ /   
# Quellen:
# https://www.youtube.com/watch?v=hLm8xfwWYPw
# http://num.math.uni-goettingen.de/werner/gold.pdf
# https://de.wikipedia.org/wiki/Goldener_Schnitt
# https://www.tu-ilmenau.de/fileadmin/media/simulation/Lehre/Vorlesungsskripte/OPT1/OS1-kapitel-5.pdf
# https://stackoverflow.com/questions/48847962/what-does-o-mean-in-matplotlibs-plot-function
# https://matplotlib.org/users/pyplot_tutorial.html
# https://python-reference.readthedocs.io/en/latest/docs/str/formatting.html


import matplotlib.pyplot

def func(x):
    ''' Docstring '''
    return (x+(1/3))**2

def _plot(a, b, minimum):
    ''' Docstring '''
    
    # Allg. Definition
    intervall = (a - 3, b + 3)      # Erweiter Intervall zum Plotten
    _height = 1                     # Hilfsvariable

    # Bestimme Maximum zum Plotten der Intervallhoehe
    if abs(a) > abs(b):
        _height = a * 1.1
    else:
        _height = b * 1.1

    fig = matplotlib.pyplot.figure()
    ax = fig.add_subplot(1,1,1)

    # Funktion [x ; y]
    ax.plot([i for i in range(intervall[0], intervall[1])], [func(i) for i in range(intervall[0], intervall[1])], color='c')
    # Minimum plotten
    ax.plot(minimum, func(minimum), 'o', color='m')
    # Initial Intervall
    ax.plot([a] * int(func(_height)), [i for i in range(0, int(func(_height)))], '--', color='r')
    ax.plot([b] * int(func(_height)), [i for i in range(0, int(func(_height)))], '--', color='r')

    ax.legend(['(x+1/3)**2', 'Minimum: %.3g' % minimum, 'Intervallgrenzen'])
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')
    matplotlib.pyplot.show()

def goldenSearch(a, b):
    ''' Docstring '''

    # Definition
    phi = ((1+(5**0.5))*0.5) - 1     # Kehrwert der <GoldenRatio> # 0.618
    epsilon = 0.001 # Genauigkeit
    minimum = -1

    if b - a < 0:
        print("Fuer das Intervall muss gelten a < b")
        return -1

    # Abbruchkriterium
    while b -a > epsilon:

        # Strecke maximal
        s = b - a
        # laengere Seite
        l = s * phi

        # Setze Intervall der GoldenRatio
        x1 = a + l
        x2 = b - l

        # Neue Grenze setzen
        if func(x2) > func(x1):
            a = x2
        elif func(x1) > func(x2):
            b = x1  

    # Berechne Minimum
    minimum = (a+b)/2
    return minimum
                     

def main():
    # Intervall [a, b]
    a = -12
    b = 12

    _minimum = goldenSearch(a, b)
    _plot(a, b, _minimum)

main()
