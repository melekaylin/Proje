elipsvarmi=False      #ekranda ELIPS olup olmadığını tutuyor

gray=(176,176,176)
yesil=(0,255,0)
kirmizi=(255,0,0)
mavi=(0,0,255)

#ışınlara basılması durumunda filtrenin alacağı rengi tutacak olan değişkenlerdir.
yesildeger=0
kirmizideger=0
mavideger=0

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
    #bu değerlere baglı olarak filtre olustur
    ellipseciz()  


def ellipseciz():
    #kullanıcının belirledği R,G,B değerlerine göre filtre çizer
    print("Elips çiz fonk çağırıldı")
    global elipsvarmi
    elipsvarmi=True
    pygame.draw.ellipse(screen, (kirmizideger, yesildeger, mavideger), (550, 100, 100, 400))


#KIRMIZI, YEŞİL ve MAVİ Filtre butonlarının oluştuğu ve konumlandığı ve ayrıca üzerindeki METİNlerin yazıldığı alandır
kirmizi_filtre_button = pygame.Rect(520, 50, 50, 25)
yesil_filtre_button = pygame.Rect(570, 50, 50, 25)
mavi_filtre_button = pygame.Rect(620, 50, 50, 25)
font = pygame.font.Font(None, 30)
kirmizi_filtre_text = font.render("R", True, (255, 255, 255))
yesil_filtre_text = font.render("G", True, (255, 255, 255))
mavi_filtre_text = font.render("B", True, (255, 255, 255))

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

    #Filtre butonlarını konumlandırıp yerleştiriyororuz
    pygame.draw.rect(screen, (255, 0, 0), kirmizi_filtre_button)
    pygame.draw.rect(screen, (0, 255, 0), yesil_filtre_button)
    pygame.draw.rect(screen, (0, 0, 255), mavi_filtre_button)
    screen.blit(kirmizi_filtre_text, (540, 50))
    screen.blit(yesil_filtre_text, (590, 50))
    screen.blit(mavi_filtre_text, (640, 50))