# Verstasjon: Enviro HAT+, Raspberry PI og Thingspeak
Raspberry PI-basert verstasjon som loggar til Thingspeak. Opnar for fleire alternativ til logging etterkvart.

For IM, ToF og andre som måtte vere interessert.

## Del 1: Installasjon
Sensoren me tek utgangspunkt i er [Enviro HAT+](https://github.com/pimoroni/enviroplus-python). **NB: Følg installasjonsinstruksjonar i denne lenka!**

## Del 2: Enkeltfunksjonalitet
Oversikt over filene og kva dei inneheld:
- **eks1**: Enkelt eksempel på korleis du kan vente mellom kvar registrering utan å bruke sleep-funksjonen. Sleep fører til potensielle problem med å lese av korrekte data (samanlikn med korleis eit kamera treng litt tid til å fokusere og registrere lysnivå før det tek bilete).
- **eks2**: Enkelt eksempel på korleis du kan lese av alle sensorane frå Enviro+ og partikkelsensoren.
- **eks3**: Enkelt eksempel på korleis du kan skrive data til Thingspeak sin IoT-tjeneste. NB: Merk at eg har oppgitt min private API-nøkkel. Endre denne til din eigen når du skal teste.
- **eks4**: Enkelt eksempel på korleis du kan koble til ein MySQL-database og skrive data til denne.
- **eks5**: Enkelt eksempel på korleis du kan blur-e eit bilete (gjere det uskarpt) ved å bruke Pillow-biblioteket.
- **eks6**: Enkelt eksempel på korleis du kan lage eit enkelt brukargrensesnitt ved å bruke guizero-biblioteket.

## Del 3: "Sy saman"
**v1** inneheld per no den siste versjonen av koden som koblar saman all denne funksjonaliteten. Forbetringspotensiale her, endringar kjem.

## Tips og forslag til framgangsmåte:
1. Få eksempel 1-3 til å fungere kvar for seg, og "leik" og tilpass deretter desse til dine behov.
2. Slå saman til eit ferdig program som kombinerer dei tre "teknikkane". Løysingsforslag v1 i **verstasjon_ferdig_v1.py**.

Dersom du bruker [Netlify](https://www.netlify.com) så kan du få publisert eit repository sin HTML gratis. Ein "plasshaldar"-versjon av nettsida til verstasjonen ser du her:
[Nettside for verstasjon](https://verstasjon.netlify.app/)

Kan du vise fram resultata frå Thingspeak på ein eller annan måte? Hint: Sjå kva du finn hjå ThingSpeak.

## MySQL:
Tips til korleis du kan sette opp og jobbe med MySQL-serveren (som per no køyrer på ein PI v1 i klasserommet, sjå passord på boksen). Denne tillet tilkoblingar via Workbench dersom du bruker TCP/IP saman med SSH. Sjå lenker under. 
- https://pimylifeup.com/raspberry-pi-mysql/
- https://howtoraspberrypi.com/enable-mysql-remote-connection-raspberry-pi/
- https://pimylifeup.com/raspberry-pi-phpmyadmin/