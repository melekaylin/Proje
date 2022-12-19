#Tanımlamalar
import pygame 
import sys
pygame.init()
img = pygame.image.load('projeiçinfoto.png')

# Renkler
siyah = (0,0,0)
beyaz = (255,255,255)
kirmizi = (255,0,0)
yesil = (0,255,0)
mavi = (0,0,255)
gray = (176,176,176)

#Ekran ve kadının konumlandırılması
w , h = 1000 , 700
screen = pygame.display.set_mode((w, h))
screen.fill(gray)
rect = img.get_rect()
rect.center = w//5, h //2
screen.blit(img, rect)

#Exit tuşunun konumlandırılması
screen_en = screen.get_width()
screen_boy = screen.get_height()
yazi_tipi = pygame.font.SysFont('lucida' , 25 )
yazi = yazi_tipi.render('EXİT', True , siyah)
yazi_1 = yazi_tipi.render('EXİT', True ,beyaz)

#Önce kadını oynatıp daha sonra exit tuşu daha içte olacak şekilde oynatıyoruz. 
pygame.display.update()
while Warning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            Warning = False

#Tuşun son işlemleri
    while True:
        for event in pygame.event.get():
            mouse = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if( screen_en //20) <= mouse[0] <= ( screen_en //20 ) + 50 and (screen_boy//23) <= mouse[1] <= (screen_boy//23) + 30 :
                    pygame.quit()
        pygame.draw.rect( screen, beyaz ,[int(screen_en//20), int(screen_boy//23) ,50,30] )
        screen.blit(yazi,[(screen_en//20) + 5, (screen_boy//23) + 3])
        mouse = pygame.mouse.get_pos()
        if   ( screen_en //20) <= mouse[0] <= ( screen_en //20 ) + 50 and (screen_boy//23) <= mouse[1] <= (screen_boy//23) + 30 :
            pygame.draw.rect( screen,kirmizi ,[ int(screen_en//20), int(screen_boy//23) ,50,30] )
            screen.blit(yazi_1,[(screen_en/20) + 5, (screen_boy/23) + 3])
        pygame.display.flip()

