import matplotlib.pyplot as plt

karakter_liste = [5, 3, 6, 3, 5, 1, 2, 2, 2, 4, 2, 2, 5, 5, 6, 3, 5, 3, 5, 4, 2, 6, 1, 4, 2, 3, 3, 3, 5, 5]
karakterer = [1, 2, 3, 4, 5, 6]
respektive_karakterer = [karakter_liste.count(1), karakter_liste.count(2), karakter_liste.count(3), karakter_liste.count(4), karakter_liste.count(5), karakter_liste.count(6)]

plt.bar(karakterer, respektive_karakterer)
#plt.pie(respektive_karakterer, labels=karakterer)
plt.grid(axis="y")
plt.show()