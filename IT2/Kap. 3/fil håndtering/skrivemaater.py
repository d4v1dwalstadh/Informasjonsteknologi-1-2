import csv
import json

filnavn = "MikkelRev.txt"
with open(filnavn, encoding="utf-8") as fil:
  innhold = fil.read() #leser hele filen
print(innhold)


filnavn = "MikkelRev.txt"
with open(filnavn, encoding="utf-8") as fil:
  for linje in fil: 
    print(linje) #printer ut linje for linje, kan dermed også lese kun første


with open(filnavn, "a") as fil: #append legger til "w" write erstatter alt i
  fil.write("Hei\n") #linjeskifte
  fil.write("på\t") #tabulator, mellomrom
  fil.write("deg.")
  
  
#import csv
filnavn = "Befolkning_1951-2022.csv"
with open(filnavn, encoding="utf-8-sig") as fil:
  filinnhold = csv.reader(fil, delimiter=";") #delimeter angir hva som skiller
  overskrifter = next(filinnhold) #tar den første raden i filen
  print(overskrifter)
  for rad in filinnhold:
    print(rad)
  
  
#import json
filnavn = "skandinavia.json"
with open(filnavn, encoding="utf-8") as fil:
  data = json.load(fil) #load for json
data_formatert = json.dumps(data, indent=2) #ryddigjør dataen
print(data_formatert)