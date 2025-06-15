a = [8, 5, 2, 6, 12]

def byttPlass(liste, posisjon):
    """Funk. som bytter plass på tall i angitt posisjon i liste og bytter med neste tall i listen"""
    neste_tall_kopi = liste[posisjon + 1]
    liste[posisjon + 1] = liste[posisjon]
    liste[posisjon] = neste_tall_kopi

for j in range(len(a)):
    for i in range(len(a) - 1):
        if a[i] > a[i +1]:
            byttPlass(a, i)
print(a)

