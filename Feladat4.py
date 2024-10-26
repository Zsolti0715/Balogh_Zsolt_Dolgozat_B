#4.feladat:	Kérj be a felhasználótól egy valósszámot. A programod számítsa ki a bekért érték felső egész részét(kerekítse felfele), ehhez a math csomag ceil() eljárását használd.
import math
def negyes():
    szam = float(input ("Kérem adjon meg egy valós számot!:"))
    print("A kerekített érték: "+(str(math.ceil (szam))))

