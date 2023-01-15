# Proje
#Tanımlamalar
import pygame 
import sys
pygame.init()
img = pygame.image.load('projeiçinfoto.png') #fotoğraf yüklemek için kodumuz
img1 = pygame.image.load('ortadakielfeneri.png')
img2 = pygame.image.load('elfenerialttaki.png')
img3 = pygame.image.load('elfeneriüstteki.png')
pencere = pygame.display.set_mode((1000,700), pygame.SWSURFACE) #pygame penceresine başlık attık
pygame.display.set_caption("Işık Ve Renkler") 

#tuş sınıfı
class button(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__() 
        self.original_image = pygame.Surface((50, 50), pygame.SRCALPHA)
        pygame.draw.circle(self.original_image, color, (25, 25), 25)
        pygame.draw.circle(self.original_image, (0,0,0), (25, 25), 25, 4)
        self.click_image = pygame.Surface((50, 50), pygame.SRCALPHA)
        pygame.draw.circle(self.click_image, color, (25, 25), 25)
        pygame.draw.circle(self.click_image, (255, 255, 255), (25, 25), 25, 4)
        self.image = self.original_image 
        self.rect = self.image.get_rect(center = (x, y))
        self.clicked = False

    def update(self, event_list):
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    self.clicked = not self.clicked

        self.image = self.click_image if self.clicked else self.original_image
# Renkler
siyah = (0,0,0)
beyaz = (255,255,255)
kirmizi = (255,0,0)
yesil = (0,255,0)
mavi = (0,0,255)
gray = (176,176,176)

#Ekran ve kadının konumlandırılması
pygame.init()
w , h = 1000 , 700
screen = pygame.display.set_mode((w, h))
clock = pygame.time.Clock()
screen.fill(gray)
rect = img.get_rect()
rect.center = w//4, h //2
screen.blit(img, rect)

rect = img1.get_rect()
rect.center = w - 100, 350
screen.blit(img1, rect)

rect = img2.get_rect()
rect.center = w - 100, 550
screen.blit(img2, rect)

rect = img3.get_rect()
rect.center = w - 100, 150
screen.blit(img3, rect)




pygame.draw.ellipse(screen, beyaz, (165,80,165,70), 1) #kadının üstünde duran elips (x konumu, y konumu, x genişliği, y uzunluğu) ve çizginin kalınlığı. 
pygame.draw.ellipse(screen, beyaz, (65,150,125,50), 1) 
pygame.draw.ellipse(screen, beyaz, (15,210,100,40), 1) 

#  butonlar  için konumlandırma bloğu
sprite_object = button(*screen.get_rect().center, (128, 128, 0))
group = pygame.sprite.Group([
    button(screen.get_width() *2 // 3 +255, (screen.get_height() // 3)+120, (128, 0, 0)), #kırmızı
    button(screen.get_width() *2 // 3 +255, (screen.get_height() // 6)+10, (0, 128, 0)), #yeşil
    button(screen.get_width() *2 // 3 +255, (screen.get_height() // 2)+215, (0, 0, 128)),  #mavi

])

#Filtrelerin konumlandırılması
beyaz = (255,255,255)


pygame.draw.ellipse(pencere, beyaz, (550,100,150,500), 5)


pygame.display.flip()

#ışındeneme

kirmizi = (255,0,0)
yesil = (0,255,0)
mavi = (0,0,255)


pygame.draw.aaline(pencere,kirmizi,(852,333),(540,175))
pygame.draw.aaline(pencere,kirmizi,(852,336),(540,200))
pygame.draw.aaline(pencere,kirmizi,(852,339),(540,225))
pygame.draw.aaline(pencere,kirmizi,(852,342),(540,250))
pygame.draw.aaline(pencere,kirmizi,(852,345),(540,275))
pygame.draw.aaline(pencere,kirmizi,(852,348),(540,300))
pygame.draw.aaline(pencere,kirmizi,(852,351),(540,325))
pygame.draw.aaline(pencere,kirmizi,(852,354),(540,350))
pygame.draw.aaline(pencere,kirmizi,(852,357),(540,375))
pygame.draw.aaline(pencere,kirmizi,(852,360),(540,400))
pygame.draw.aaline(pencere,kirmizi,(852,363),(540,425))
pygame.draw.aaline(pencere,kirmizi,(852,366),(540,450))
pygame.draw.aaline(pencere,kirmizi,(852,369),(540,475))


pygame.draw.aaline(pencere,yesil,(860,160),(560,200))
pygame.draw.aaline(pencere,yesil,(862,162),(560,225))
pygame.draw.aaline(pencere,yesil,(864,164),(560,250))
pygame.draw.aaline(pencere,yesil,(866,166),(560,275))
pygame.draw.aaline(pencere,yesil,(868,168),(560,300))
pygame.draw.aaline(pencere,yesil,(870,170),(560,325))
pygame.draw.aaline(pencere,yesil,(872,172),(560,350))
pygame.draw.aaline(pencere,yesil,(874,174),(560,375))
pygame.draw.aaline(pencere,yesil,(876,176),(560,400))
pygame.draw.aaline(pencere,yesil,(878,178),(560,425))
pygame.draw.aaline(pencere,yesil,(880,180),(560,450))
pygame.draw.aaline(pencere,yesil,(882,182),(560,475))
pygame.draw.aaline(pencere,yesil,(884,184),(560,500))


pygame.draw.aaline(pencere,mavi,(889,513),(540,150))
pygame.draw.aaline(pencere,mavi,(887,515),(540,175))
pygame.draw.aaline(pencere,mavi,(885,517),(540,200))
pygame.draw.aaline(pencere,mavi,(883,519),(540,225))
pygame.draw.aaline(pencere,mavi,(881,521),(540,250))
pygame.draw.aaline(pencere,mavi,(879,523),(540,275))
pygame.draw.aaline(pencere,mavi,(877,525),(540,300))
pygame.draw.aaline(pencere,mavi,(875,527),(540,325))
pygame.draw.aaline(pencere,mavi,(873,529),(540,350))
pygame.draw.aaline(pencere,mavi,(871,531),(540,375))
pygame.draw.aaline(pencere,mavi,(869,533),(540,400))
pygame.draw.aaline(pencere,mavi,(867,535),(540,425))
pygame.draw.aaline(pencere,mavi,(865,537),(540,450))

#Exit tuşunun konumlandırılması
w = screen.get_width()
h = screen.get_height()
yazi_tipi = pygame.font.SysFont('lucida' , 25 )
yazi = yazi_tipi.render('EXİT', True , siyah)
yazi_1 = yazi_tipi.render('EXİT', True ,beyaz)




#Önce kadını oynatıp daha sonra exit tuşu daha içte olacak şekilde oynatıyoruz. 
pygame.display.update()
while Warning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            pygame.display.flip()
            Warning = False

    run = True
    while run:
        clock.tick(60)
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                run = False 

        group.update(event_list)
        group.draw(screen)
        pygame.display.flip()



#Tuşun son işlemleri
    while True:
        for event in pygame.event.get():
            mouse = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if( w //20) <= mouse[0] <= ( w //20 ) + 50 and (h//23) <= mouse[1] <= (h//23) +30 :
                    pygame.quit()
        pygame.draw.rect( screen, beyaz ,[int(w//20), int(h//23) ,50,30] )
        screen.blit(yazi,[(w//20) + 5, (h//23) + 5])
        mouse = pygame.mouse.get_pos()
        if   ( w //20) <= mouse[0] <= ( w //20 ) + 50 and (h//23) <= mouse[1] <= (h//23) +30 :
            pygame.draw.rect( screen,kirmizi ,[ int(w//20), int(h//23) ,50,30] )
            screen.blit(yazi_1,[(w/20) + 5, (h/23) + 3])
        pygame.display.flip()   

pygame.quit()
exit()
