class Medlem:
    medlemsnummer = 0
    
    def __init__(self, fornavn, etternavn):
        self.fornavn = fornavn
        self.etternavn = etternavn
        Medlem.medlemsnummer = Medlem.medlemsnummer + 1
        self.medlemsnummer = Medlem.medlemsnummer
    
        
per = Medlem("Per", "Lund")
kim = Medlem("Kim", "Svendsen")
kelly = Medlem("Kelly", "Brixton")

print(f"{per.fornavn} har medlemsnummer {per.medlemsnummer}")
print(f"{kim.fornavn} har medlemsnummer {kim.medlemsnummer}")
print(f"{kelly.fornavn} har medlemsnummer {kelly.medlemsnummer}")