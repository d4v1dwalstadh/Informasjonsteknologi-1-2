import pygame as pg
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT)
import math as m

# Initialiserer/starter pygame
pg.init()

# Oppretter et vindu der vi skal "tegne" innholdet vårt
VINDU_BREDDE = 500
VINDU_HOYDE  = 500
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])

class Ball:
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
  
  def finnAvstand(self, annenBall):
    """Metode for å finne avstanden til en annen ball"""
    xAvstand2 = (self.x - annenBall.x)**2  # x-avstand i andre
    yAvstand2 = (self.y - annenBall.y)**2  # y-avstand i andre
    sentrumsavstand = m.sqrt(xAvstand2 + yAvstand2)
    radiuser = self.radius + annenBall.radius
    avstand = sentrumsavstand - radiuser
    return avstand

class Hinder(Ball):
  """Klasse for å representere et hinder"""
  def __init__(self, x, y, radius, farge, vindusobjekt, xFart, yFart):
    super().__init__(x, y, radius, farge, vindusobjekt)
    self.xFart = xFart
    self.yFart = yFart
    self.antallTreff = 0
    
  def flytt(self):
    """Metode for å flytte hinderet"""
    # Sjekker om hinderet er utenfor høyre/venstre kant
    if ((self.x - self.radius) <= 0) or ((self.x + self.radius) >= self.vindusobjekt.get_width()):
      self.xFart = -self.xFart
      self.antallTreff += 1
    
    # Sjekker om hinderet er utenfor øvre/nedre kant
    if ((self.y - self.radius) <= 0) or ((self.y + self.radius) >= self.vindusobjekt.get_height()):
      self.yFart = -self.yFart
      self.antallTreff += 1
      
    # Flytter hinderet
    self.x += self.xFart
    self.y += self.yFart

class Spiller(Ball):
  """Klasse for å representere en spiller"""
  def __init__(self, x, y, radius, farge, vindusobjekt, fart):
    super().__init__(x, y, radius, farge, vindusobjekt)
    self.fart = fart
    
  def flytt(self, taster):
    """Metode for å flytte spilleren"""
    if taster[K_UP]:
        if self.y - self.radius <= 0:
          self.y = vindu.get_height() - self.radius/2
        else:
          self.y -= self.fart
    if taster[K_DOWN]:
      if self.y + self.radius >= vindu.get_height():
        self.y = 0 + self.radius/2
      else:
        self.y += self.fart
    if taster[K_LEFT]:
      if self.x - self.radius <= 0:
        self.x = vindu.get_width() - self.radius/2
      else:
        self.x -= self.fart
    if taster[K_RIGHT]:
      if self.x + self.radius >= vindu.get_width():
        self.x = 0 + self.radius/2
      else:
        self.x += self.fart
      
# Lager et Spiller-objekt
spiller = Spiller(200, 200, 20, (255, 69, 0), vindu, 0.05)
# Lager et Hinder-objekt
hinder = Hinder(100, 250, 35, (0, 0, 255), vindu, 0.18, 0.08)
hinder2 = Hinder(400, 100, 35, (0, 0, 255), vindu, 0.18, 0.08)

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
    
    poengsum_tekst = font.render(f"Poeng: {hinder.antallTreff}", True, (0, 0, 0))
    vindu.blit(poengsum_tekst, (0, 0))
    
    # Tegner og flytter spiller og hinder
    spiller.tegn()
    spiller.flytt(trykkede_taster)
    hinder.tegn()
    hinder2.tegn()
    hinder.flytt()
    hinder2.flytt()
    
    # Sjekker avstanden mellom spiller og hinder
    if spiller.finnAvstand(hinder) <= 0 or spiller.finnAvstand(hinder2) <= 0:
      spiller.fart = 0
      hinder.xFart = 0
      hinder.yFart = 0
      hinder2.xFart = 0
      hinder2.yFart = 0
      avslutt_tekst = font.render("Game over!", True, (0, 0, 0))
      vindu.blit(avslutt_tekst, (215, 230))
      
    # Oppdaterer alt innholdet i vinduet
    pg.display.flip()
    
# Avslutter pygame
pg.quit()