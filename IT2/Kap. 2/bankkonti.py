class Bankkonto:
  kontonr = 0
  def __init__(self, saldo, eier, antallUttak = -1):
    self.saldo = saldo
    self.eier = eier
    Bankkonto.kontonr = Bankkonto.kontonr + 1
    self.kontonr = Bankkonto.kontonr
    self.antallUttak = antallUttak
    self.uttakTeller = 0
    
  
  def ta_ut(self, uttak = 1000):
    if self.antallUttak == 1:
      self.saldo = 0
    
    elif self.antallUttak == -1 or self.uttakTeller < self.antallUttak:
      if self.saldo > 0:
        self.saldo -= uttak
        self.uttakTeller += 1
      else:
        print("ingen penger å ta ut")
        
    else: 
      print("Du har nådd maks antall uttak for i år, som er: " + str(self.antallUttak))
  
  def sett_inn(self, innskud):
    self.saldo += innskud
  
  def vis_saldo(self):
    print(self.eier + " du har på konto(" + str(self.kontonr) + "): " + str(self.saldo))
    
    
class Sparekonto(Bankkonto):
  def __init__(self, saldo, eier):
    super().__init__(saldo, eier, antallUttak = 3)
  
  
class BSUKonto(Bankkonto):
  def __init__(self, saldo, eier):
    super().__init__(saldo, eier, antallUttak = 1)
    





person1 = Bankkonto(1000, "David")
person1.ta_ut(500)
person1.sett_inn(1000)
person1.vis_saldo()

person2 = Sparekonto(400, "Hans")
person2.ta_ut(10)
person2.ta_ut(10)
person2.ta_ut(10)
person2.ta_ut(10)
person2.vis_saldo()

person3 = BSUKonto(2000, "Pål")
person3.sett_inn(500)
person3.ta_ut()
person3.vis_saldo()




  