import pygame

siyah = (0,0,0)
beyaz = (255,255,255)
kirmizi = (255,0,0)
turuncu = (255,165,0)
sari = (255,255,0)
yeşil = (50,205,50)
mavi = (0,0,255)
mor = (160,32,240)
gray =(176,176,176)
dark_gray =(40,40,40)



class button(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__() 
        self.original_image = pygame.Surface((50, 50), pygame.SRCALPHA)
        pygame.draw.circle(self.original_image, color, (25, 25), 25)
        pygame.draw.circle(self.original_image, (siyah), (25, 25), 25, 4)
        self.click_image = pygame.Surface((50, 50), pygame.SRCALPHA)
        pygame.draw.circle(self.click_image, color, (25, 25), 25)
        pygame.draw.circle(self.click_image, (beyaz), (25, 25), 25, 4)
        self.image = self.original_image 
        self.rect = self.image.get_rect(center = (x, y))
        self.clicked = False

    def update(self, event_list):
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    self.clicked = not self.clicked

        self.image = self.click_image if self.clicked else self.original_image

pygame.init()
w , h = 1000 ,700
screen = pygame.display.set_mode((w,h ))
clock = pygame.time.Clock()



#  yeşil buton için konumlandırma bloğu
sprite_object = button(*screen.get_rect().center, (yeşil))
group = pygame.sprite.Group([
    button(screen.get_width() *2 // 3+ +255, (screen.get_height() // 6 )+5, (0, 128, 0)),

])

run = True
while run:
    clock.tick(60)
    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            run = False 

    group.update(event_list)

    screen.fill(gray)
    group.draw(screen)
    pygame.display.flip()

pygame.quit()
exit()