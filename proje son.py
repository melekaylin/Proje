# Proje
#Tanımlamalar
"""
Oyun için gereken modülleri ekledik.
pygame oyun modülü,
sys, çıkış yapmak için kullanılıyor.
"""
import pygame 
import sys
pygame.init()

#Değişkenler tanımlanıyor,

tumcizgiler=[]        #üretilen her bir ışını burada saklıyoruz ki sonra temizlemek mümkün olsun
elipsvarmi=False      #ekranda ELIPS/filtre olup olmadığını bilmek için
buttonstart_visible = True   #ilk açılışta start butonu görünsün, ve sonra gizlensin, 
buttonreset_visible = False  #ilk açılışta RESET butonu gizlensin, start baslınca görünsün

#renk tanimlari yapılıyor
#renkler RGB modeline uygun olarak bir TUPLE şeklinde tanımlanır
gray=(176,176,176)
yesil=(0,255,0)
kirmizi=(255,0,0)
mavi=(0,0,255)

#ışınlara basılması durumunda filtrenin alacağı rengi tutacak olan değişkenleri belirledik.
yesildeger=0
kirmizideger=0
mavideger=0

#Ekran ayarları yapılıyor, ekran genişliği 1000, yükseklik 700, arka plan GRİ, ve başlığı IŞIK ve RENKLER
screen = pygame.display.set_mode((1000,700), pygame.SWSURFACE) #pygame penceresine başlık attık
screen.fill(gray)
pygame.display.set_caption("Işık Ve Renkler") 

#projede kullanılacak görseller tanımlanıyor,
proje = pygame.image.load('projeiçinfoto.png')      #Kadın görseli
yesilfener = pygame.image.load('yesil_fener.png')   #Yeşil Fener görseli
mavifener = pygame.image.load('mavi_fener.png')     #Mavi Fener Görseli
kirmizifener = pygame.image.load('kirmizi_fener.png') #Kırmızı Fener Görseli


#KIRMIZI ışın yayan bir buton geliştirdik,
#Bu butonunun görseli, yukarıdaki görsellerden kirmizifener dir,
button_kirmizi_fener = kirmizifener
button_kirmizi_fener = pygame.transform.scale(kirmizifener, (100, 100))
button_rect_kirmizi_fener = button_kirmizi_fener.get_rect()
button_rect_kirmizi_fener.center = (900,100)

#YEŞİL ışın yayan bir buton geliştiriyoruz,
#Bu butonunun görseli, yukarıdaki görsellerden yesilfener dir,
button_yesil_fener = yesilfener
button_yesil_fener = pygame.transform.scale(yesilfener, (100, 100))
button_rect_yesil_fener = button_yesil_fener.get_rect()
button_rect_yesil_fener.center = (900,300)

#MAVİ ışın yayan bir buton geliştiriyoruz,
#Bu butonunun görseli, yukarıdaki görsellerden mavifener dir,
button_mavi_fener = mavifener
button_mavi_fener = pygame.transform.scale(mavifener, (100, 100))
button_rect_mavi_fener = button_mavi_fener.get_rect()
button_rect_mavi_fener.center = (900,500)

#Tüm fenerlerin ve kadin görselinin ekrana yerleşmesini için
screen.blit(button_kirmizi_fener, button_rect_kirmizi_fener)
screen.blit(button_yesil_fener, button_rect_yesil_fener)
screen.blit(button_mavi_fener, button_rect_mavi_fener)
screen.blit(proje,(50,90))


# Görüntüyü güncelliyoruz
pygame.display.flip()






#Filtre üretimi için gereken fonksiyondur.
#hangi renk filtre üreteceğini aldığı parametrelerdeki değerler belirlemektedir.

def filtre_uret(r,g,b):
    print("Filtre Üret Fonk Çağırıldı")
    global elipsvarmi
    elipsvarmi=True
    global mavideger
    global kirmizideger
    global yesildeger
    mavideger=b
    kirmizideger=r
    yesildeger=g
    #Tüm ışınları sil
    oklarisil()
    #eğer r değerin 0 dan büyükse kırmızı ışınları çiz
    if r>0:
        kirmiziisinlar()
    #eğer g değerin 0 dan büyükse yeşil ışınları çiz
    if g>0:
        yesilisinlar()
    #eğer b değerin 0 dan büyükse kırmızı ışınları çiz
    if b>0:
        maviisinlar()
    #bu değerlere baglı olarak elips olustur
    ellipseciz()   

