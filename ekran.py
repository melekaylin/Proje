import pygame as pg
import sys
pg.init()

en , boy = 1000 , 700
siyah = 0, 0, 0
beyaz = 255, 255, 255
kırmızı = 255, 0, 0
yesil = 90, 180, 90
mavi = 3, 28, 252

ekran = pg.display.set_mode( (en , boy) )

while True :
    for event in pg.event.get() :
        if event.type == pg.QUIT :
            sys.exit() ;
        ekran.fill(siyah)
        pg.draw.rect(ekran,beyaz,pg.Rect(10,300,300,200))
        pg.display.flip()