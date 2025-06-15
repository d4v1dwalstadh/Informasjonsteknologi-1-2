import pygame as pg
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT)
import math as m
from random import randint

FPS = 144
fpsClock = pg.time.Clock()

# Initialiserer/starter pygame
pg.init()

# Oppretter et vindu der vi skal "tegne" innholdet vårt
VINDU_BREDDE = 600
VINDU_HOYDE  = 600
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])

class SpillObjekt:
  """Klasse for å representere en ball"""
  def __init__(self, x, y, radius, farge, vindusobjekt):
    """Konstruktør"""
    self.x = x
    self.y = y
    self.radius = radius
    self.farge = farge
    self.vindusobjekt = vindusobjekt
  
  def tegn(self):
    """Metode for å tegne ballen"""
    pg.draw.circle(self.vindusobjekt, self.farge, (self.x, self.y), self.radius) 
    pg.draw.line(self.vindusobjekt, (255, 255, 255), (100, 0), (100, self.vindusobjekt.get_height()))
    pg.draw.line(self.vindusobjekt, (255, 255, 255), (self.vindusobjekt.get_width() - 100, 0), (self.vindusobjekt.get_width() - 100, self.vindusobjekt.get_height()))
  
  def finnAvstand(self, annenBall):
    """Metode for å finne avstanden til en annen ball"""
    xAvstand2 = (self.x - annenBall.x)**2  # x-avstand i andre
    yAvstand2 = (self.y - annenBall.y)**2  # y-avstand i andre
    sentrumsavstand = m.sqrt(xAvstand2 + yAvstand2)
    radiuser = self.radius + annenBall.radius
    avstand = sentrumsavstand - radiuser
    return avstand


class Spiller(SpillObjekt):
  """Klasse for å representere en spiller"""
  def __init__(self, x, y, radius, farge, vindusobjekt, fart):
    super().__init__(x, y, radius, farge, vindusobjekt)
    self.fart = fart
    self.bærer = False
    self.poengsum = 0
    # self.treffHindring = False
    
  def flytt(self, taster, hindringer_par):
    """Metode for å flytte spilleren"""
    for hindring in hindringer_par:
        if taster[K_UP]:
            if self.y - self.radius <= 0 or spiller.finnAvstand(hindring) - 1 <= 0:
                return
            else:
                self.y -= self.fart
        if taster[K_DOWN]:
            if self.y + self.radius >= vindu.get_height() or spiller.finnAvstand(hindring) + 1 <= 0:
                return
            else:
                self.y += self.fart
        if taster[K_LEFT]:
            if self.x - self.radius <= 0 or spiller.finnAvstand(hindring) - 1 <= 0:
                return
            else:
                self.x -= self.fart
        if taster[K_RIGHT]:
            if self.x + self.radius >= vindu.get_width() or spiller.finnAvstand(hindring) + 1 <= 0:
                return
            else:
                self.x += self.fart
    

  

class Spokelse(SpillObjekt):
    def __init__(self, x, y, radius, farge, vindusobjekt, xFart, yFart):
      super().__init__(x, y, radius, farge, vindusobjekt)
      self.xFart = xFart
      self.yFart = yFart
      
    def plassering(self):
      pg.draw.circle(self.vindusobjekt, self.farge, (self.x, self.y), self.radius) 
    
    def endreRetning(self):
        """Metode for å flytte hinderet"""
        # Sjekker om hinderet er utenfor høyre/venstre kant
        if ((self.x - self.radius) <= 100) or ((self.x + self.radius) >= self.vindusobjekt.get_width() - 100):
            self.xFart = -self.xFart
        
        # Sjekker om hinderet er utenfor øvre/nedre kant
        if ((self.y - self.radius) <= 0) or ((self.y + self.radius) >= self.vindusobjekt.get_height()):
            self.yFart = -self.yFart
     
        
        # Flytter hinderet
        self.x += self.xFart
        self.y += self.yFart

