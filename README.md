# Proje
import pygame
from pygame.draw import *

pygame.init()
sc = pygame.display.set_mode((800, 800))


# block color
brown = (139,115,85)
bisque1 = (255,228,196)
white = (240,248,255)
blue = (0,0,255)
black = (0, 0, 0)
red = (255, 0, 0)
yellow = (255, 255, 0)
gray = (200, 200, 200)
sc.fill(black)
flruning = True



# kafa ağız göz koordinatları

circle_center_koordinate_head_smile = (300 , 300)
circle_center_koordinate_right_eye_smile = (400, 230)
circle_center_koordinate_left_eye_smile = (200, 230)

# kafa çizimi

circle(sc,bisque1 , circle_center_koordinate_head_smile, 200)
circle(sc, black, circle_center_koordinate_head_smile, 200,1)

# sağ göz çizimi

circle(sc, white, circle_center_koordinate_right_eye_smile, 40)
circle(sc, black, circle_center_koordinate_right_eye_smile, 40, 1)
circle(sc, blue, circle_center_koordinate_right_eye_smile, 20)

# sol göz çizimi

circle(sc, white, circle_center_koordinate_left_eye_smile, 40)
circle(sc, black, circle_center_koordinate_left_eye_smile, 40, 1)
circle(sc, blue, circle_center_koordinate_left_eye_smile, 20)

#ağız çizimi

rect(sc,red, (200, 400, 200, 15))

# sağ kaş çizimi

polygon(sc, brown, [(340, 230), (340-10, 230-12), (480-10, 150-12), (480, 150)])  

# sol kaş çizimi

polygon(sc, brown, [(250, 220), (264, 208), (115+14-10, 115-12-10), (115-10, 115-10)])



pygame.display.update()
while flruning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            flruning = False
