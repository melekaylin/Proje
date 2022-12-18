import pygame
img = pygame.image.load('projeiçinfoto.png')
#EKRAN BOYUTU AYARLAMASI
w = 1000
h = 700

screen = pygame.display.set_mode((w, h)) #EKRAN TANIMI
gray = (176,176,176) #ARKA PLAN RENGİ 

rect = img.get_rect() 
rect.center = w//4, h//2 #GÖRÜNTÜNÜN EKRANDA KONUMU

screen.fill(gray)
screen.blit(img, rect)

#EKRANA YANSITMAK İÇİN SON İŞLEMLER
pygame.display.update()
while Warning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            Warning = False

