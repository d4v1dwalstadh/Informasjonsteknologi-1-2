from random import randint
from math import sqrt

class Mangekant:
  def __init__(self, antallSider):
    self.antallSider = antallSider
    self.lengder = []
    
  def gi_sider(self):
    for i in range(self.antallSider):
      self.lengder.append(int(input("Lengde på sidene (en om gangen)")))
    
  def regn_omkrets(self):
    return sum(self.lengder)
  
  def vis_info(self):
    print("Mangekanten har " + str(self.antallSider) + " sider, med sidelengder på " + str(self.lengder))
    print("og dermed en omkrets på " + str(self.regn_omkrets()))


class Rektangel(Mangekant):
  def __init__(self):
    super().__init__(4)
  
  def gi_sider(self):
    self.lengder.append(int(input("Lengde på den første siden: ")))
    self.lengder.append(int(input("Lengde på den andre siden: ")))
    self.lengder *= 2 ## for å få verdi for resterende sider
  
  def regn_areal(self):
    return self.lengder[0] * self.lengder[1]
  
  def vis_info(self):
    print("Mangekanten har " + str(self.antallSider) + " sider, med sidelengder på " + str(self.lengder))
    print("og dermed en omkrets på " + str(self.regn_omkrets()) + " og areal på " + str(self.regn_areal()))


class Kvadrat(Rektangel):
  def __init__(self):
    super().__init__()
  
  def gi_sider(self):
    self.lengder.append(int(input("Lengde på siden: ")))
    self.lengder *= 4


class Trekant(Mangekant):
  def __init__(self):
    super().__init__(3)
    
  def regn_areal(self):
    s = self.regn_omkrets() / 2
    a = self.lengder[0]
    b = self.lengder[1]
    c = self.lengder[2]
    return round(sqrt(s * (s - a) * (s - b) * (s - c)), 2)
  
  def vis_info(self):
    print("Sidelengder: " + str(self.lengder))
    print("Omkrets: " + str(self.regn_omkrets()))
    print("Areal: " + str(self.regn_areal()))
    





trekant1 = Trekant()
trekant1.gi_sider()
trekant1.vis_info()



"""
mangekant_liste = []

#lager en liste med fire figurer, med tilfeldig antall sider
for i in range(4):
    print("figur nr: " + str(i + 1))
    mangekant = Mangekant(randint(3, 5))
    mangekant.gi_sider()
    mangekant_liste.append(mangekant)

# Du kan nå aksessere objektene i mangekant_liste som ønsket.
for mangekant in mangekant_liste:
    mangekant.vis_info()
"""

"""
firkant_liste = []

for i in range(4):
  print("rektangel nr: "+ str(i + 1))
  rektangel = Rektangel()
  rektangel.gi_sider()
  firkant_liste.append(rektangel)
  print("kvadrat nr: "+ str(i + 1))
  kvadrat = Kvadrat()
  kvadrat.gi_sider()
  firkant_liste.append(kvadrat)
  
for firkant in firkant_liste:
  firkant.vis_info()
""" 


