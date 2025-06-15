import pygame as pg

pg.init()

hoyde = 160
bredde = 240

vindu = pg.display.set_mode([bredde, hoyde])

print(type(vindu))


font = pg.font.SysFont("Calibri", 15) 

fortsett = True
while fortsett:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False
    
    vindu.fill((255, 255, 255))
    
    pg.draw.rect(vindu, (255, 0, 0), (0, 0, 60, 60))
    pg.draw.rect(vindu, (255, 0, 0), (0, 100, 60, 60))
    pg.draw.rect(vindu, (255, 0, 0), (100, 0, 140, 60))
    pg.draw.rect(vindu, (255, 0, 0), (100, 100, 140, 60))
    
    pg.draw.line(vindu, (0, 0, 153), (80, 0), (80, 160), 20)
    pg.draw.line(vindu, (0, 0, 153), (0, 80), (240, 80), 20)
    
    bilde = font.render("Norge", True, (255, 255, 255))
    vindu.blit(bilde, (0, 0))
    
    pg.display.flip()


pg.quit()



