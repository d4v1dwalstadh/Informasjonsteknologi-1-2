import csv
import subprocess
from datetime import datetime
 

class Elev:
    def __init__(self, navn, fag1, fag2, fag3):
        """Klasse for eleven info, tar inn navn, email, fag 1-3 som streng. 
        Innehar metodene lag_klasselister og kontakt_elev"""
        self.navn = navn
        self.email = ((self.navn).replace(" ", ".")).casefold() + "@viken.no"
        self.fag1 = fag1
        self.fag2 = fag2
        self.fag3 = fag3
        self.klasse = None
        self.fagliste = [fag1, fag2, fag3]


    def lag_klasselister(elever, klasser):
        for i, elev in enumerate(elever):
            klasse = klasser[i % len(klasser)]
            elev.klasse = klasse
    
    def vis_dine_faglister(self):
        for fag in self.fagliste:
            print(f"{fag}: {fagliste[f"{fag}"]}, klasserom: {klasserom_oversikt[f"{fag}"]}")
        print(f"Fellesfag ({self.klasse}): {klasseliste[f"{self.klasse}"]}, klasserom: {klasserom_oversikt[self.klasse]}")
    


    def kontakt_elev(self):
        try:  
            # E-postadresse du ønsker å bruke som mottaker
            mottaker = self.email

            # Ditt AppleScript for å opprette et nytt utkast med en mottaker
            applescript_code = f'''
            tell application "Mail"
                activate
                set newMessage to make new outgoing message with properties {{subject:"", content:""}}
                tell newMessage
                    make new to recipient at end of to recipients with properties {{address:"{mottaker}"}}
                    open
                end tell
            end tell
            '''

            # Kjør AppleScript ved hjelp av subprocess
            subprocess.run(["osascript", "-e", applescript_code])
            
        except subprocess.CalledProcessError as error:
            print(f"Feil oppstod ved forsøk på å kontakte {self.navn}: {error}")
        except OSError as error:
            print(f"Kunne ikke kjøre AppleScript for {self.navn}. Feil: {error}. Sørg for at programmet kjører på macOS.")
                

    
# Opprett en tom liste for å lagre Elev-objekter
elever = {}

# Les inn CSV-filen
with open('elev_info.csv', newline='') as csvfil:
    elevleser = csv.reader(csvfil)
    next(elevleser)  # Hopper over overskriften hvis den finnes i CSV-filen
    for rad in elevleser:
        navn, fag1, fag2, fag3 = rad
        elev = Elev(navn, fag1, fag2, fag3)
        elever[navn] = elev

# Angir mulige klasser en kan komme i
klasser = ['3STA', '3STB', '3STC', '3STD']

# Fordel elevene jevnt på klasser
Elev.lag_klasselister(list(elever.values()), klasser)

# Oppretter klasselister
klasseliste = {}
for elev in elever.values():
    klasse = elev.klasse
    if klasse not in klasseliste:
        klasseliste[klasse] = []  # Oppretter nøkkel for klassene
    klasseliste[klasse].append(elev.navn)

# Opprett faglister
fagliste = {}
for elev in elever.values():
    for fag in elev.fagliste:
        if fag not in fagliste:
            fagliste[fag] = []
        fagliste[fag].append(elev.navn)
  

# Opprett oversikt over hvilke klasserom der hvert fag har sitt faste egne
klasserom_oversikt = {}
for i, fag in enumerate(fagliste):
    klasserom_oversikt[fag] = 300 + i
    # Angir klasserom for fellesfagene
for i, klasse in enumerate(klasser):
    klasserom_oversikt[klasse] = 300 + i


time_tider = {
    "forste_time": { 
        "start": datetime.strptime("08:30", "%H:%M"),
        "slutt": datetime.strptime("10:00", "%H:%M")
    },
    "andre_time": {
        "start": datetime.strptime("10:15", "%H:%M"),
        "slutt": datetime.strptime("11:45", "%H:%M")
    },
    "tredje_time": {
        "start": datetime.strptime("12:15", "%H:%M"),
        "slutt": datetime.strptime("13:45", "%H:%M")
    },
    "fjerde_time": {
        "start": datetime.strptime("14:00", "%H:%M"),
        "slutt": datetime.strptime("15:30", "%H:%M")
    }
}
# Oversikt over hvilke fag som går samtidig der a-b-c er programfag og d er fellesfag
time_bolker = {
    "bolk_a": ["R2", "S2"],
    "bolk_b": ["IT2", "Markedsføring og ledelse 2", "Fysikk 2", "Økonomistyring"],
    "bolk_c": ["Engelsk 2", "Filosofi", "Breddeidrett 2", "Psykologi"],
    "bolk_d": ["Norsk", "Historie", "Religion"]
}

