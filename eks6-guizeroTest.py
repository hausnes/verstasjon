'''
Meir informasjon om å oppdatere GUI ved faste intervall
https://lawsie.github.io/guizero/blocking/

Meir informasjon om å bruke fleire vindu i same appen 
https://lawsie.github.io/guizero/window/
'''

from guizero import App, Text, Window, PushButton
import random

def visData():
    temperatur = hentData()
    samlaTekst = "Temperaturen er " + str(temperatur)
    text.value = samlaTekst

def hentData():
    temperatur = random.randint(5,10)
    return temperatur

def open_window():
    window.show(wait=True) # Fjern 'wait=True' dersom du ynskjer å kunne bruke begge vindua samtidig

app = App(title="Temperaturvisning", height=300, width=200)
window = Window(app, title = "Vindu nr. 2", height=300, width=200)
window.hide()
text = Text(app, text=visData)
text.repeat(1000, visData)  # Oppdaterer tekstfeltet sitt innhald kvar 1000ms (= 1s)
open_button = PushButton(app, text="Opne vindu nr. 2", command=open_window)
app.display()