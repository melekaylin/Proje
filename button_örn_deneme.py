import pygame as pg


class key (pg.sprite.Sprite):
    def __init__(self,xpos,ypos ,id) :
        super(key , self).__init__()
        self.image =pg.image.load ("button.png").convert()
        self.clicked = False
        self.rect= self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos
        self.clicked = False
        self.id = id
        self.linkReady = False
        self.links = []


# renkler
siyah = (0,0,0)
kirmizi = (255,0,0)
turuncu = (255,165,0)
sari = (255,255,0)
yeşil = (50,205,50)
mavi = (0,0,255)
mor = (160,32,240)
gray = (176,176,176)


pg.init()

w , h = 1000 , 700
screen = pg.display.set_mode((w, h))
screen.fill(gray)

pg.display.set_caption("yeni pencere")

done = False
clock = pg.time.Clock()

key_list = pg.sprite.Group()

# Ana döngü

while not done :
    for event in pg.event.get() :
        if event.type ==  pg.QUIT:
            done = True

        if event.type == pg.MOUSEBUTTONDOWN:
            pos = pg.mouse.get_pos()
            x = pos[0]
            y = pos[1]
            if event.button == 3 :
                key_list.add(key(x,y ,len(key_list)+1))
            elif event.button == 1 :
                for key in key_list :
                    if key.rect.collidepoint(pos) :
                        key.clicked = True
            elif event.button == 2 :
                for key in key_list :
                    if key.rect.collidepoint(pos):
                        key.linkReady = True
                        count = 0
                        links = []
                        for key in key_list :
                            if key.linkReady == True :
                                count += 1 
                                links.append (key.id)
                        if count == 2 :
                            for key in key_list :
                                if key.linkReady == True :
                                    key.linkReady = False
                                    count += 1
                                    key.links += links
            
            if event.type == pg.MOUSEBUTTONUP:
                for key in key_list :
                    key.clicked = False 
                drag_id = 0

        if event.type == pg.MOUSEBUTTONUP:
            for key in key_list :
                pos = pg.mouse.get_pos()
                key.rect.x = pos[0]-(key.rect.width/2)
                key.rect.y = pos[1]-(key.rect.height/2)

    screen.fill(gray)

    key_list.draw(screen)

    pg.display.flip()
    clock.tick (60)
pg.quit