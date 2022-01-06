from datetime import datetime # For aa handtere tidspunkt og timing av maalingar
import time
import requests # For aa handtere aa sende data til Thingspeak
import sys
from csv import writer
import csv

# Dine unike innstillingar for Thingspeak
# Endre til din nokkel
API_KEY  = 'L59DSUZUOKBP8PEQ' # NB: Ikkje del i ein "vanleg situasjon", og ikkje bruk min nokkel!
API_URL  = 'https://api.thingspeak.com/update'
# PS: Kven som helst kan sjå live data på: 

# Sensorar
# Lys, avstand (proximity)
try:
    # Transitional fix for breaking change in LTR559
    from ltr559 import LTR559
    ltr559 = LTR559()
except ImportError:
    import ltr559

from bme280 import BME280 # Temperatur, luftfuktighet og trykk
from pms5003 import PMS5003, ReadTimeoutError as pmsReadTimeoutError # Partikkelsensor
from enviroplus import gas

# BME280 sensor for temperatur/trykk/fuktigheit
bme280 = BME280()

# PMS5003 partikkelsensor
pms5003 = PMS5003()

# Innstillingar
tidsstempel = datetime.now() # Tidspunktet programmet startar
forsinkelse = 15 #sekunder

# Hentar data fraa sensorane
def hentData():
    listeVerdata = [] # Ei tom liste som skal innehalde data
    
    listeVerdata.append(datetime.now()) # Legg til tidspunkt for avlesing

    temperatur = bme280.get_temperature()
    listeVerdata.append(temperatur) # Legg til temperatur
    trykk = bme280.get_pressure()
    listeVerdata.append(trykk) # Legg til trykk
    fuktighet = bme280.get_humidity()
    listeVerdata.append(fuktighet) # Legg til fuktighet
    lys = ltr559.get_lux()
    listeVerdata.append(lys) # Legg til lys
    
    try:
        dataPM1 = pms5003.read()
    except pmsReadTimeoutError:
        print("Feil ved avlesing av PMS5003, pm1")
        dataPM1 = 0
    else:
        dataPM1 = float(dataPM1.pm_ug_per_m3(1.0))
        listeVerdata.append(dataPM1)
    
    try:
        dataPM25 = pms5003.read()
    except pmsReadTimeoutError:
        print("Feil ved avlesing av PMS5003, pm2.5")
        dataPM25 = 0
    else:
        dataPM25 = float(dataPM25.pm_ug_per_m3(2.5))
        listeVerdata.append(dataPM25)

    try:
        dataPM10 = pms5003.read()
    except pmsReadTimeoutError:
        print("Feil ved avlesing av PMS5003, pm10")
        dataPM10 = 0
    else:
        dataPM10 = float(dataPM10.pm_ug_per_m3(10))
        listeVerdata.append(dataPM10)

    return listeVerdata # Returnerer svaret

# Programloopen, koyrer til du avsluttar med CTRL+C
try:
    with open('verdata.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        while True:
            tidNo = datetime.now()
            dt = tidNo - tidsstempel
            #print(dt.seconds)
            if dt.seconds > forsinkelse:
                dataTilSending = hentData()
                writer.writerow(dataTilSending)
                tidsstempel = datetime.now()
except KeyboardInterrupt: # Kontrollert avslutning med CTRL + C
    print("Avsluttar...")
    sys.exit(0)