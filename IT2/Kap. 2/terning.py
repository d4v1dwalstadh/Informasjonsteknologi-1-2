from random import randint

class Terning:
    def __init__(self, antallSider):
        """Klasse som skal trille en terning med et visst antall sider"""
        self.antallSider = antallSider
    
    def trill_Terning(self):
        return randint(1, self.antallSider)


def mange_kast(antall_kast, antall_sider):
    """Kaster terning x antall ganger ved Terning klassen"""
    for i in range(antall_kast):
        print(Terning(antall_sider).trill_Terning())
    
    
mange_kast(20, 6)
