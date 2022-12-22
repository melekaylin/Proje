import pygame as pg
import sys
import random
pg.init()

# kırmızı
class k_foton:
    def __init__(self,) -> None:
        self.x = random.randrange(400,700)
        self.y = random.randrange(400,700)
        self.cap = 5
        self.x_speed = 10
        self.y_speed = 10
        self.renk = 255, 0, 0
    def hareket_ettir (self,ekran_en,ekran_boy) :
        self.x -= self.x_speed
        self.y -= self.y_speed

        if self.x > ekran_en or self.x < 0 :
            self.x_speed *= 1
        if self.y > ekran_boy or self.x < 0 :
            self.y_speed *= 1 
    
    def cizdir (self,ekran) :
        pg.draw.circle(ekran,self.renk,(self.x , self.y) , self.cap)
        
    def hareket_sürekliligi (self) :
        for event in pg.event.get() :
            if event.type == pg.QUIT :
                sys.exit() ;
            return 
        self.cizdir

# mavi
class m_foton:
    def __init__(self) -> None:
        self.x = random.randrange(200,600)
        self.y = random.randrange(400,700)
        self.cap = 5
        self.x_speed = 10
        self.y_speed = 10
        self.renk = 0, 0, 255
    def hareket_ettir (self,ekran_en,ekran_boy) :
        self.x -= self.x_speed
        self.y += self.y_speed

        if self.x > ekran_en or self.x < 0 :
            self.x_speed *= 1
        if self.y > ekran_boy or self.x < 0 :
            self.y_speed *= 1 
    
    def cizdir (self,ekran) :
        pg.draw.circle(ekran,self.renk,(self.x , self.y) , self.cap)
        
    def hareket_sürekliligi (self) :
        for event in pg.event.get() :
            if event.type == pg.QUIT :
                sys.exit() ;
            return 
        self.cizdir

# yeşil
class y_foton:
    def __init__(self) -> None:
        self.x = random.randrange(400,700)
        self.y = random.randrange(200,700)
        self.cap = 5
        self.x_speed = 10
        self.y_speed = 10
        self.renk = 0, 255, 0
    def hareket_ettir (self,ekran_en,ekran_boy) :
        self.x += self.x_speed
        self.y += self.y_speed

        if self.x > ekran_en or self.x < 0 :
            self.x_speed *= 1
        if self.y > ekran_boy or self.x < 0 :
            self.y_speed *= 1 
    
    def cizdir (self,ekran) :
        pg.draw.circle(ekran,self.renk,(self.x , self.y) , self.cap)
        
    def hareket_sürekliligi (self) :
            self.cizdir
            self.hareket_ettir
            

    
en , boy = 1000,700
siyah = 0, 0, 0
beyaz = 255, 255, 255
kırmızı = 255, 0, 0
yesil = 0, 255, 0
mavi = 0, 0, 255

x , y = en//2 , boy//2
clock = pg.time.Clock()

ekran = pg.display.set_mode( (en , boy) )

fotonlar = []
for i in range(100) :
    fotonlar.append(k_foton())
    fotonlar.append(m_foton())
    fotonlar.append(y_foton())

    
while True :
    for event in pg.event.get() :
        if event.type == pg.QUIT :
            sys.exit() ;
        
    ekran.fill(siyah)

    for ind in range(len(fotonlar)) :
        fotonlar[ind].hareket_ettir(en,boy)
        fotonlar[ind].cizdir(ekran)
        fotonlar[ind].hareket_sürekliligi()
        for ind2 in range(len(fotonlar)):
            if ind == ind2 :
                continue
    
                
    pg.display.flip()
    clock.tick(30)