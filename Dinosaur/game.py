import sys
import pygame as pg
import random
import pygame.locals

pg.init()
screen=pg.display.set_mode((900,500))
pg.display.set_caption("Dinosaur Game")
font=pg.font.Font(None,32)

run=True
while run:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            run=False
            sys.exit()

    screen.fill((0,0,0))
    pg.display.update()

pg.quit()