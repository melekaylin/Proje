import pygame, sys

pygame.init()

pencere = pygame.display.set_mode((300,300))

mavi = (0,0,255)

while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()

    pygame.draw.ellipse(pencere, mavi, (50,50,80,120), 1)

    pygame.display.flip()