#3.feladat:	Írd ki  50-900-ig a páros számokat, amik oszthatók 11-el, egy sorba  álló függőleges vonallal (|)  elválasztva. (ne egyesével gépeld be őket, az nem jó megoldás!) A megoldásodat for-al és while-al is valósítsad meg! (19 pont)

import math
def harmadik():

    for i in range(50, 901):
        if i % 2 == 0 and i % 11 == 0:
            print((i)+"|", end="")

