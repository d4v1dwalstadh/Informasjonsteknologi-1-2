import csv

def convert_and_sort(value):
    try:
        float_value = float(value)
        return True, float_value
    except ValueError:
        return False, value

def sort_dict_by_value(dictionary, sort_column_name):
    sort_key_index = kolonne_overskrifter.index(sort_column_name)
    return dict(sorted(dictionary.items(), key=lambda item: (convert_and_sort(item[1][sort_key_index]))))

youtube_info_dict = {}
land_oversikt = {}
kolonne = "Country"  # Sjekke om riktig skrevet, noen er lower andre er ikke

with open('Global YouTube Statistics-kopi.csv', newline='', encoding='utf-8') as csvfil:
    youtubeleser = csv.reader(csvfil, delimiter=",")
    kolonne_overskrifter = next(youtubeleser)  # Hopper over overskriften hvis den finnes i CSV-filen
    for i, rad in enumerate(youtubeleser):
        youtube_info_dict[f"{rad[1]}"] = rad
        
        # Lage ordlister for hvert av landene
        if rad[7] not in land_oversikt:
            land_oversikt[f"{rad[7]}"] = []
        land_oversikt[f"{rad[7]}"].append(rad[:6])

# Sorter ordboken etter en bestemt verdi (for eksempel kolonne "subscribers")
sorted_dict = sort_dict_by_value(youtube_info_dict, kolonne)

# Skriv ut de 10 første resultatene
utvalgt_intervall = list(sorted_dict.items())[:10]
# utvalgt_intervall.reverse()  # når du tar -10: f.eks

# for key, value in utvalgt_intervall:
#     kolonne_indeks = kolonne_overskrifter.index(kolonne)
#     print(f"{key} - {kolonne}: {value[kolonne_indeks]}")



