from guizero import App, Text
import random

def visData():
    temperatur = hentData()
    samlaTekst = "Temperaturen er " + str(temperatur)
    text.value = samlaTekst

def hentData():
    temperatur = random.randint(5,10)
    return temperatur

app = App("Temperaturvisning")
text = Text(app, text=visData)
text.repeat(1000, visData)  # Oppdaterer tekstfeltet sitt innhald kvar 1000ms (= 1s)
app.display()

# Meir informasjon om å oppdatere GUI ved faste intervall
# https://lawsie.github.io/guizero/blocking/