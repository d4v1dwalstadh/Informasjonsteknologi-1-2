class Billett():
    """Klasse for å regne ut endelig billettpris"""
    def __init__(self):
        self.mva = 0.12
        self.pris = 20
    
    def beregnPris(self):
        return self.pris + (self.pris * self.mva)

class BarneBillett(Billett):
    "Klasse for barnebillettpris"
    def __init__(self):
        super().__init__()
        self.rabatt = 0.5
    
    def beregnPris(self):
        return super().beregnPris() * self.rabatt
        
    
billett1 = BarneBillett()

print(billett1.beregnPris())
    