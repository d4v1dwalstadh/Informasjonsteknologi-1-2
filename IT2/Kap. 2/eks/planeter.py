class Planet:
  def __init__(self, navn, solavstand, radius, antallRinger = 0):
    self.navn = navn
    self.solavstand = solavstand
    self.radius = radius
    self.antallRinger = antallRinger
  
  def visInfo(self):
    print(f"Planeten {self.navn} har {self.antallRinger} ringer,", end=" ") 
    #test her bare fordi linjen blir for lang
    print(f"er {self.solavstand} mil. km unna sola og har radius {self.radius} km.")
    
planeter = {}

# Lager og legger til noen Planet-objekter
planeter["Mars"] = Planet("Mars", 227.9, 3389.5)
planeter["Jupiter"] = Planet("Jupiter", 778.5, 69911, 4)
planeter["Saturn"] = Planet("Saturn", 1434000, 58232, 7)

for p in planeter.values():
    p.visInfo()