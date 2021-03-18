from time import sleep
from datetime import datetime
import random

# Innstillingar
tidsstempel = datetime.now()
forsinkelse = 5

def hentData():
    listeVerdata = []
    trykk = random.randint(1000,1100)
    listeVerdata.append(trykk)
    temp = random.randint(20,26)
    listeVerdata.append(temp)
    fukt = random.randint(34,66)
    listeVerdata.append(fukt)
    listeVerdata.append(datetime.now())
    return listeVerdata

while True:
    #tidsstempel = datetime.now()
    data = hentData()
    dt = data[-1] - tidsstempel
    #print(dt.seconds)
    if dt.seconds > forsinkelse:
        print("Full liste denne runden:",hentData())
        tidsstempel = datetime.now()