import datetime as dt

class Person:
    """Klasse som tar inn navn og fødselår i string og printer setning"""
    def __init__(self, fornavn, etternavn, fødselår):
        self.fornavn = fornavn
        self.etternavn = etternavn
        self.fødselsår = fødselår
        
    def beregn_Alder(self):
        """Beregner alder i nøyaktig tid, gir det alder du fyller det året"""
        self.tidsforskjell = (dt.datetime.now()) - (dt.datetime(self.fødselsår, 1, 1))
        return self.tidsforskjell.days // 365
        
        
    def vis_Info(self):
        """Viser info og printer svarsetning med navn og alder"""
        print(f"Ditt navn er {self.fornavn} {self.etternavn} og", end=' ')
        print(f"du er født i {self.fødselsår} og er eller fyller {self.beregn_Alder()}")

person1 = Person("David", "Walstad", 2005)
person1.vis_Info()

person2 = Person("Hans", "Karlsson", 1967)
person2.vis_Info()

person3 = Person("Mads", "Hansen", 1992)
person3.vis_Info()

