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

## Del 3: "Sy saman"
**v1** inneheld per no den siste versjonen av koden som koblar saman all denne funksjonaliteten. Forbetringspotensiale her, endringar kjem.

## Tips og forslag til framgangsmåte:
1. Få eksempel 1-3 til å fungere kvar for seg, og "leik" og tilpass deretter desse til dine behov.
2. Slå saman til eit ferdig program som kombinerer dei tre "teknikkane". Løysingsforslag i **verstasjon_ferdig_v1.py**.

Dersom du bruker [Netlify](https://www.netlify.com) så kan du få publisert eit repository sin HTML gratis. Ein "plasshaldar"-versjon av nettsida til verstasjonen ser du her:
[Nettside for verstasjon](https://verstasjon.netlify.app/)

Kan du vise fram resultata frå Thingspeak på ein eller annan måte?