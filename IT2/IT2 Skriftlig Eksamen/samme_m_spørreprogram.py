import csv

def convert_and_sort(value):
    try:
        float_value = float(value)
        return True, float_value
    except ValueError:
        return False, value

def sort_dict_by_value(dictionary, sort_column_name):
    sort_key_index = kolonne_overskrifter.index(sort_column_name)
    return dict(sorted(dictionary.items(), key=lambda item: convert_and_sort(item[1][sort_key_index])))

youtube_info_dict = {}

with open('Global YouTube Statistics-kopi.csv', newline='', encoding='utf-8') as csvfil:
    youtubeleser = csv.reader(csvfil, delimiter=",")
    kolonne_overskrifter = next(youtubeleser)  # Hopper over overskriften hvis den finnes i CSV-filen
    for i, rad in enumerate(youtubeleser):
        youtube_info_dict[f"{rad[1]}"] = rad

# Det samme som spørreprogram
print(f"Mulige kategorier er: {', '.join(kolonne_overskrifter[:10])}")
kolonne = str(input("Hvilken kategori vil du sortere etter?"))  # Sjekke om riktig skrevet, noen er lower andre er ikke

# Sorter ordboken etter en bestemt verdi (for eksempel kolonne "subscribers")
sorted_dict = sort_dict_by_value(youtube_info_dict, kolonne)

intervallet = eval(input("Oppgi intervallet du vil bruke? (Format: (a, b))"))
utvalgt_intervall = list(sorted_dict.items())[intervallet[0]:intervallet[1]]

stigende_eller_synkende = str(input("Vil du ha i stigende eller synkende rekkefølge?"))
if stigende_eller_synkende.casefold() == "stigende":
    for key, value in utvalgt_intervall:
        kolonne_indeks = kolonne_overskrifter.index(kolonne)
        print(f"{key} - {kolonne}: {value[kolonne_indeks]}")
        
elif stigende_eller_synkende.casefold() == "synkende":
     utvalgt_intervall.reverse()
     for key, value in utvalgt_intervall:
        kolonne_indeks = kolonne_overskrifter.index(kolonne)
        print(f"{key} - {kolonne}: {value[kolonne_indeks]}")