timeplan = {
   "mandag": [elev.fag1, elev.fag2, elev.fag3, elev.klasse],
    "tirsdag": [elev.klasse, elev.fag1, elev.fag2, elev.fag3],
    "onsdag": [elev.fag1, elev.fag2, elev.fag3, elev.klasse],
    "torsdag": [elev.klasse, elev.fag1, elev.fag2, elev.fag3],
    "fredag": [elev.fag1, elev.klasse]
}




def finn_elev(elev_navn, klokke):
    try:
        elev = None
        for elev_obj in elever.values():
            if elev_obj.navn == elev_navn:
                elev = elev_obj
        # Konverter brukerens input til et datetime-objekt
        klokkeslett = datetime.strptime(klokke, "%H:%M")
       
        if time_tider["forste_time"]["start"] <= klokkeslett <= time_tider["forste_time"]["slutt"]:
            print(f"{elev_navn} er i klasserom: {klasserom_oversikt[elev.fag1]}")
            
        elif time_tider["andre_time"]["start"] <= klokkeslett <= time_tider["andre_time"]["slutt"]:
            print(f"{elev_navn} i klasserom: {klasserom_oversikt[elev.fag2]}")
            
        elif time_tider["tredje_time"]["start"] <= klokkeslett <= time_tider["tredje_time"]["slutt"]:
            print(f"{elev_navn} er i klasserom: {klasserom_oversikt[elev.fag3]}")
            
        elif time_tider["fjerde_time"]["start"] <= klokkeslett <= time_tider["fjerde_time"]["slutt"]:
            print(f"{elev_navn} er i klasserom: {klasserom_oversikt[elev.fag3]}")
            
        else:
            print("Elev har enten friminutt eller er ferdig på skolen")
    except ValueError:
        print("Ugyldig klokkeslettformat. Bruk HH:MM.")

finn_elev("Mads Hansen", "09:15")



"""
Notes
klasserom oversikt kan tilpasses slik at flere rom brukes til flere fag på forskjellige tidspunkt. 
ta hensyn til at klasser har norsk i forskjellige klasserom

Strukturere koden bedre fikse rekkefølge ev. og kommentarer
Justere koden slik at den kan ta inn elever fra forskjellige trinn, merk endring i fag og klasser som fordeles på
Printe timeplan som tabell, vurdere vise ring eller markere hvor eleven er nå
Vurdere ta vekk mail funksjonen på kontakt, vil vel ikke funke på andre operativ
Vurdere om alle kommentarer skal stå, eller om man da leder til spørsmål om det som en kan svare på



time_tider = {
    "forste_time": { 
        "start": datetime.strptime("08:30", "%H:%M"),
        "slutt": datetime.strptime("10:00", "%H:%M")
    },
    "andre_time": {
        "start": datetime.strptime("10:15", "%H:%M"),
        "slutt": datetime.strptime("11:45", "%H:%M")
    },
    "tredje_time": {
        "start": datetime.strptime("12:15", "%H:%M"),
        "slutt": datetime.strptime("13:45", "%H:%M")
    },
    "fjerde_time": {
        "start": datetime.strptime("14:00", "%H:%M"),
        "slutt": datetime.strptime("15:30", "%H:%M")
    }
}
timeplan = {
    "mandag": 
    "tirsdag": 
    "onsdag": 
    "torsdag": 
    "fredag": 
}

# Oversikt over hvilke fag som går samtidig der a-b-c er programfag og d er fellesfag
time_bolker = {
    "bolk_a": ["R2", "S2"],
    "bolk_b": ["IT2", "Markedsføring og ledelse 2", "Fysikk 2", "Økonomistyring"],
    "bolk_c": ["Engelsk 2", "Filosofi", "Breddeidrett 2", "Psykologi"],
    "bolk_d": ["Norsk", "Historie", "Religion"]
}

"""