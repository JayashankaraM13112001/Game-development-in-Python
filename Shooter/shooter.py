import sys
import pygame

pygame.init()
screen=pygame.display.set_mode((600, 600))
pygame.display.set_caption("Shooter")

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x>vel:
        x-=vel
    if keys[pygame.K_RIGHT] and x<600-vel-width:
        x+=vel

    screen.fill((0,0,0))
    font=pygame.font.Font(None,32)

    pygame.display.update()
    pygame.time.delay(20)