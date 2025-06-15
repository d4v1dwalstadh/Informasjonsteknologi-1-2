import pygame as pg


# Initialiserer/starter pygame
pg.init()

# Oppretter et vindu der vi skal "tegne" innholdet vårt
VINDU_BREDDE = 500
VINDU_HOYDE = 500
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])

class Ball:
    """Klasse for å representere en ball"""
    def __init__(self, x, y, xFart, yFart, radius, vindusobjekt, farge):
        """Konstruktør"""
        self.x = x
        self.y = y
        self.xFart = xFart
        self.yFart = yFart
        self.radius = radius
        self.vindusobjekt = vindusobjekt
        self.farge = farge

    def tegn(self):
        """Metode for å tegne ballen"""
        pg.draw.circle(self.vindusobjekt, self.farge, (self.x, self.y), self.radius)

    def flytt(self):
        """Metode for å flytte ballen"""
        # Sjekker om ballen er utenfor høyre/venstre kant
        if ((self.x - self.radius) <= 0) or ((self.x + self.radius) >= self.vindusobjekt.get_width()):
            self.xFart = -self.xFart
        elif ((self.y - self.radius) <= 0) or ((self.y + self.radius) >= self.vindusobjekt.get_height()):
            self.yFart = -self.yFart

        # Flytter ballen
        self.x += self.xFart
        self.y += self.yFart


# Lager et Ball-objekt
ball = Ball(250, 250, 0.1, 0.2, 40, vindu, (0, 255, 0))
ball2 = Ball(100, 100, 0.2, 0.1, 40, vindu, (0, 0, 255))

# Gjenta helt til brukeren lukker vinduet
fortsett = True
while fortsett:

    # Sjekker om brukeren har lukket vinduet
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False

    # Farger bakgrunnen lyseblå
    vindu.fill((135, 206, 235))

    # Tegner ballene før flytting
    ball.tegn()
    ball2.tegn()

    # Flytter ballene
    ball.flytt()
    ball2.flytt()

    # Oppdaterer alt innholdet i vinduet
    pg.display.flip()

# Avslutter pygame
pg.quit()