class Hindring(SpillObjekt):
    def __init__(self, x, y, radius, farge, vindusobjekt):
       super().__init__(x, y, radius, farge, vindusobjekt)
    
    def tegn(self):
        pg.draw.circle(self.vindusobjekt, self.farge, (self.x, self.y), self.radius) 
    
   
       
class Sau(SpillObjekt):
    def __init__(self, x, y, radius, farge, vindusobjekt):
       super().__init__(x, y, radius, farge, vindusobjekt)
       self.blirBåret = False
       
    def tegn(self):
        pg.draw.circle(self.vindusobjekt, self.farge, (self.x, self.y), self.radius) 

      

# Lager et Spiller-objekt
spiller = Spiller(200, 200, 20, (255, 69, 0), vindu, 0.4)




spokelser = [Spokelse(300, 300, 30, (0, 50, 50), vindu, 0.05, 0.09)]
hindringer = [Hindring(300, 300, 30, (0, 120, 50), vindu), Hindring(300, 60, 20, (0, 120, 50), vindu), Hindring(400, 300, 40, (0, 120, 50), vindu)]
sauer = [Sau(550, 200, 20, (0, 0, 0), vindu), Sau(520, 100, 20, (0, 0, 0), vindu), Sau(530, 400, 20, (0, 0, 0), vindu)]

font = pg.font.SysFont("Calibri", 15) 

# Gjenta helt til brukeren lukker vinduet
fortsett = True
while fortsett:
    # Sjekker om brukeren har lukket vinduet
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False
            
    # Henter en ordbok med status for alle tastatur-taster
    trykkede_taster = pg.key.get_pressed()
    
    # Farger bakgrunnen lyseblå
    vindu.fill((135, 206, 235))
    

    
    # Tegner og flytter spiller og spokelse
    spiller.tegn()
    spiller.flytt(trykkede_taster, hindringer)
    
    for spokelse in spokelser:
        spokelse.plassering()
        spokelse.endreRetning()

    for sau in sauer:
        sau.tegn()
        
    for hindring in hindringer:
        hindring.tegn()
    
    poengsum_tekst = font.render(f"Poeng: {spiller.poengsum}", True, (0, 0, 0))
    vindu.blit(poengsum_tekst, (10, 570))
    
   
    
       
    
    
    for sau in sauer:
        if spiller.finnAvstand(sau) <= 0 and spiller.bærer is False:
            spiller.fart = 0.1
            sau.x = spiller.x
            sau.y = spiller.y
            sau.blirBåret = True
            spiller.bærer = True
        elif sau.blirBåret is True:
            sau.x = spiller.x
            sau.y = spiller.y
        
    
    if spiller.x <= 100 and spiller.bærer is True:
        for sau in sauer:
            if sau.blirBåret is True:
                sau.x = -20
                sau.y = -20 
                sau.blirBåret = False
                spiller.bærer = False
        spiller.fart = 0.15
        spiller.poengsum += 1
        
        spokelser.append(Spokelse(300, 300, 30, (0, 50, 50), vindu, 0.05, 0.09))
        sauer.append(Sau(randint(560, 590), randint(10, 590), 20, (0, 120, 50), vindu))    
        hindringer.append(Hindring(randint(175, 425), randint(25, 575), 40, (0, 150, 150), vindu))
        

    # Sjekker avstanden mellom spiller og spokelse
    for spokelse in spokelser:
        if spiller.finnAvstand(spokelse) <= 0:
            spiller.fart = 0
            for spokelse in spokelser:
                spokelse.xFart = 0
                spokelse.yFart = 0
            avslutt_tekst = font.render("Game over!", True, (0, 0, 0))
            vindu.blit(avslutt_tekst, (215, 230))
        
    # Oppdaterer alt innholdet i vinduet
    pg.display.flip()
    
    fpsClock.tick(FPS)
    
# Avslutter pygame
pg.quit()