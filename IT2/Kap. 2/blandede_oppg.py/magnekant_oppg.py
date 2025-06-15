class Mangekant:
    """Opprettelse og info om en mangekant"""
    def __init__(self, sider = 0, lengder = []):
        self.sider = sider
        self.lengder = lengder

    def registrer_sidelengder(self):
        self.sider = int(input("Skriv inn antall sider i mangekanten: "))
        self.lengder = []
        for i in range(self.sider):
            lengde = float(input(f"Skriv inn lengden til side {i+1}: "))
            self.lengder.append(lengde)
            
    def omkrets(self):
        self.omkrets_verdi = sum(self.lengder)
        return self.omkrets_verdi
        
        
    def visInfo(self):
        print(f"Du har en mangekant med sider {self.sider}")
        print(f"Du har gitt den lengdene {self.lengder}")
        print(f"Omkretsen på mangekanten din gir {self.omkrets()}")
    

class Rektangel(Mangekant):
    def __init__(self):
        super().__init__(sider = 2)
        self.lengder = [float(input("Skriv inn bredde og lengde: "))
                        for i in range(self.sider)]
    
    def areal(self):
        return self.lengder[0] * self.lengder[1]
    
    def omkrets(self):
        return (self.lengder[0] * 2) + (self.lengder[1] * 2)
    
    def __str__(self):
        return f"Figur har areal {self.areal()} og omkrets {self.omkrets()}"
    

class Kvadrat(Rektangel):
  """Klasse for å representere et kvadrat"""
  def __init__(self):
      super().__init__(sider = 1)
      
      
        
    
   


kvadrat1 = Kvadrat()
kvadrat1.areal()
print(str(kvadrat1))
"""
rektangel1 = Rektangel()
print((rektangel1))
"""



  




"""oppg. 1
mangekant1 = Mangekant()
mangekant1.registrer_sidelengder()
mangekant1.omkrets()
mangekant1.visInfo()

mangekanter = []

mangekanter.append(Mangekant(3, [1, 2, 3]))
mangekanter.append(Mangekant(4, [2, 2, 2, 2]))
mangekanter.append(Mangekant(2, [3, 2]))
mangekanter.append(Mangekant(3, [5, 2, 3]))

for m in mangekanter:
    m.visInfo()
"""