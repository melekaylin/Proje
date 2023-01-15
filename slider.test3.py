import pygame
import sys


pygame.init()


#RENKLER
siyah = (0,0,0)
beyaz =(255,255,255)
red = (255,0,0)
turuncu = (255,165,0)
sari = (255,255,0)
yeşil = (50,205,50)
mavi = (0,0,255)
mor = (160,32,240)
gray =(176,176,176)


w , h = 1000 , 700
screen = pygame.display.set_mode((w, h))
screen.fill(mor)
w = screen.get_width()
h = screen.get_height()

bar_x = 10 
bar_y = 200
x_scroll1 = 10 
x_scroll2 = 10 
x_scroll3 = 10 
running = True

def button1 ( x , y , width , height , active_colour , action =None):
    global pen_colour , pensize , x_scroll1 , x_scroll2 , x_scroll3
    cur = pygame.mouse.get_pos()
    click= pygame.mouse.get_pressed()
    if x + width > cur[0] > x and y + height+ 12 > cur[1] > y-12:
        pygame.draw.rect (screen , active_colour , ( x , y , width, height ))
        if click [0] == 1 and action != None :
            if action == "scroll1":
                x_scroll1 = cur [0]
            elif action == "scroll2":
                x_scroll2 = cur [0]
            elif action == "scroll3":
                x_scroll3 = cur [0]
    else:
        pygame.draw.rect(screen, active_colour, (x, y , width , height))



while running :
    pos = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runnig = False
    
    screen.fill(mor)
    button1(bar_x, bar_y, 75 , 2 , gray , action = "scroll1" )
    button1(bar_x, bar_y+30  , 75 , 2 , gray , action = "scroll2" )
    button1(bar_x, bar_y+30 *2 , 75 , 2 , gray , action = "scroll3" )

    pygame.draw.rect(screen , gray , [x_scroll1 - 5 , bar_y - 12 , 10 ,24 ] )
    pygame.draw.rect(screen , gray , [x_scroll2 - 5 , bar_y + 30 - 12 , 10 ,24 ] )
    pygame.draw.rect(screen , gray , [x_scroll3 - 5 , bar_y + 30 *2 - 12 , 10 ,24 ] )

    red_scroll = (255/75)  * (x_scroll1 - 10)
    green_scroll = (255/75)  * (x_scroll2 - 10)
    blue_scroll = (255/75)  * (x_scroll3 - 10)

    colour = [red_scroll,green_scroll,blue_scroll]


    pygame.draw.ellipse(screen ,  colour, [50,100,200,90])





    pygame.display.flip()
