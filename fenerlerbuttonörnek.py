import pygame

# 
class button(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__() 
        self.original_image = pygame.Surface((50, 50), pygame.SRCALPHA)
        pygame.draw.circle(self.original_image, color, (25, 25), 25)
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

pygame.init()
w , h = 1000 ,700
screen = pygame.display.set_mode((w,h ))
clock = pygame.time.Clock()



#  butonlar  için konumlandırma bloğu
sprite_object = button(*screen.get_rect().center, (128, 128, 0))
group = pygame.sprite.Group([
    button(screen.get_width() *2 // 3, (screen.get_height() // 2)+50, (128, 0, 0)),
    button(screen.get_width() *2 // 3, (screen.get_height() // 2)+100, (0, 128, 0)),
    button(screen.get_width() *2 // 3, (screen.get_height() // 2)+150, (0, 0, 128)),

])

run = True
while run:
    clock.tick(60)
    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            run = False 

    group.update(event_list)

    screen.fill(0)
    group.draw(screen)
    pygame.display.flip()

pygame.quit()
exit()