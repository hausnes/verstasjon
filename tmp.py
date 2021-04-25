import time
#import dht11
import requests
import random

# NB: Ikkje del i ein "vanleg situasjon", bytt ut og bruk DIN EIGEN KEY
API_KEY  = '3BZPWB00E7V3RZWW' # BYTT UT DENNE NØKKELEN!
API_URL  = 'https://api.thingspeak.com/update'
SLEEP    = 15

def get_data_from_raspberry():
	while True:
		#result = dht11_sensor.read()
		temperatur = random.randint(0,20)
		fukt = random.randint(40,60)
		trykk = random.randint(900,1100)

		print("Temperatur: %d C" % temperatur)
		print("Fukt: %d %%" % fukt)
		print("Trykk: %d" % trykk)

		send_data_to_thingspeak(temperatur, fukt, trykk)

		time.sleep(SLEEP)

def hentDataFraThingspeak(temperatur, fukt, trykk):
    data = {'api_key': API_KEY, 'field1':temperatur, 'field2':fukt, 'field3':trykk};
    resultat = requests.post(API_URL, params=data)
    print(resultat.status_code)
    if resultat.status_code == 200: # "godkjent"
        print("Suksess! Fekk kobla til og sendt til Thingspeak.")
    else:
        print("Feil, problem med å kontakte Thingspeak.")

def main():
	get_data_from_raspberry()

main()