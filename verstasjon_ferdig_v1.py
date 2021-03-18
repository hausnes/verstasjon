from datetime import datetime # For aa handtere tidspunkt og timing av maalingar
import requests # For aa handtere aa sende data til Thingspeak

# Dine unike innstillingar for Thingspeak
# Endre til din nokkel
API_KEY  = '3BZPWB00E7V3RZWW' # NB: Ikkje del i ein "vanleg situasjon", og ikkje bruk min nokkel!
API_URL  = 'https://api.thingspeak.com/update'
# PS: Kven som helst kan sjå live data på: https://thingspeak.com/channels/1312133

# Sensorar
# BME280 sensor for temperatur/trykk/fuktigheit
from bme280 import BME280
bme280 = BME280()

# Innstillingar
tidsstempel = datetime.now() # Tidspunktet programmet startar
forsinkelse = 15 #sekunder

# Sender data til Thingspeak, gjer feilmelding om problem
def send_data_til_thingspeak(temperatur, fukt, trykk):
    data = {'api_key': API_KEY, 'field1':temperatur, 'field2':fukt, 'field3':trykk}; # Sjekk dette opp mot korleis du satte opp Thingspeak
    resultat = requests.post(API_URL, params=data)
    print(resultat.status_code)
    if resultat.status_code == 200: # "godkjent"
        print("Suksess, sendt til Thingspeak.")
    else:
        print("Feil, ikje sendt til Thingspeak.")

# Hentar data fraa sensorane
def hentData():
    listeVerdata = [] # Ei tom liste som skal innehalde data
    trykk = bme280.get_pressure()
    listeVerdata.append(trykk) # Legg til trykk
    temp = bme280.get_temperature()
    listeVerdata.append(temp) # Legg til temperatur
    fukt = bme280.get_humidity()
    listeVerdata.append(fukt) # Legg til fuktighet

    listeVerdata.append(datetime.now()) # Legg til tidspunkt for avlesing

    return listeVerdata # Returnerer svaret

# Programloopen, koyrer til du avsluttar med CTRL+C
while True:
    data = hentData()
    dt = data[-1] - tidsstempel # Kva trur du -1 betyr?
    #print(dt.seconds)
    if dt.seconds > forsinkelse:
        dataTilSending = hentData()
        print("Full liste denne runden:",dataTilSending," - forsoker aa sende til Thingspeak...")
        send_data_til_thingspeak(dataTilSending[1],dataTilSending[2],dataTilSending[0])
        tidsstempel = datetime.now()