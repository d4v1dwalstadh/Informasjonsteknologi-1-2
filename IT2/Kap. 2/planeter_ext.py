from random import pi

class Planet:
  def __init__(self, navn, solavstand, radius, antallRinger = 0):
    self.navn = navn
    self.solavstand = solavstand
    self.radius = radius
    self.antallRinger = antallRinger
    self.maaner = []
  
  
  def leggTilMaane(self, maaneobjekt):
    self.maaner.append(maaneobjekt)
  
  def visInfoMaane(self):
    if len(self.maaner) > 0:
      print(self.navn + " sine måner")
      for maane in self.maaner:
        print(maane.navn + " forholdtall: " + str(maane.radius / self.radius))
    else: 
      print(self.navn + " har ingen måner")
    
  def visInfo(self):
    print("Planeten " + self.navn + " har " + str(self.antallRinger) + " ringer, er ", end="")
    print(str(self.solavstand) + " millioner km unna sola og har radius " + str(self.radius) + " km.")


class Maane:
  def __init__(self, navn, radius):
    self.navn = navn
    self.radius = radius
  
  def gi_volum(self):
    return 4/3 * pi * (self.radius**3)
  
  


planeter = {}
planeter["Mars"] = Planet("Mars", 227.9, 3389.5, 2)
planeter["Mars"].leggTilMaane(Maane("Phobos", 11.267))
planeter["Mars"].leggTilMaane(Maane("Deimos", 6.2))

planeter["Jorda"] = Planet("Jorda", 300, 4000, 0)


planeter[""].visInfoMaane()