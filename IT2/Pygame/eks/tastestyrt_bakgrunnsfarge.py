import pygame as pg
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT)

# Initialiserer/starter pygame
pg.init()

# Oppretter et vindu der vi skal "tegne" innholdet vårt
VINDU_BREDDE = 500
VINDU_HOYDE  = 500
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])

# Gjenta helt til brukeren lukker vinduet
fortsett = True
while fortsett:

    # Sjekker om brukeren har lukket vinduet
    for event in pg.event.get():
      if event.type == pg.QUIT:
        fortsett = False

    # Henter en liste med status for alle tastatur-taster
    trykkede_taster = pg.key.get_pressed()

    # Farger bakgrunnen
    if trykkede_taster[K_UP]:
      vindu.fill((0, 255, 255))
    if trykkede_taster[K_DOWN]:
      vindu.fill((255, 255, 0))
    if trykkede_taster[K_LEFT]:
      vindu.fill((255, 0, 255))
    if trykkede_taster[K_RIGHT]:
      vindu.fill((0, 0, 255))

    # Oppdaterer alt innholdet i vinduet
    pg.display.flip()

# Avslutter pygame
pg.quit()