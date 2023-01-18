gray=(176,176,176)
yesil=(0,255,0)
kirmizi=(255,0,0)
mavi=(0,0,255)

#KIRMIZI ışın yayan bir buton geliştiriyoruz,
#Bu butonunun görseli, yukarıda tanımlanan görsellerden kirmizifener dir,
button_kirmizi_fener = kirmizifener
button_kirmizi_fener = pygame.transform.scale(kirmizifener, (100, 100))
button_rect_kirmizi_fener = button_kirmizi_fener.get_rect()
button_rect_kirmizi_fener.center = (900,100)


#YEŞİL ışın yayan bir buton geliştiriyoruz,
#Bu butonunun görseli, yukarıda tanımlanan görsellerden yesilfener dir,
button_yesil_fener = yesilfener
button_yesil_fener = pygame.transform.scale(yesilfener, (100, 100))
button_rect_yesil_fener = button_yesil_fener.get_rect()
button_rect_yesil_fener.center = (900,300)

#MAVİ ışın yayan bir buton geliştiriyoruz,
#Bu butonunun görseli, yukarıda tanımlanan görsellerden mavifener dir,
button_mavi_fener = mavifener
button_mavi_fener = pygame.transform.scale(mavifener, (100, 100))
button_rect_mavi_fener = button_mavi_fener.get_rect()
button_rect_mavi_fener.center = (900,500)

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