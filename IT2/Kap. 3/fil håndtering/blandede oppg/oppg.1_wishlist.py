filnavn = "wish_list.txt"

bruker_input = ""

with open(filnavn, "a", encoding="utf-8") as fil:
    while bruker_input != "stopp":
        bruker_input = input("Legg til ønske: ")
        
        if bruker_input != "stopp": 
            fil.write('\n' + bruker_input )  #lager og legger til i egen ny fil


with open(filnavn, encoding="utf-8") as fil2: 
    print("Oppdatert ønskeliste:")
    print(fil2.read())

#funker