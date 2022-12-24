import pygame
import sys

pygame.init()

pencere = pygame.display.set_mode((1000,700), pygame.SWSURFACE)
pygame.display.set_caption("Işık Ve Renkler")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()
