import matplotlib.pyplot as plt

filnavn = "./valgdeltagelse.txt"

aarstall = []
deltagelse = []

with open(filnavn) as fil:
    for linje in fil:
        data = linje.rstrip().split(";")
        
        aarstall.append(int(data[0]))
        deltagelse.append(float(data[1].replace(",", ".")))

plt.plot(aarstall, deltagelse)
plt.show()



    