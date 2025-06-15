import math as m

pi = m.pi

def gi_overflateareal(type, radius=0, høyde=0, sidelengde=0):
    if type.lower() == "kule":
        a_kule = 4 * pi * radius**2
        print(a_kule)

    if type.lower() == "sylinder":
        a_sylinder = (2 * pi * radius**2) + (2 * pi * radius * høyde)
        return a_sylinder

    if type.lower() == "kjegle":
        a_kjegle = (pi * radius**2) + (pi * radius * sidelengde)
        print(a_kjegle)


print(gi_overflateareal("sylinder", 2, 1, 1))
gi_overflateareal("kule", 3, 0)

