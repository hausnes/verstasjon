from datetime import datetime # For aa handtere tidspunkt og timing av maalingar
import time
import requests # For aa handtere aa sende data til Thingspeak
import sys
from csv import writer
import csv

# Dine unike innstillingar for Thingspeak
# Endre til din nokkel
API_KEY  = 'xxxxxxxxxxxxxxxx' # NB: Ikkje del i ein "vanleg situasjon", og ikkje bruk min nokkel!
API_URL  = 'https://api.thingspeak.com/update'

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

# Sender data til Thingspeak, gjer feilmelding om problem
def send_data_til_thingspeak(temperatur, trykk, fuktighet, lys, pm1, pm25, pm10):
    data = {
        'api_key': API_KEY, 
        'field1':temperatur, 
        'field2':trykk, 
        'field3':fuktighet,
        'field4':lys,
        'field5':pm1,
        'field6':pm25,
        'field7':pm10,
    }; 
    resultat = requests.post(API_URL, params=data)
    print(resultat.status_code)
    if resultat.status_code == 200: # "godkjent"
        print("Suksess, sendt til Thingspeak.")
    else:
        print("Feil, ikkje sendt til Thingspeak.")
        # Boer me handtere dette? Me kan til doemes lagre i ein datastruktur (liste) og skrive innhaldet fraa denne naar me igjen "faar kontakt"

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

hentData() # Me koyrer ein uthenting umiddelbart for aa unngaa den foerste maalinga som alltid blir "paa viddene"

# Programloopen, koyrer til du avsluttar med CTRL+C
try:
    with open('verdata.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        while True:
            tidNo = datetime.now()
            dt = tidNo - tidsstempel
            #print(dt.seconds)
            if dt.seconds > forsinkelse:
                dataTilSending = hentData()
                # Skriv til Thingspeak
                print("Full liste denne runden:",dataTilSending," - forsoker aa sende til Thingspeak...")
                send_data_til_thingspeak(dataTilSending[1],dataTilSending[2],dataTilSending[3],dataTilSending[4],dataTilSending[5],dataTilSending[6],dataTilSending[7])
                # Skriv til CSV
                writer.writerow(dataTilSending)
                tidsstempel = datetime.now()
except KeyboardInterrupt: # Kontrollert avslutning med CTRL + C
    print("Avsluttar...")
    sys.exit(0)