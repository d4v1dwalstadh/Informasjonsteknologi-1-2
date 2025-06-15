import csv

youtube_info_dict = {}

land_oversikt = {}


with open('Global YouTube Statistics.csv', newline='', encoding='utf-8') as csvfil:
    youtubeleser = csv.reader(csvfil, delimiter=",")
    kolonne_overskrifter = next(youtubeleser)  # Hopper over overskriften hvis den finnes i CSV-filen
    for i, rad in enumerate(youtubeleser):
        youtube_info_dict[f"{rad[1]}"] = rad
        
        # Lage ordlister for hvert av landene
        if rad[7] not in land_oversikt:
            land_oversikt[f"{rad[7]}"] = []
        land_oversikt[f"{rad[7]}"].append(rad[:6])
 
 
 # Antall kanaler per land
kanal_per_land = {}

for key in land_oversikt:
    flest_kanaler = 0
    if len(land_oversikt[f"{key}"]) > flest_kanaler:
        flest_kanaler = len(land_oversikt[f"{key}"])
        kanal_per_land[f"{key}"] = flest_kanaler
        



views_per_land = {}

for key in land_oversikt:
    tot_views = 0
    for i in range(kanal_per_land[f"{key}"]):
        tot_views += float(land_oversikt[f"{key}"][i][3])
    views_per_land[f"{key}"] = tot_views
    
    
abonnenter_per_land = {}

for key in land_oversikt:
    tot_abonnenter = 0
    for i in range(kanal_per_land[f"{key}"]):
        tot_abonnenter += float(land_oversikt[f"{key}"][i][2])
    abonnenter_per_land[f"{key}"] = tot_abonnenter

    
# Sorterer ordboken etter verdier fra høyest til lavest, printer top 10
verdi_sortert = dict(sorted(kanal_per_land.items(), key=lambda item: item[1], reverse=True))
utvalgt_intervall = list(verdi_sortert.items())[:10]
ordliste_igjen = dict(utvalgt_intervall)

for i, key in enumerate(ordliste_igjen.keys()):
    kanaler = kanal_per_land[f"{key}"]
    avg_views = round(views_per_land[f"{key}"] / kanaler, 0)
    avg_abonnenter = round(abonnenter_per_land[f"{key}"] / kanaler, 2)
    print(f"{i+1}. {key}, tot. kanaler: {kanaler}, gjennomsnittlige abonnenter: {avg_abonnenter},  gjennomsnittlige views: {avg_views}")








 





