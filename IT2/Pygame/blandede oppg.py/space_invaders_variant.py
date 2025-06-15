import pygame as pg
from pygame.locals import (K_LEFT, K_RIGHT, K_SPACE, KEYUP)
import math as m

pg.init()

(bredde, hoyde) = (500, 600)
vindu = pg.display.set_mode([bredde, hoyde])

font = pg.font.SysFont("Calibri", 18)


class Spiller:
    def __init__(self):
        self.vindusobjekt = vindu
        self.farge = (57, 255, 20)
        (self.x, self.y) = (250, 550)
        self.radius = 30
        self.xFart = 0.14
        self.kan_skyte = True  # Variabel for å kontrollere om spilleren kan skyte
        self.prosjektiler = []  # Liste for å lagre prosjektiler

    def tegn(self):
        """Metode for å tegne ballen"""
        pg.draw.circle(self.vindusobjekt, self.farge, (self.x, self.y), self.radius)

    def flytt(self, taster):
        if taster[K_LEFT] and (self.x - self.radius) > 0:
            self.x -= self.xFart
        if taster[K_RIGHT] and (self.x + self.radius) < self.vindusobjekt.get_width():
            self.x += self.xFart

    def skyt(self, taster):
        if taster[K_SPACE] and self.kan_skyte:
            prosjektil_x = self.x
            prosjektil_y = self.y - self.radius
            self.prosjektiler.append((prosjektil_x, prosjektil_y))
            self.kan_skyte = False  # Blokkerer ytterligere skyting

    def oppdater_prosjektiler(self): 
        for i in range(len(self.prosjektiler)):
            x, y = self.prosjektiler[i]
            pg.draw.circle(self.vindusobjekt, (255, 60, 0), (x, y), 5)
            self.prosjektiler[i] = (x, y - 1)  # Oppdaterer posisjonen
    
    
# Gjøre alleHindringer elementer til objekter fra en egen klasse så jeg kan kopiere finn avstand funksjonen               
        

class Hindringer:
    def __init__(self):
        self.vindusobjekt = vindu
        self.farge = (255, 255, 255)
        self.radius = 30
        self.yFart = 0.02
        self.antallTruffet = 0
        self.y = 10
        self.alleHindringer = []
        

    def spawn(self):
        antall = 5
        avstand = self.vindusobjekt.get_width() / antall
        for i in range(5):
            hindring_y = i * 150
            for j in range(antall):
                if i % 2 == 0:
                    hindring_x = j * avstand + self.radius
                    pg.draw.circle(self.vindusobjekt, self.farge, (hindring_x, (self.y - hindring_y)), self.radius)
                    self.alleHindringer.append([hindring_x, hindring_y])
                else:
                    hindring_x = j * avstand + (self.radius * 2)
                    pg.draw.circle(self.vindusobjekt, self.farge, (hindring_x, (self.y - hindring_y)), self.radius)
                    self.alleHindringer.append([hindring_x, hindring_y])
    
    def beveg(self):
        self.y += self.yFart
    
   


spiller1 = Spiller()
hindringer1 = Hindringer()

fortsett = True
while fortsett:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False
        elif event.type == KEYUP:
            if event.key == K_SPACE:
                spiller1.skyt(pg.key.get_pressed())
                spiller1.kan_skyte = True  # Tillater ny skyting

    vindu.fill((0, 0, 0))
    dod_linje = 520
    pg.draw.line(vindu, (255, 0, 0), (0, dod_linje), (bredde, dod_linje), 3)

    trykkede_taster = pg.key.get_pressed()

    spiller1.tegn()
    spiller1.flytt(trykkede_taster)  # Lar spiller flytte skipet
    spiller1.skyt(trykkede_taster)  
    spiller1.oppdater_prosjektiler() 
    
      


    hindringer1.spawn()
    hindringer1.beveg()

    if hindringer1.y >= dod_linje - hindringer1.radius:
        spiller1.xFart = 0
        hindringer1.yFart = 0
        avslutt_tekst = font.render("Game over!", True, (255, 255, 255))
        vindu.blit(avslutt_tekst, (215, 230))

    pg.display.flip()

pg.quit()
