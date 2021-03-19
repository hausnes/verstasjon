# verstasjon
Raspberry PI-basert verstasjon som loggar til Thingspeak.

For IM, ToF og andre som måtte vere interessert.

Oversikt over filene og kva dei inneheld:
- eks1: Enkelt eksempel på korleis du kan vente mellom kvar registrering utan å bruke sleep-funksjonen. Sleep fører til potensielle problem med å lese av korrekte data (samanlikn med korleis eit kamera treng litt tid til å fokusere og registrere lysnivå før det tek bilete).
- eks2: Enkelt eksempel på korleis du kan lese av alle sensorane frå Enviro+ og partikkelsensoren.
- eks3: Enkelt eksempel på korleis du kan skrive data til Thingspeak sin IoT-tjeneste. NB: Merk at eg har oppgitt min private API-nøkkel. Endre denne til din eigen når du skal teste.

v1 inneheld per no den siste versjonen av koden som koblar saman all denne funksjonaliteten. Forbetringspotensiale her, endringar kjem.

Forslag til framgangsmåte:
1. Få eksempel 1-3 til å fungere for seg sjølv, "leik" og tilpass desse til dine behov.
2. Slå saman til eit ferdig program som kombinerer dei tre "teknikkane".
