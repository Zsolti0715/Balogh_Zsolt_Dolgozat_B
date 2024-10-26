#5.feladat:	Írd ki a -90 és 160 közötti számokat felkiáltó jelel elválasztva egy sorba, úgy hogy az utolsó után ne legyen felkiálltójel. A tanult két fajta módon is valósítsad meg a programod.

def otos():
     for i in range(-91,160,1):
           print(str(i)+"!", end="")


def otosb():
    i = -91
    while i<161:
        print(str(i)+"!" , end="")
        i+=1