def ellipseciz():
    #kullanıcının belirledği R,G,B değerlerine göre ellips çizer
    print("Elips çiz fonk çağırıldı")
    global elipsvarmi
    elipsvarmi=True
    pygame.draw.ellipse(screen, (kirmizideger, yesildeger, mavideger), (550, 100, 100, 400))

#Bu fonksiyon yeşil ışın çizer
#Bunun için yesildeger isimli değişkene ihtiyaç duyar
#En fazla 10 adet yeşil ışın çizebilmektedir.
#Bu nedenle yesildeger değişkeninin 255/10 olan yaklaşık 25 arttırır
#Işın çizimi bitince gider ve elipsin yeniden oluşmasını sağlar, çünkü değişen GREEN değerini yansıtmak gerek
def yesilisinlar():
    global elipsvarmi
    if elipsvarmi:
        global yesildeger
        if yesildeger<250:
            yesildeger+=25
        print("Yeşil Işın Değeri:",yesildeger)
        for i in range(yesildeger//25):
            pygame.draw.aaline(screen,yesil,(860,300),(600,175+(25*i)))
            cizgi=(860,300,600,175+(25*i))
            tumcizgiler.append(cizgi)
        
        ellipseciz()
#Bu fonksiyon Kırmızı ışın çizer
#Bunun için kirmizideger isimli değişkene ihtiyaç duyar
#En fazla 10 adet kırmızı ışın çizebilmektedir.
#Bu nedenle kirmizideger değişkeninin 255/10 olan yaklaşık 25 arttırır
#Işın çizimi bitince gider ve elipsin yeniden oluşmasını sağlar, çünkü değişen RED değerini yansıtmak gerek

def kirmiziisinlar():
    global elipsvarmi
    if elipsvarmi:
        global kirmizideger
        if kirmizideger<250:
            kirmizideger+=25
        print("Kırmızı Işın Değeri:",kirmizideger)
        for i in range(kirmizideger//25):
            pygame.draw.aaline(screen,kirmizi,(860,120),(600,125+(25*i)))
            cizgi=(860,120,600,125+(25*i))
            tumcizgiler.append(cizgi)
        ellipseciz()

#Bu fonksiyon mavi ışın çizer
#Bunun için mavideger isimli değişkene ihtiyaç duyar
#En fazla 10 adet mavi ışın çizebilmektedir.
#Bu nedenle yesildeger değişkeninin 255/10 olan yaklaşık 25 arttırır
#Işın çizimi bitince gider ve elipsin yeniden oluşmasını sağlar, çünkü değişen BLUE değerini yansıtmak gerek

def maviisinlar():
    global elipsvarmi
    
    if elipsvarmi:
        global mavideger
        if mavideger<250:
            mavideger+=25
        print("MAvi Işın Değeri:",mavideger)
        for i in range(mavideger//25):
            pygame.draw.aaline(screen,mavi,(860,490),(600,225+(25*i)))
            cizgi=(860,490,600,225+(25*i))
            tumcizgiler.append(cizgi)
        ellipseciz()


#OYun başlaması için gereken butondur.
#Başlar başlamaz bir ellips çizer ve diğer butonların da calısmasını sağlar
def start():
    print("Start Butonuna Basıldı")
    ellipseciz()

#Okların silinmesini sağlayan koddur.
#aslında gerçek anlamda okları silmiyoruz.
#daha önce çizilen her bir okun koordinatları üzerinde GRAY yeni oklar olusturuyoruz.
#Bir bakıma üstünden GRİ ile geçiyoruz
def oklarisil():
    global tumcizgiler
    print("Oklar silindi")
    if len(tumcizgiler)>0:
        for _ in range(10):
            for x1,y1,x2,y2 in tumcizgiler:
                pygame.draw.aaline(screen,gray,(x1,y1),(x2,y2),5)
    tumcizgiler=[]

#RESET butonuna basınca, önce okları siler ve sonra yenidne r:0,g:0,b:0 bir elips olusturur
def reset():
    oklarisil()
    
    global elipsvarmi
    elipsvarmi=True
    filtre_uret(0,0,0)
    

    
#Oyundan çıkmak için  gereken kodlardır
def quit():
    print("Quit buttona basildi")
    pygame.quit()
    sys.exit()


#START, RESET ve QUIT butonlarının oluştuğu ve konumlandığı ve ayrıca üzerindeki METİNlerin yazıldığı alandır
start_button = pygame.Rect(50, 50, 75, 25)
reset_button = pygame.Rect(50, 100, 75, 25)
quit_button = pygame.Rect(50, 150, 75, 25)
font = pygame.font.Font(None, 30)
start_text = font.render("START", True, (255, 255, 255))
reset_text = font.render("RESET", True, (255, 255, 255))
quit_text = font.render("QUIT", True, (255, 255, 255))



#KIRMIZI, YEŞİL ve MAVİ Filtre butonlarının oluştuğu ve konumlandığı ve ayrıca üzerindeki METİNlerin yazıldığı alandır
kirmizi_filtre_button = pygame.Rect(520, 50, 50, 25)
yesil_filtre_button = pygame.Rect(570, 50, 50, 25)
mavi_filtre_button = pygame.Rect(620, 50, 50, 25)
font = pygame.font.Font(None, 30)
kirmizi_filtre_text = font.render("R", True, (255, 255, 255))
yesil_filtre_text = font.render("G", True, (255, 255, 255))
mavi_filtre_text = font.render("B", True, (255, 255, 255))



#Basılan tusları kontrol ettiğimiz alandayız
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            #Start butonu basıldığında, kendini gizlesin ve 
            # reset butonu aktif olsun diye değişkenlere değer atarız
            #arından start fonk cagırırız
            if start_button.collidepoint(event.pos):
                buttonstart_visible = not buttonstart_visible
                buttonreset_visible=not buttonreset_visible
                start()
            #Reset butonu basıldıgında reset fonk cagırırız
            if reset_button.collidepoint(event.pos):
                reset()
            #QUIT butonu basıldığında quit fonk cagırırız
            if quit_button.collidepoint(event.pos):
                quit()
            #Yeşil fener butonu basıldıgında yesilisinlar isimli fonk cagırırız
            if button_rect_yesil_fener.collidepoint(event.pos):
                yesilisinlar()
            #Kırmızı fener butonu basıldıgında kirmiziisinlar isimli fonk cagırırız
            if button_rect_kirmizi_fener.collidepoint(event.pos):
                kirmiziisinlar()
            #Mavi fener butonu basıldıgında maviisinlar isimli fonk cagırırız
            if button_rect_mavi_fener.collidepoint(event.pos):
                maviisinlar()

            #Kırmızı filtre butonu basıldıgında filtre_uret isimli fonk cagırırız
            #ve bu fonksiyona red : 255, greeen: 0 , blue: 0 değerlerini parametre olarak göndeririz.
            if kirmizi_filtre_button.collidepoint(event.pos):
                filtre_uret(255,0,0)
            #Mavi filtre butonu basıldıgında filtre_uret isimli fonk cagırırız
            #ve bu fonksiyona red : 0, greeen: 0 , blue: 255 değerlerini parametre olarak göndeririz.
            if mavi_filtre_button.collidepoint(event.pos):
                filtre_uret(0,0,255)
            #Yeşil filtre butonu basıldıgında filtre_uret isimli fonk cagırırız
            #ve bu fonksiyona red : 0, greeen: 255 , blue: 0 değerlerini parametre olarak göndeririz.
            if yesil_filtre_button.collidepoint(event.pos):
                filtre_uret(0,255,0)
            

    
    
    #Çıkışl butonunu ve textini yerleştiriyoruz
    pygame.draw.rect(screen, (255, 0, 0), quit_button)
    screen.blit(quit_text, (60, 155))

    #Filtre butonlarını konumlandırıp yerleştiriyororuz
    pygame.draw.rect(screen, (255, 0, 0), kirmizi_filtre_button)
    pygame.draw.rect(screen, (0, 255, 0), yesil_filtre_button)
    pygame.draw.rect(screen, (0, 0, 255), mavi_filtre_button)
    screen.blit(kirmizi_filtre_text, (540, 50))
    screen.blit(yesil_filtre_text, (590, 50))
    screen.blit(mavi_filtre_text, (640, 50))


    #Start butonu görünecekse, ona göre yerleşim yapıyoruz
    if buttonstart_visible:
        pygame.draw.rect(screen, (0, 255, 0), start_button)
        screen.blit(start_text, (60, 55))

    #Reset butonu görünecekse ona göre yerleşim yapıyoruz   
    if buttonreset_visible:
        pygame.draw.rect(screen, (0, 0, 255), reset_button)
        screen.blit(reset_text, (60, 105))
        pygame.draw.rect(screen, gray, start_button)
        
        
    
    
    

    pygame.display.update()