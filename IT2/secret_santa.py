import random

fornavn_liste = [
    "Anders", "Axel", "Cornelius", "David", "Djulian",
    "Elliot", "Elmer", "Henrik", "Eskil", "Lars",
    "Leon", "Fredrik", "Henrich", "Bjørgo", "Eriksson",
    "Jens", "Leon", "Bubresko", "Wiksaas", "Marius",
    "Ferner", "Habert", "Noah", "Said", "Cavanzo",
    "Hellestad", "Siggurd", "Theodor", "Troy"
]

giver_liste = []
mottaker_liste = []

gutta_random = fornavn_liste.copy()  # Kopier listen for å holde styr på tildelte gaver
random.shuffle(gutta_random)  # Blander listen for å tildele tilfeldige gaver

for i, giver in enumerate(gutta_random):
    if i + 1 == len(fornavn_liste):
        print(f"{giver} gir gave til {gutta_random[0]}")
    else:
        print(f"{giver} gir gave til {gutta_random[i + 1]}")



