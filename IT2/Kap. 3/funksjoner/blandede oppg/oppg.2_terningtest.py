from random import randint
import matplotlib.pyplot as plt

xverdier = [1, 2, 3, 4, 5, 6]
hundrekast = []

for i in range(100):
    hundrekast.append(randint(1, 6))

yverdier = [hundrekast.count(1), hundrekast.count(2), hundrekast.count(3), 
            hundrekast.count(4), hundrekast.count(5), hundrekast.count(6)]

plt.bar(xverdier, yverdier)
plt.title("frekvens ved randint funk.")
plt.xlabel("mulige utfall")
plt.ylabel("antall utfall")
plt.show()
