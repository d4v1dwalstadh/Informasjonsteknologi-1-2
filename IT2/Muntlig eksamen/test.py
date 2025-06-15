import csv

class Elev:
    def __init__(self, navn, email, fag1, fag2, fag3):
        self.navn = navn
        self.email = email
        self.fag1 = fag1
        self.fag2 = fag2
        self.fag3 = fag3

# Opprett en tom liste for å lagre Elev-objekter
elever = []

# Les inn CSV-filen
with open('elev_info.csv', newline='') as csvfile:
    elevleser = csv.reader(csvfile)
    next(elevleser)  # Hopper over overskriften hvis den finnes i CSV-filen
    for rad in elevleser:
        navn, email, fag1, fag2, fag3 = rad
        elev = Elev(navn, email, fag1, fag2, fag3)
        elever.append(elev)

# Eksempel: Skriv ut klasselister
klasseliste = {}
for elev in elever:
    klasse = elev.email.split('@')[0].split('.')[-1].upper()
    if klasse not in klasseliste:
        klasseliste[klasse] = []
    klasseliste[klasse].append(elev.navn)

for klasse, elever_i_klasse in klasseliste.items():
    print(f'Klasse {klasse}: {", ".join(elever_i_klasse)}')

# Eksempel: Finn klasserom for en bestemt elev
sok_navn = 'Mads Hansen'
for elev in elever:
    if elev.navn == sok_navn:
        klasse = elev.email.split('@')[0].split('.')[-1].upper()
        print(f'{sok_navn} er i klasse {klasse}')

# Eksempel: Kontakt en elev
sok_navn = 'Ingrid Olsen'
for elev in elever:
    if elev.navn == sok_navn:
        print(f'Kontakt {sok_navn} via e-post: {elev.email}')
