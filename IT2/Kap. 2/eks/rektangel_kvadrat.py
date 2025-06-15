class Rektangel:
  """Klasse for å representere rektangel"""
  def __init__(self, lengde: int, bredde: int):
    self.lengde = lengde
    self.bredde = bredde
  
  def areal(self):
    """Metode for utregning av areal"""
    return self.lengde * self.bredde
   
  def visInfo(self):
    """Skriver ut info om rektangel"""
    print(f"Rektangel med lengde {self.lengde} og", end=" ")
    print(f"bredde {self.bredde} gir areal {self.areal()}")
  
class Kvadrat(Rektangel):
  """Klasse for å representere kvadrat"""
  def __init__(self, sidekant: int):
    super().__init__(sidekant, sidekant)
  
  def visInfo(self):
    print(f"Kvadrat med sidekant {self.sidekant} gir areal {self.areal()}")
    
  
rektangler = []

rektangler.append(Rektangel(2, 5))
rektangler.append(Rektangel(4, 3))
rektangler.append(Rektangel(5, 6)) 

for r in rektangler:
  r.visInfo()
    