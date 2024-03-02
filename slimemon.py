import pgzrun
import time

WIDTH = 690
HEIGHT = 410

player = Actor("down_1")
player.pos = (400,240)


tuccar = Actor("tuccar")
tuccar.pos = (610,370) # TUCCAR

iskelet1 = Actor("iskelet1")
iskelet1.pos = (120,45)

iskelet1_seviye_bar = Actor("kilic")
iskelet1_seviye_bar.pos = (125,98)

iskelet2 = Actor("iskelet1")
iskelet2.pos = (50,145)

iskelet2_seviye_bar = Actor("kilic")
iskelet2_seviye_bar.pos = (55,200)


canavar1 = Actor("canavar1")
canavar1.pos = (260,260)

canavar1_seviye_bar = Actor("kilic")
canavar1_seviye_bar.pos = (265,210)

canavar2 = Actor("canavar2")
canavar2.pos = (385,245)

canavar2_seviye_bar = Actor("kilic")
canavar2_seviye_bar.pos = (390,190)

kaktus = Actor("kaktus")
kaktus.pos = (570,195)

kaktus_seviye_bar = Actor("kilic")
kaktus_seviye_bar.pos = (575,255)

kaktus_boss = Actor("kaktus_boss")
kaktus_boss.pos = (300,60)

kaktus_boss_seviye_bar = Actor("kilic")
kaktus_boss_seviye_bar.pos = (305,110)

kaktus_savas = Actor("kaktus")
kaktus_savas.pos = (480,90)

kaktus_boss_savas = Actor("kaktus_boss")
kaktus_boss_savas.pos = (480,90)


vampir =Actor("vampir")
vampir.pos = (570,195)

vampir_seviye_bar = Actor("kilic")
vampir_seviye_bar.pos = (575,255)

vampir_boss = Actor("vampir_boss")
vampir_boss.pos = (350,80)

vampir_boss_seviye_bar = Actor("kilic")
vampir_boss_seviye_bar.pos = (365,140)



vampir_savas = Actor("vampir")
vampir_savas.pos = (480,90)

vampir_boss_savas = Actor("vampir_boss")
vampir_boss_savas.pos = (480,90)


orumcek = Actor("orumcek")
orumcek.pos = (605,215)

orumcek_seviye_bar = Actor("kilic")
orumcek_seviye_bar.pos = (610, 270)

orumcek_savas = Actor("orumcek")
orumcek_savas.pos = (489,90)

orumcek_boss = Actor("orumcek_boss")
orumcek_boss.pos =(360,70)

orumcek_boss_seviye_bar = Actor("kilic")
orumcek_boss_seviye_bar.pos = (365,140)

orumcek_boss_savas = Actor("orumcek_boss")
orumcek_boss_savas.pos = (480,90)


orumcek
iskelet_boss = Actor("iskelet_boss")
iskelet_boss.pos = (355,90)

iskelet_boss_savas = Actor("iskelet_boss")
iskelet_boss_savas.pos = (480,90)

iskelet_boss_seviye_bar = Actor("kilic")
iskelet_boss_seviye_bar.pos = (360,160)




 ###################

gecit_1 = Actor("gecit")
gecit_1.pos = (100,100)

gecit_2 = Actor("gecit")
gecit_2.pos = (250,130)
#PORTALLAR
gecit_3 = Actor("gecit")
gecit_3.pos = (390,80)

gecit_4 = Actor("gecit")
gecit_4.pos = (600,200)

################################

gecit2_1 = Actor("gecit2")
gecit2_1.pos = (295,260)

gecit2_2 = Actor("gecit2")
gecit2_2.pos = (320,260)

gecit2_3 = Actor("gecit2")
gecit2_3.pos = (280,230)

gecit2_4 = Actor("gecit2")
gecit2_4.pos = (250,250)

 ##################

portal_bar_icon1 = Actor("portal_bar_icon")
portal_bar_icon1.pos = (100,50)

portal_bar_icon2 = Actor("portal_bar_icon")
portal_bar_icon2.pos = (250,100)

portal_bar_icon3 = Actor("portal_bar_icon")
portal_bar_icon3.pos = (390,30)

portal_bar_icon4 = Actor("portal_bar_icon")
portal_bar_icon4.pos = (600,150)



slime1_icon = Actor("slime_1")
slime1_icon.pos = (30,345)




kilic1_icon = Actor("kilic")
kilic1_icon.pos = (70,340)



xp_icon1 = Actor("xp")
xp_icon1.pos = (70, 375)

can_icon = Actor("can_icon")
can_icon.pos = (70,310)




gold_icon = Actor("gold_icon")
gold_icon.pos = (155,322) # ALTIN İKON

iksir_icon = Actor("iksir_icon")
iksir_icon.pos = (250, 320) # ANAHTAR İKONU

kafatasi_icon = Actor("kafatasi_icon")
kafatasi_icon.pos = (305, 320) # KAFATASI İKONU

sol_el_icon = Actor("sol_el_icon")
sol_el_icon.pos = (20,200)

sag_el_icon = Actor("sag_el_icon")
sag_el_icon.pos = (670,200)

m_icon = Actor("m_icon")
m_icon.pos = (100,80)

m_icon2 = Actor("m_icon")
m_icon2.pos = (250,130)

m_icon3 = Actor("m_icon")
m_icon3.pos = (390,60)

m_icon4 = Actor("m_icon")
m_icon4.pos = (600,180)

k_icon1 = Actor("k_icon")
k_icon1.pos = (100,60)

k_icon2 = Actor("k_icon")
k_icon2.pos = (250,115)

k_icon3 = Actor("k_icon")
k_icon3.pos = (390,60)

k_icon4 = Actor("k_icon")
k_icon4.pos = (600,170)

ust_el_icon = Actor("ust_el_icon")
ust_el_icon.pos = (170,260)

ust_el_icon2 = Actor("ust_el_icon")
ust_el_icon2.pos = (420,380)


slime1_guc = 4
slime1_can = 35

slime2_guc = 0
slime3_guc = 0

slime1_xp = 0
slime2_xp = 0  # o anki mevcut xpsi
slime3_xp = 0

slime1_level = 0
slime1_level_max = 10

gold = 10
kafatasi = 0
iksir = 0
damage_iksir = 0

savas_buton_1 = Actor("savas_buton")
savas_buton_1.pos = (180,240)

savas_buton_2 = Actor("savas_buton")
savas_buton_2.pos = (300,240)

savas_buton_3 = Actor("savas_buton")
savas_buton_3.pos = (420,240)


savas_buton_kilic = Actor("savas_buton_kilic")
savas_buton_kilic.pos = (200,239)

savas_buton_item = Actor("savas_buton_item")
savas_buton_item.pos = (315,235)

savas_buton_run = Actor("savas_buton_run")
savas_buton_run.pos = (430,239)


screen_2 = False
konum = False

screen_3 = False
konum2 = False

screen_4 = False
konum3 = False

screen_5 = False
konum4 = False

screen_6 = False
konum5 = False

m_bas = False
m_bas2 = False
m_bas3 = False
m_bas4 = False

dusman_base1 = False
dusman_base2 = False
dusman_base3 = False
dusman_base4 = False

savas_ani = False
savas_bitir = False # savas ekranından cıkmak icin
savas_durum = False

oyuncu_konum = False

iskelet1_savas = Actor("iskelet1_savas")
iskelet1_savas.pos = (480,90)

canavar1_savas = Actor("canavar1_savas") # CANAVAR 1 E CAN VE DAMAGAE VER
canavar1_savas.pos = (480,90)

canavar2_savas = Actor("canavar2_savas")
canavar2_savas.pos = (480,90)


iskelet1_can = 20
iskelet1_guc = 2

iskelet2_can = 20
iskelet2_guc = 4

canavar1_can = 40
canavar1_guc = 8

canavar2_can = 50
canavar2_guc = 10

slime1_kostum = "slime_1"
slime_1 = Actor(slime1_kostum)
slime_1.pos = (450,250)

slime_1_savas = Actor("slime_1_savas")
slime_1_savas.pos = (200,190)

space_durum = False



damage_yazisi = False
item = False

item_bar = Actor("item_bar")
item_bar.pos = (490,330)

damage_iksir_icon = Actor("damage_iksir_icon")
damage_iksir_icon.pos = (520,330)

iksir_icon_bar = Actor("iksir_icon_bar")
iksir_icon_bar.pos = (420, 330)


el_ikon = True

kaktus_can = 70
kaktus_guc = 13

kaktus_boss_can = 90
kaktus_boss_guc = 15

vampir_can = 100
vampir_guc = 17

vampir_boss_can = 120
vampir_boss_guc = 20

orumcek_can = 130
orumcek_guc = 22

orumcek_boss_can = 150
orumcek_boss_guc = 25

iskelet_boss_can = 190
iskelet_boss_guc = 30

tuccar_item_bar = Actor ("tuccar_item_bar")
tuccar_item_bar.pos = (580,300)
damage_iksir_ikon_bar = Actor("damage_iksir_icon_bar")
damage_iksir_ikon_bar.pos = (550,300)
iksir_ikon_bar = Actor("iksir_icon_1")
iksir_ikon_bar.pos = (590,300)
sag_el_icon2 = Actor("sag_el_icon")
sag_el_icon2.pos = (520,300)
tuccar_item_bar2 = Actor("tuccar_item_bar2")
tuccar_item_bar2.pos = (520,380)

damage_iksir_ikon_bar2 = Actor("damage_iksir_icon_bar")
damage_iksir_ikon_bar2.pos = (210,320)

seviye_bilgi = Actor("seviye_bilgi")
seviye_bilgi.pos = (530,230)


e_icon = Actor("e_icon")
e_icon.pos = (500,380)
def draw():
    global slime1_guc, slime2_guc, canavar2_guc, dusman_base2,kaktus_boss_durum,kaktus_boss_can,orumcek_can,slime1_can,vampir_can,orumcek_boss_can,iskelet_boss_can,vampir_boss_can, dusman_base4,space_durum,slime1_level, kaktus_can, gold,kafatasi, slime3_guc,savas_ani, konum, m_bas3, m_bas4, konum2, screen_3, screen_2,dusman_base3, screen_4, konum3, screen_5, konum4, screen_6, konum5, dusman_base1
    slime1_xp, slime2_xp, slime3_xp, m_bas, m_bas2
    gold, iksir, kafatasi

    if screen_2 == False and screen_3 == False and screen_4 == False: # ANA EKRAN
        screen.blit("game_screen_1", (0,0))


        

        gecit_1.draw()
        gecit_2.draw()
        gecit_3.draw()
        gecit_4.draw()

        slime_1.draw()
        player.draw()
        tuccar.draw()


        portal_bar_icon1.draw()
        portal_bar_icon2.draw()
        portal_bar_icon3.draw()
        portal_bar_icon4.draw()



        sol_el_icon.draw()


        screen.draw.text("1", (95,45), color="black", fontsize=18)
        screen.draw.text("2", (245,95), color="black",fontsize=18)
        screen.draw.text("3", (385,25), color="black",fontsize=18)
        screen.draw.text("4", (595,145), color="black",fontsize=18)

        if m_bas:
            m_icon.draw()

        if m_bas2:
            m_icon2.draw()

        if m_bas3:
            m_icon3.draw()

        if m_bas4:
            m_icon4.draw()


    if screen_2 == True: # OYUNCU SOLDAN CIKINCA

        screen.blit("game_screen_2", (0,0))
        iskelet1.draw()
        iskelet1_seviye_bar.draw()
        iskelet2.draw()
        iskelet2_seviye_bar.draw()
        canavar1.draw()
        canavar1_seviye_bar.draw()
        canavar2.draw()
        canavar2_seviye_bar.draw()
        slime_1.draw()
        player.draw()
        sag_el_icon.draw()
        savas_ekrani1()


        if not konum:
            player.pos = (680,200) # karakterin konumunu bir kere ayarla
            slime_1.pos = (690,200)
            konum = True

    if not screen_2:
        if konum:
            player.pos = (20,200) # eger karakter yine ekran dısına cıkarsa eski konuma donsun
            slime_1.pos = (10,200)
            konum = False



    if screen_3: # PORTAL 1 E GECİNCE
        if not dusman_base1:
            screen.blit("game_screen_3", (0,0))
            gecit_1.draw()
            gecit2_1.draw()
            slime_1.draw()
            kaktus.draw()
            kaktus_seviye_bar.draw()

            player.draw()
            if not konum2:
                player.pos = (60,50)
                slime_1.pos = (60,45)
                konum2 = True

            if player.colliderect(gecit_1): 
                k_icon1.draw()

            if player.colliderect(gecit_1) and keyboard.k:
                screen_3 = False 
                player.pos = (100,130) 
                slime_1.pos = (100,125)

            if kaktus_durum and screen_3: # KAKTUSE DEGERSE SAVAS
                savas()
                kaktus_savas.draw()
                slime_1_savas.draw()
                screen.draw.text(f"KATLETME ODULU: GOLD +19, LEVEL +25", (400,370), fontsize =15, color="yellow")
                screen.draw.text(f"TUHAF KAKTUS;  HEALT : {kaktus_can}\n DAMAGE : {kaktus_guc}", (120,40), fontsize=14, color="black") # iskelet can guc
                screen.draw.text(f"EVCIL SLIME; HEALT : {slime1_can}\n DAMAGE: {slime1_guc}", (390,150), fontsize=16, color="black")# slime 1 durum
                savas_ani = True

                if keyboard.space and ust_el_icon.pos == (410,260): # RUN 
                    player.pos = (200,200)
                    savas_ani = False
                   
                
                if kaktus_can <= 0: # eger iskeletin canı sıfıra inerse
                    slime1_level+=25 # level 2 art
                    gold+=19
                    kafatasi+=1
                    player.pos = (130,200) # konuma don
                    kaktus_can+=70 # iskelet yeniden dirilt
                    savas_ani = False # klavye kontrolu gel
                    slime1_can+=13

                if keyboard.space and ust_el_icon.pos == (170,260) and not space_durum: #DAMAGE BASINCA
                    
        
                    space_durum = True # SAVAS BASLANDIGINDA SPACE KULLANILAMAZ KI SLİME DAHA FAZLA UZAGA GİTMESİN

                    clock.schedule_unique(slime1_yaklas, 0.3)  
                    clock.schedule_unique(slime1_kaktus_vur, 0.8)  
                    clock.schedule_unique(slime1_geridon, 1.5)  

                    clock.schedule_unique(kaktus_yaklas, 2)
                    clock.schedule_unique(kaktus_vur, 2.5)
                    clock.schedule_unique(kaktus_geridon, 3)

                    clock.schedule_unique(space, 3.2) # SAVAS ANİMASYONU BİTİNCE SPACE YENİDEN KULLANILABİLSİN
                
                

                  

        if dusman_base1: # PORTAL 1 DE DUSMAN BASE E GİRİNCE
            
            screen.blit("siyah", (0,0))
            screen.blit("game_screen_7", (150,0))
            gecit2_1.draw()
            kaktus_boss.draw()
            kaktus_boss_seviye_bar.draw()
            slime_1.draw()
            player.draw()
            if player.colliderect(gecit2_1) and keyboard.k: # GECITE DEGIYOR VE ME YE BASIYORSA CIKSIN
                dusman_base1 = False

            if kaktus_boss_durum: # DUSMAN BASE DE KAKTUS BOSSA DEGINCE
                savas()
                kaktus_boss_savas.draw()
                slime_1_savas.draw()
                screen.draw.text(f"KATLETME ODULU: GOLD +24, LEVEL +30", (400,370), fontsize =15, color="yellow")

                screen.draw.text(f"GUCLU KAKTUS;  HEALT : {kaktus_boss_can}\n DAMAGE : {kaktus_boss_guc}", (120,40), fontsize=14, color="black") # iskelet can guc
                screen.draw.text(f"EVCIL SLIME; HEALT : {slime1_can}\n DAMAGE: {slime1_guc}", (390,150), fontsize=16, color="black")# slime 1 durum

                if keyboard.space and ust_el_icon.pos == (410,260): # RUN 
                    player.pos = (150,400)
                    savas_ani = False

                if keyboard.space and ust_el_icon.pos == (170,260) and not space_durum: #DAMAGE BASINCA
                    
        
                    space_durum = True # SAVAS BASLANDIGINDA SPACE KULLANILAMAZ KI SLİME DAHA FAZLA UZAGA GİTMESİN

                    clock.schedule_unique(slime1_yaklas, 0.3)  
                    clock.schedule_unique(slime1_kaktus_boss_vur, 0.8)  
                    clock.schedule_unique(slime1_geridon, 1.5)  

                    clock.schedule_unique(kaktus_boss_yaklas, 2)
                    clock.schedule_unique(kaktus_boss_vur, 2.5)
                    clock.schedule_unique(kaktus_boss_geridon, 3)

                    clock.schedule_unique(space, 3.2) # SAVAS ANİMASYONU BİTİNCE SPACE YENİDEN KULLANILABİLSİN
                
                if kaktus_boss_can <= 0: # eger iskeletin canı sıfıra inerse
                    slime1_level+=30 # level 2 art
                    gold+=24
                    kafatasi+=1
                    player.pos = (130,200) # konuma don
                    kaktus_boss_can+=90 # iskelet yeniden dirilt
                    savas_ani = False # klavye kontrolu gel
                    slime1_can+=15

                        
                
                
                

                
                    



    if screen_4: # PORTAL 2 YE GECİNCE
        screen.blit("game_screen_4", (0,0))
        gecit_2.draw()
        gecit2_2.draw()
        vampir.draw()
        vampir_seviye_bar.draw()
        slime_1.draw()
        player.draw()
        if not konum3:
            player.pos = (250,150) # konum ayarla bir kere
            slime_1.pos = (250,145)
            konum3 = True
        if player.colliderect(gecit_2): # portala degerse k iconu cıksın
            k_icon2.draw()
        if keyboard.k and player.colliderect(gecit_2): # k ye basınca ve degince portal 1 den cıksın
            screen_4 = False
            player.pos = (250,170)
            slime_1.pos = (250,165)


        if vampir_durum and screen_4 and not dusman_base2: # VAMPIRDE DEGDIGINDE
            savas()
            vampir_savas.draw()
            slime_1_savas.draw()
            screen.draw.text(f"KATLETME ODULU: GOLD +28, LEVEL +34", (400,370), fontsize =15, color="yellow")

            screen.draw.text(f"GUNES SEVEN VAMPIR;  HEALT : {vampir_can}\n DAMAGE : {vampir_guc}", (120,40), fontsize=14, color="black") 
            screen.draw.text(f"EVCIL SLIME; HEALT : {slime1_can}\n DAMAGE: {slime1_guc}", (390,150), fontsize=16, color="black")
            savas_ani = True

            if keyboard.space and ust_el_icon.pos == (410,260): # RUN 
                player.pos = (200,200)
                savas_ani = False

            if vampir_can <= 0: # eger iskeletin canı sıfıra inerse
                slime1_level+=34 # level 2 art
                gold+=28
                kafatasi+=1
                player.pos = (130,200) # konuma don
                vampir_can+=100 # iskelet yeniden dirilt
                savas_ani = False # klavye kontrolu gel
                slime1_can+=2
                slime1_can+=17

            
            if keyboard.space and ust_el_icon.pos == (170,260) and not space_durum: #DAMAGE BASINCA
                    
        
                    space_durum = True # SAVAS BASLANDIGINDA SPACE KULLANILAMAZ KI SLİME DAHA FAZLA UZAGA GİTMESİN

                    clock.schedule_unique(slime1_yaklas, 0.3)  
                    clock.schedule_unique(slime1_vampir_vur, 0.8)  
                    clock.schedule_unique(slime1_geridon, 1.5)  

                    clock.schedule_unique(vampir_yaklas, 2)
                    clock.schedule_unique(vampir_vur, 2.5)
                    clock.schedule_unique(vampir_geridon, 3)

                    clock.schedule_unique(space, 3.2) # SAVAS ANİMASYONU BİTİNCE SPACE YENİDEN KULLANILABİLSİN
                
                


        if dusman_base2: # PORTAL 2 DE DUSMAN BASE E GECİNCE
            
            screen.blit("siyah", (0,0))
            screen.blit("game_screen_8", (200,0))
            gecit2_2.draw()
            vampir_boss.draw()
            vampir_boss_seviye_bar.draw()
            slime_1.draw()
            player.draw()
            if keyboard.k and player.colliderect(gecit2_2):
                dusman_base2 = False
               

            if player.colliderect(vampir_boss) and dusman_base2: # VAMPIR BOSS A DEGINCE
                savas()
                vampir_boss_savas.draw()
                slime_1_savas.draw()
                screen.draw.text(f"KATLETME ODULU: GOLD +30, LEVEL +40, +YENI KOSTUM", (400,370), fontsize =15, color="yellow")

                screen.draw.text(f"DISSIZ VAMPIR;  HEALT : {vampir_boss_can}\n DAMAGE : {vampir_boss_guc}", (120,40), fontsize=14, color="black") 
                screen.draw.text(f"EVCIL SLIME; HEALT : {slime1_can}\n DAMAGE: {slime1_guc}", (390,150), fontsize=16, color="black")
                savas_ani = True

                if keyboard.space and ust_el_icon.pos == (410,260): # RUN 
                    player.pos = (200,400)
                    savas_ani = False

                if vampir_boss_can <= 0:
                    slime1_level+=40 # level 2 art
                    gold+=30
                    kafatasi+=1
                    player.pos = (130,200) # konuma don
                    vampir_boss_can+=120 # iskelet yeniden dirilt
                    savas_ani = False # klavye kontrolu gel
                    slime_1.image = "slime_2"
                    slime_1_savas.image = "slime_2"
                    slime1_can+=20

                if keyboard.space and ust_el_icon.pos == (170,260) and not space_durum: #DAMAGE BASINCA
                    
        
                    space_durum = True # SAVAS BASLANDIGINDA SPACE KULLANILAMAZ KI SLİME DAHA FAZLA UZAGA GİTMESİN

                    clock.schedule_unique(slime1_yaklas, 0.3)  
                    clock.schedule_unique(slime1_vampir_boss_vur, 0.8)  
                    clock.schedule_unique(slime1_geridon, 1.5)  

                    clock.schedule_unique(vampir_boss_yaklas, 2)
                    clock.schedule_unique(vampir_boss_vur, 2.5)
                    clock.schedule_unique(vampir_boss_geridon, 3)

                    clock.schedule_unique(space, 3.2) # SAVAS ANİMASYONU BİTİNCE SPACE YENİDEN KULLANILABİLSİN
                



    if screen_5: # portal 3 e gectiginde
        screen.blit("game_screen_5", (0,0))
        gecit_3.draw()
        gecit2_3.draw()
        orumcek.draw()
        orumcek_seviye_bar.draw()
        slime_1.draw()
        player.draw()
        if not konum4:
            player.pos = (390,80) # oyuncu konumu
            slime_1.pos = (390,75)
            konum4 = True
        if player.colliderect(gecit_3):
            k_icon3.draw()
        if player.colliderect(gecit_3) and keyboard.k: # eger portala degiyor ve k ye basıyorsa çıkı
            screen_5 = False

        if orumcek_durum and screen_5:   # ORUMCEGE DEGINCE
            savas()
            orumcek_savas.draw()
            slime_1_savas.draw()
            screen.draw.text(f"KATLETME ODULU: GOLD +35, LEVEL +45", (400,370), fontsize =15, color="yellow")

            screen.draw.text(f"DORTGOZ ORUMCEK;  HEALT : {orumcek_can}\n DAMAGE : {orumcek_guc}", (120,40), fontsize=14, color="black") 
            screen.draw.text(f"EVCIL SLIME; HEALT : {slime1_can}\n DAMAGE: {slime1_guc}", (390,150), fontsize=16, color="black")
            savas_ani = True

            if keyboard.space and ust_el_icon.pos == (410,260): # RUN 
                    player.pos = (200,200)
                    savas_ani = False

            if orumcek_can <= 0:
                slime1_level+=45 # level 2 art
                gold+=35
                kafatasi+=1
                player.pos = (130,200) # konuma don
                orumcek_can+=130 # iskelet yeniden dirilt
                savas_ani = False # klavye kontrolu gel
                slime1_can+=22

            if keyboard.space and ust_el_icon.pos == (170,260) and not space_durum: #DAMAGE BASINCA
                    
        
                space_durum = True # SAVAS BASLANDIGINDA SPACE KULLANILAMAZ KI SLİME DAHA FAZLA UZAGA GİTMESİN

                clock.schedule_unique(slime1_yaklas, 0.3)  
                clock.schedule_unique(slime1_orumcek_vur, 0.8)  
                clock.schedule_unique(slime1_geridon, 1.5)  

                clock.schedule_unique(orumcek_yaklas, 2)
                clock.schedule_unique(orumcek_vur, 2.5)
                clock.schedule_unique(orumcek_geridon, 3)

                clock.schedule_unique(space, 3.2) # SAVAS ANİMASYONU BİTİNCE SPACE YENİDEN KULLANILABİLSİN
                




        if dusman_base3: # PORTAL 3 DE DUSMAN BASEİNE GİRDİGİNDE
            screen.blit("siyah", (0,0))
            screen.blit("game_screen_9", (200,0))
            gecit2_3.draw()
            orumcek_boss.draw()
            orumcek_boss_seviye_bar.draw()
            slime_1.draw()
            player.draw()
            if player.colliderect(gecit2_3) and keyboard.k:
                dusman_base3 = False

            if player.colliderect(orumcek_boss): # ORUMCEK BOSS A DEGINCE
                savas()
                orumcek_boss_savas.draw()
                slime_1_savas.draw()
                screen.draw.text(f"KATLETME ODULU: GOLD +40, LEVEL +50, +YENI KOSTUM", (400,370), fontsize =15, color="yellow")

                screen.draw.text(f"TERBIYESIZ ORUMCEK;  HEALT : {orumcek_boss_can}\n DAMAGE : {orumcek_boss_guc}", (120,40), fontsize=14, color="black") 
                screen.draw.text(f"EVCIL SLIME; HEALT : {slime1_can}\n DAMAGE: {slime1_guc}", (390,150), fontsize=16, color="black")
                savas_ani = True

            if keyboard.space and ust_el_icon.pos == (410,260): # RUN 
                player.pos = (200,200)
                savas_ani = False

            if orumcek_boss_can <= 0:
                slime1_level+=50 # level 2 art
                gold+=40
                kafatasi+=1
                player.pos = (130,200) # konuma don
                orumcek_boss_can+=10 # iskelet yeniden dirilt
                savas_ani = False # klavye kontrolu gel
                slime_1.image = "slime_3"
                slime_1_savas.image = "slime_3"
                slime1_can+=25

            if keyboard.space and ust_el_icon.pos == (170,260) and not space_durum: #DAMAGE BASINCA
                    
        
                space_durum = True # SAVAS BASLANDIGINDA SPACE KULLANILAMAZ KI SLİME DAHA FAZLA UZAGA GİTMESİN

                clock.schedule_unique(slime1_yaklas, 0.3)  
                clock.schedule_unique(slime1_orumcek_boss_vur, 0.8)  
                clock.schedule_unique(slime1_geridon, 1.5)  

                clock.schedule_unique(orumcek_boss_yaklas, 2)
                clock.schedule_unique(orumcek_boss_vur, 2.5)
                clock.schedule_unique(orumcek_boss_geridon, 3)

                clock.schedule_unique(space, 3.2) # SAVAS ANİMASYONU BİTİNCE SPACE YENİDEN KULLANILABİLSİN
                








    if screen_6: # 4 Portala gectiginde
        screen.blit("game_screen_6", (0,0))
        gecit_4.draw()
        gecit2_4.draw()
        slime_1.draw()
        player.draw()
        if not konum5:
            player.pos =(600,170) # oyuncu konumu
            slime_1.pos = (600,165)
            konum5 = True
        if player.colliderect(gecit_4): # portala degiyorsa k ikonu cıksın
            k_icon4.draw()
        if player.colliderect(gecit_4) and keyboard.k: # hem degiyor hem k ye basıyorsa portaldan cıksın
            screen_6 = False


        if dusman_base4: #PORTAL 4 DE DUSMAN BASEİNE GİRİNCE
            screen.blit("siyah", (0,0))
            screen.blit("game_screen_10", (200,0))
            gecit2_4.draw()
            iskelet_boss.draw()
            iskelet_boss_seviye_bar.draw()
            slime_1.draw()
            player.draw()
            if player.colliderect(gecit2_4) and keyboard.k: # PORTAL 4 DE BASE GİRMİSSE VE BASE DEGIYORSA K YE BASARAK CIKSIN
                dusman_base4 = False

            if player.colliderect(orumcek_boss): # ISKELET BOSS A DEGINCE
                savas()
                iskelet_boss_savas.draw()
                slime_1_savas.draw()
                screen.draw.text(f"KATLETME ODULU: GOLD +100, LEVEL +100", (400,370), fontsize =15, color="yellow")

                screen.draw.text(f"BOSS;  HEALT : {iskelet_boss_can}\n DAMAGE : {iskelet_boss_guc}", (120,40), fontsize=14, color="black") 
                screen.draw.text(f"EVCIL SLIME; HEALT : {slime1_can}\n DAMAGE: {slime1_guc}", (390,150), fontsize=16, color="black")
                savas_ani = True

            if keyboard.space and ust_el_icon.pos == (410,260): # RUN 
                player.pos = (200,200)
                savas_ani = False

            if iskelet_boss_can <= 0:
                slime1_level+=100 # level 2 art
                gold+=100
                kafatasi+=1
                player.pos = (130,200) # konuma don
                iskelet_boss_can+=190 # iskelet yeniden dirilt
                savas_ani = False # klavye kontrolu gel
                slime1_can+=30

            if keyboard.space and ust_el_icon.pos == (170,260) and not space_durum: #DAMAGE BASINCA
                    
        
                space_durum = True # SAVAS BASLANDIGINDA SPACE KULLANILAMAZ KI SLİME DAHA FAZLA UZAGA GİTMESİN

                clock.schedule_unique(slime1_yaklas, 0.3)  
                clock.schedule_unique(slime1_iskelet_boss_vur, 0.8)  
                clock.schedule_unique(slime1_geridon, 1.5)  

                clock.schedule_unique(iskelet_boss_yaklas, 2)
                clock.schedule_unique(iskelet_boss_vur, 2.5)
                clock.schedule_unique(iskelet_boss_geridon, 3)

                clock.schedule_unique(space, 3.2) # SAVAS ANİMASYONU BİTİNCE SPACE YENİDEN KULLANILABİLSİN
                

            


    screen.blit("level_bar", (10,295))
    slime1_icon.draw()


    kilic1_icon.draw()


    xp_icon1.draw()

    can_icon.draw()


    gold_icon.draw()

    iksir_icon.draw()

    kafatasi_icon.draw()

    damage_iksir_ikon_bar2.draw()

    screen.draw.text(f":   {slime1_guc}",(90,335), fontsize=19, color="white") #SLİME GUC RAKAMI

    screen.draw.text(f":   {slime1_xp}", (90,370), fontsize=19, color="green") #SLİME XP RAKAMI

    screen.draw.text(f":   {slime1_can}", (90,305), fontsize=19, color="red") #SLİME CAN RAKAMI


    screen.draw.text(f"{gold}", (170,315), fontsize=20, color="gold")
    screen.draw.text(f"{iksir}", (265,315), fontsize=20, color="red")
    screen.draw.text(f"{kafatasi}", (335,315), fontsize=20, color="grey")
    screen.draw.text(f"{damage_iksir}", (220,315), fontsize=20, color="brown")

    screen.draw.text(f"EVCIL SLIME XP: {slime1_level}/ MAX {slime1_level_max}", (160,363), fontsize =20, color="black")

    if slime_1_savas.colliderect(iskelet1_savas) and slime_1_savas.pos == (420,110): # SAVAS ESNASINDA DUSMANA VURULDUGUNDA CIKACAK YAZİ
        screen.draw.text(f"DAMAGE {slime1_guc}",(380,70), fontsize=20, color="blue")

    if iskelet1_savas.colliderect(slime_1_savas) and slime_1_savas.pos == (200,190): # SAVAS ESNASINDA SLİME DARBE YİYİNCE CIKACAK YAZİ
        screen.draw.text(f"DAMAGE -{iskelet1_guc}", (100,150), fontsize=20, color="red")

    if canavar1_savas.colliderect(slime_1_savas) and slime_1_savas.pos == (200,190): # SAVAS ESNASINDA SLİME DARBE YİYİNCE CIKACAK YAZİ
        screen.draw.text(f"DAMAGE -{canavar1_guc}", (100,150), fontsize=20, color="red")

    if canavar2_savas.colliderect(slime_1_savas) and slime_1_savas.pos == (200,190): # SAVAS ESNASINDA SLİME DARBE YİYİNCE CIKACAK YAZİ
        screen.draw.text(f"DAMAGE -{canavar2_guc}", (100,150), fontsize=20, color="red")

    if kaktus_savas.colliderect(slime_1_savas) and slime_1_savas.pos == (200,190): # SAVAS ESNASINDA SLİME DARBE YİYİNCE CIKACAK YAZİ
        screen.draw.text(f"DAMAGE -{kaktus_guc}", (100,150), fontsize=20, color="red")

    if kaktus_boss_savas.colliderect(slime_1_savas) and slime_1_savas.pos == (200,190): # SAVAS ESNASINDA SLİME DARBE YİYİNCE CIKACAK YAZİ
        screen.draw.text(f"DAMAGE -{kaktus_boss_guc}", (100,150), fontsize=20, color="red")

    if vampir_savas.colliderect(slime_1_savas) and slime_1_savas.pos == (200,190): # SAVAS ESNASINDA SLİME DARBE YİYİNCE CIKACAK YAZİ
        screen.draw.text(f"DAMAGE -{vampir_guc}", (100,150), fontsize=20, color="red")


    if vampir_boss_savas.colliderect(slime_1_savas) and slime_1_savas.pos == (200,190): # SAVAS ESNASINDA SLİME DARBE YİYİNCE CIKACAK YAZİ
        screen.draw.text(f"DAMAGE -{vampir_boss_guc}", (100,150), fontsize=20, color="red")

    if orumcek_savas.colliderect(slime_1_savas) and slime_1_savas.pos == (200,190): # SAVAS ESNASINDA SLİME DARBE YİYİNCE CIKACAK YAZİ
        screen.draw.text(f"DAMAGE -{orumcek_guc}", (100,150), fontsize=20, color="red")

    if orumcek_boss_savas.colliderect(slime_1_savas) and slime_1_savas.pos == (200,190): # SAVAS ESNASINDA SLİME DARBE YİYİNCE CIKACAK YAZİ
        screen.draw.text(f"DAMAGE -{orumcek_boss_guc}", (100,150), fontsize=20, color="red")

    if iskelet_boss_savas.colliderect(slime_1_savas) and slime_1_savas.pos == (200,190): # SAVAS ESNASINDA SLİME DARBE YİYİNCE CIKACAK YAZİ
        screen.draw.text(f"DAMAGE -{iskelet_boss_guc}", (100,150), fontsize=20, color="red")


    if item: # İTEM BARI ACILDIGINDA
        item_bar.draw()
        damage_iksir_icon.draw()
        iksir_icon_bar.draw()
        screen.draw.text(f"{iksir}", (450,325), color="red")
        screen.draw.text(f"{damage_iksir}", (550,325), color="brown")
        e_icon.draw()


    
    if tuccar_item_durum:
        tuccar_item_bar.draw()
        tuccar_item_bar2.draw()
        damage_iksir_ikon_bar.draw()
        iksir_ikon_bar.draw()
        screen.draw.text("$60", (555,295), fontsize=15, color="gold")
        screen.draw.text("$10", (600,295), fontsize=15, color="gold")
        screen.draw.text("Damage Iksiri 60\nCan Iksiri 10 Gold",(465,370), color="black", fontsize=15)
        seviye_bilgi.draw()
        screen.draw.text("SEVİYE ATLAMA\nODULLERI:\nGOLD + 15\nSLIME GUC + 5\nSLIME CAN +10", (488,200), fontsize=13, color="black")
        
        sag_el_icon2.draw()
        if keyboard.right:
            sag_el_icon2.pos = (570,300)
        if keyboard.left:
            sag_el_icon2.pos = (520,300)

    
    if bitti:
        screen.blit("siyah", (0,0))
        screen.draw.text("SLIME'IN CANI BITTI\nKAYBETTIN!\n\n\nTEKRAR DENEMEK ICIN OYUNU YENIDEN BASLAT", (100,155), fontsize=30, color="red")

    
    



tuccar_item_durum = False
bitti = False
def update():
    global tuccar_item_durum, screen_2,damage_iksir,gold, iksir,slime1_can, slime1_guc, kafatasi, bitti
    if keyboard.p:
        print(player.x, player.y)
    game_screen2()
    savas_ekrani1()
    slime1_takip()
    seviye_sistemi()
    klavye()
    if screen_2 == False: # EGER PENCERE SOLUNA CIKARSA PORTALLAR DEVRE DISI OLSUN
        portal1()
        portal2()
        portal3()
        portal4()

    if player.colliderect(tuccar) and not screen_2 and not screen_3 and not screen_4 and not screen_5 and not screen_6:
        tuccar_item_durum = True
    if not player.colliderect(tuccar):
        tuccar_item_durum = False

    if tuccar_item_durum and sag_el_icon2.pos == (520,300) and keyboard.space and gold >= 60: # TUCCAR DAMAGE İTEMİ ALINCAGINDA
        time.sleep(0.5)
        damage_iksir+=1
        gold-=60

    if tuccar_item_durum and sag_el_icon2.pos == (570,300) and keyboard.space and gold >= 10: # TUCCARDAN İKSİR ALINCA
        time.sleep(0.5)
        iksir+=1
        gold-=10

    if item and ust_el_icon2.pos == (420,380) and keyboard.e and iksir >= 1: # savasta can itemi secildiginde
        time.sleep(0.3)
        slime1_can+=10
        iksir-=1

    if item and ust_el_icon2.pos == (520,375) and keyboard.e and damage_iksir >= 1: # savasta damage itemi secildiginde
        time.sleep(0.3)
        slime1_guc+=2
        damage_iksir-=1

    
    if slime1_can <= 0:
        bitti = True
      
        
        

        





def game_screen2():
    global screen_2, screen_3, screen_5

    if player.right < 0 and screen_3 == False and screen_4 == False and screen_5 == False and not screen_6 and not dusman_base1: # OYUNCU EKRANIN SOLUNDAN CIKARSA SCREEN2 CALISSIN ve portallardan birinde degilsek calıssın
        screen_2 = True
    if player.left > WIDTH: #eger yeniden cıkarsa eski haline donsun
        screen_2 = False

kaktus_durum = False
kaktus_boss_durum = False
def portal1():
    global m_bas, m_bas2, m_bas2, m_bas3, screen_3, dusman_base1, kaktus_durum, kaktus_boss_durum

    if player.colliderect(gecit_1): #yaklasınca m ye bas iconu cıksın
        m_bas = True
    if not player.colliderect(gecit_1):
        m_bas = False

    if player.colliderect(gecit_1) and keyboard.m and screen_4 == False and screen_5 == False and not screen_6 and not screen_3 and not dusman_base1: #eger portal1 e temas ediyorsak m ye basılıyorsa ve portal 2 False ise
        screen_3 = True #portal acılsın

    if player.colliderect(gecit2_1) and keyboard.m and screen_3: # eger gecit2_1 e dokunuyor ve m ye basıyorsa dusman base e gecsin
        dusman_base1 = True

    if player.colliderect(kaktus) and screen_3:
        kaktus_durum = True
    
    if not player.colliderect(kaktus):
        kaktus_durum = False

    if dusman_base1 and player.colliderect(kaktus_boss):
        kaktus_boss_durum = True

    if not player.colliderect(kaktus_boss):
        kaktus_boss_durum = False
        
    

    

vampir_durum = False
def portal2():
    global m_bas2, screen_4, dusman_base1, dusman_base2, vampir_durum

    if player.colliderect(gecit_2): #temas edince m iconu cıksın
        m_bas2 = True
    if not player.colliderect(gecit_2):
        m_bas2 = False

    if player.colliderect(gecit_2) and keyboard.m and screen_3 == False and screen_5 == False and not screen_6 and not dusman_base1: #eger temas ediyor, m ye basıyor ve portal1 false ise
        screen_4 = True # portal 2 ye girsin

    if player.colliderect(gecit2_2) and keyboard.m and screen_4: # EGER PORTAL 2 DE DUSMAN BASE E YAKLASIP M YE BASARSA DUSMAN BASE TRUE OLSUN
        dusman_base2 = True

    if player.colliderect(vampir) and screen_4:
        vampir_durum = True
    
    if not player.colliderect(vampir):
        vampir_durum = False

orumcek_durum = False
def portal3():
    global m_bas3, screen_5, dusman_base1, dusman_base3, orumcek_durum
    if player.colliderect(gecit_3): # eger portala degiyorsa
        m_bas3 = True # m iconu goster
    if not player.colliderect(gecit_3): # degmisyorsa gosterme
        m_bas3 = False

    if player.colliderect(gecit_3) and keyboard.m and not screen_4 and not screen_5 and not screen_6 and not screen_3 and not dusman_base1: # eger degiyor ve me ye basıyorsa portal 3 e gec
        screen_5 = True

    if player.colliderect(gecit2_3) and keyboard.m and screen_5: # PORTAL 3 DE DUSMAN BASE E YAKLASIP M YE BASARSA GİRSİN
        dusman_base3 = True


    if player.colliderect(orumcek) and screen_5:
        orumcek_durum = True
    
    if not player.colliderect(orumcek):
        orumcek_durum = False

iskelet_boss_durum = False
def portal4():
    global m_bas4, screen_6, dusman_base1, dusman_base4, iskelet_boss_durum

    if player.colliderect(gecit_4):
        m_bas4 = True  # eger temas ediyorsa m ikonu cıksın
    if not player.colliderect(gecit_4):
        m_bas4 = False # degmiyorsa cıkmasın

    if player.colliderect(gecit_4) and keyboard.m and not screen_3 and not screen_4 and not screen_5 and not dusman_base1: # degiyor, me ye basıyor ve diger portallarda degilse portal4 e girsin
        screen_6 = True

    if player.colliderect(gecit2_4) and keyboard.m and screen_6:
        dusman_base4 = True

    if player.colliderect(iskelet_boss) and screen_5:
        iskelet_boss_durum = True
    
    if not player.colliderect(iskelet_boss):
        iskelet_boss_durum = False

       ##########################################


def savas(): # DUSMANA TEMAS EDİNCE GELEN SAVAS EKRANI
    global savas_bitir, savas_ani, el_ikon, item
    screen.blit("siyah", (0,0))
    screen.blit("fight_screen", (1,-35))
    savas_buton_1.draw()
    savas_buton_2.draw()
    savas_buton_3.draw()

    screen.draw.text("DAMAGE", (138,233), fontsize=17, color="black")
    screen.draw.text("ITEM", (270,233), fontsize=17, color="black")
    screen.draw.text("RUN", (390,233), fontsize=17, color="black")

    savas_buton_kilic.draw()
    savas_buton_item.draw()
    savas_buton_run.draw()

    
    if el_ikon:
        ust_el_icon.draw()
        if keyboard.left:
            ust_el_icon.pos = (170,260)

        if keyboard.down:
            ust_el_icon.pos = (290, 260)  # el ikonu

        if keyboard.right:
            ust_el_icon.pos = (410,260)

        if keyboard.space and ust_el_icon.pos == (290,260): # EL İKONU İTEMDEYKEN
            time.sleep(0.4)
            item = True
            el_ikon = False

        

    if item: # itemdeyken el ikonu
        ust_el_icon2.draw()
        if keyboard.right:
            ust_el_icon2.pos = (520,375)
        if keyboard.left:
            ust_el_icon2.pos = (420,380)
        


        if keyboard.up: # eger itemmdeyken carpıya basılırsa
            item = False
            el_ikon = True

    



def savas_ekrani1():
    global savas_ani,slime1_level,space_durum,canavar1_can,canavar2_can,slime1_kostum,item,iskelet2_can, canavar2_guc, oyuncu_konum, slime1_guc, slime1_can, savas_bitir, iskelet1_can, iskelet1_guc, gold,kafatasi # savas bitir k ye basılırsa true olur ve kosullardan biri saglanamayarak savas biter

    if player.colliderect(iskelet1) and screen_2 and not savas_bitir: # EGER EKRANIN YANINA CIKAR VE ISKELET1 DEGERSE
       
        savas_ani = True # TRUE OLDUGU ZAMAN KLAVYE KONTROLU GİDER
        savas() # savas ekranı gelsin
        iskelet1_savas.draw()
        slime_1_savas.draw()
        screen.draw.text(f"KATLETME ODULU: GOLD +5, LEVEL +5", (400,370), fontsize =15, color="yellow")

        screen.draw.text(f"ISKELET;  HEALT : {iskelet1_can}\n DAMAGE : {iskelet1_guc}", (120,40), fontsize=16, color="black") # iskelet can guc
        screen.draw.text(f"EVCIL SLIME; HEALT : {slime1_can}\n DAMAGE: {slime1_guc}", (390,150), fontsize=16, color="black")# slime 1 durum

        if keyboard.space and ust_el_icon.pos == (170,260) and not space_durum: # el damage de iken basıldıgında
            vurma_animasyon_iskelet1()


        if iskelet1_can <= 0: # eger iskeletin canı sıfıra inerse
            slime1_level+=5 # level 2 art
            gold+=5
            kafatasi+=1
            player.pos = (530,190) # konuma don
            iskelet1_can+=20 # iskelet yeniden dirilt
            savas_ani = False # klavye kontrolu gel
            slime1_can+=2
           

    
        


    if player.colliderect(iskelet2) and screen_2 and not savas_bitir: # EGER EKRANIN YANINA CIKAR VE İSKELET2 DEGERSE
        savas()
        savas_ani = True
        iskelet1_savas.draw()
        slime_1_savas.draw()
        screen.draw.text(f"KATLETME ODULU: GOLD +8, LEVEL +7", (400,370), fontsize =15, color="yellow")

        screen.draw.text(f"ISKELET;  HEALT : {iskelet2_can}\n DAMAGE : {iskelet2_guc}", (120,40), fontsize=16, color="black") # iskelet can guc
        screen.draw.text(f"EVCIL SLIME; HEALT : {slime1_can}\n DAMAGE: {slime1_guc}", (390,150), fontsize=16, color="black")# slime 1 durum

        if keyboard.space and ust_el_icon.pos == (170,260) and not space_durum: # el damage de iken basıldıgında
            vurma_animasyon_iskelet2()


        if iskelet2_can <= 0: # eger iskeletin canı sıfıra inerse
            slime1_level+=7 # level 2 art
            gold+=8
            kafatasi+=1
            player.pos = (530,190) # konuma don
            iskelet2_can+=20 # iskelet yeniden dirilt
            savas_ani = False # klavye kontrolu gel
            slime1_can+=2
        


    if player.colliderect(canavar1) and screen_2 and not savas_bitir: # EGER EKRANIN YANINA CIKAR VE CANAVAR1 DEGERSE

        savas()
        savas_ani = True
        canavar1_savas.draw()
        slime_1_savas.draw()
        screen.draw.text(f"KATLETME ODULU: GOLD +10, LEVEL +10", (400,370), fontsize =15, color="yellow")

        screen.draw.text(f"OFKELI DEV;  HEALT : {canavar1_can}\n DAMAGE : {canavar1_guc}", (120,40), fontsize=16, color="black") # iskelet can guc
        screen.draw.text(f"EVCIL SLIME; HEALT : {slime1_can}\n DAMAGE: {slime1_guc}", (390,150), fontsize=16, color="black")# slime 1 durum

        if keyboard.space and ust_el_icon.pos == (170,260) and not space_durum:
            vurma_animasyon_canavar1()
        
        if canavar1_can <= 0: # canavar oldugunde
            slime1_level+=10 # level 2 art
            gold+=10
            kafatasi+=1
            player.pos = (530,190) # konuma don
            canavar1_can+=40 # iskelet yeniden dirilt
            savas_ani = False # klavye kontrolu gel
            slime1_can+=8



    if player.colliderect(canavar2) and screen_2 and not savas_bitir: # EGER EKRANIN YANINA CIKAR VE CANAVAR2 DEGERSE
        savas()
        savas_ani = True
        canavar2_savas.draw()
        slime_1_savas.draw()
        screen.draw.text(f"KATLETME ODULU: GOLD +15, LEVEL +14", (400,370), fontsize =15, color="yellow")

        screen.draw.text(f"OBEZ DEV;  HEALT : {canavar2_can}\n DAMAGE : {canavar2_guc}", (120,40), fontsize=16, color="black") # iskelet can guc
        screen.draw.text(f"EVCIL SLIME; HEALT : {slime1_can}\n DAMAGE: {slime1_guc}", (390,150), fontsize=16, color="black")# slime 1 durum

        if keyboard.space and ust_el_icon.pos == (170,260) and not space_durum:
            vurma_animasyon_canavar2()

        if canavar2_can <= 0: # eger iskeletin canı sıfıra inerse
            slime1_level+=14 # level 2 art
            gold+=15
            kafatasi+=1
            player.pos = (530,190) # konuma don
            canavar2_can+=50 # iskelet yeniden dirilt
            savas_ani = False # klavye kontrolu gel


        
    

    if keyboard.space and ust_el_icon.pos == (410,260) and not tuccar_item_durum: # eger k ye basarsa ve el ikonu rundaysa savastayken karakterin konumu degissin ve degmedigi icin savas bitsin
        player.pos = (530,190)
        savas_ani = False
        item = False



def vurma_animasyon_iskelet1():
        global space_durum

        space_durum = True # SAVAS BASLANDIGINDA SPACE KULLANILAMAZ KI SLİME DAHA FAZLA UZAGA GİTMESİN

        clock.schedule_unique(slime1_yaklas, 0.3)   #0.5 saniye sonra yaklasıcak dusmana
        clock.schedule_unique(slime1_iskelet1_vur, 0.8)  #yaklasınca 1 saniye beklicek ve vurcak
        clock.schedule_unique(slime1_geridon, 1.5)  # vurduktan 2 saniye sonra da geri dönecek

        clock.schedule_unique(iskelet1_yaklas, 2)
        clock.schedule_unique(iskelet1_vur, 2.5)
        clock.schedule_unique(iskelet1_geridon, 3)

        clock.schedule_unique(space, 3.2) # SAVAS ANİMASYONU BİTİNCE SPACE YENİDEN KULLANILABİLSİN


def vurma_animasyon_canavar1():
        global space_durum
        
        space_durum = True # SAVAS BASLANDIGINDA SPACE KULLANILAMAZ KI SLİME DAHA FAZLA UZAGA GİTMESİN

        clock.schedule_unique(slime1_yaklas, 0.3)  
        clock.schedule_unique(slime1_canavar1_vur, 0.8)  
        clock.schedule_unique(slime1_geridon, 1.5)  

        clock.schedule_unique(canavar1_yaklas, 2)
        clock.schedule_unique(canavar1_vur, 2.5)
        clock.schedule_unique(canavar1_geridon, 3)

        clock.schedule_unique(space, 3.2) # SAVAS ANİMASYONU BİTİNCE SPACE YENİDEN KULLANILABİLSİN

def vurma_animasyon_canavar2():
    global space_durum
        
    space_durum = True # SAVAS BASLANDIGINDA SPACE KULLANILAMAZ KI SLİME DAHA FAZLA UZAGA GİTMESİN

    clock.schedule_unique(slime1_yaklas, 0.3)  
    clock.schedule_unique(slime1_canavar2_vur, 0.8)  
    clock.schedule_unique(slime1_geridon, 1.5)  

    clock.schedule_unique(canavar2_yaklas, 2)
    clock.schedule_unique(canavar2_vur, 2.5)
    clock.schedule_unique(canavar2_geridon, 3)

    clock.schedule_unique(space, 3.2) # SAVAS ANİMASYONU BİTİNCE SPACE YENİDEN KULLANILABİLSİN

def vurma_animasyon_iskelet2():
    global space_durum
        
    space_durum = True # SAVAS BASLANDIGINDA SPACE KULLANILAMAZ KI SLİME DAHA FAZLA UZAGA GİTMESİN

    clock.schedule_unique(slime1_yaklas, 0.3)  
    clock.schedule_unique(slime1_iskelet2_vur, 0.8)  
    clock.schedule_unique(slime1_geridon, 1.5)  

    clock.schedule_unique(iskelet1_yaklas, 2)
    clock.schedule_unique(iskelet1_vur, 2.5)
    clock.schedule_unique(iskelet1_geridon, 3)

    clock.schedule_unique(space, 3.2) # SAVAS ANİMASYONU BİTİNCE SPACE YENİDEN KULLANILABİLSİN



def vurma_animasyon_kaktus():
    global space_durum
        
    space_durum = True # SAVAS BASLANDIGINDA SPACE KULLANILAMAZ KI SLİME DAHA FAZLA UZAGA GİTMESİN

    clock.schedule_unique(slime1_yaklas, 0.3)  
    clock.schedule_unique(slime1_iskelet2_vur, 0.8)  
    clock.schedule_unique(slime1_geridon, 1.5)  

    clock.schedule_unique(kaktus_yaklas, 2)
    clock.schedule_unique(kaktus_vur, 2.5)
    clock.schedule_unique(kaktus_geridon, 3)

    clock.schedule_unique(space, 3.2) # SAVAS ANİMASYONU BİTİNCE SPACE YENİDEN KULLANILABİLSİN







def slime1_yaklas():
    slime_1_savas.x+=90
    slime_1_savas.y-=80  #SLİME1 YAKLASMA FONKSİYONU #420,110
    slime_1_savas.x+=130

def slime1_vur(parametre):
    global iskelet1_can, canavar1_can,canavar2_can,iskelet2_can, kaktus_can,kaktus_boss_can,vampir_can,vampir_boss_can,orumcek_can,orumcek_boss_can,agac_can,agac_boss_can,iskelet_boss_can #SLİME1 VURMa
    if parametre == 1:
        iskelet1_can-=slime1_guc
    if parametre == 2:
        canavar1_can-=slime1_guc
    if parametre == 3:
        canavar2_can-=slime1_guc
    if parametre == 4:
        iskelet2_can-=slime1_guc
    if parametre == 5:
        kaktus_can-=slime1_guc
    if parametre == 6:
        kaktus_boss_can-=slime1_guc
    if parametre == 7:
        vampir_can-=slime1_guc
    if parametre == 8:
        vampir_boss_can-=slime1_guc
    if parametre == 9:
        orumcek_can-=slime1_guc
    if parametre == 10:
        orumcek_boss_can-=slime1_guc
    if parametre == 11:
        agac_can-=slime1_guc
    if parametre == 12:
        agac_boss_can-=slime1_guc
    if parametre == 13:
        iskelet_boss_can-=slime1_guc

def slime1_geridon():
    slime_1_savas.pos = (200,190) #SLİME1 GERİ DONME

    #####################



def iskelet1_yaklas():
    iskelet1_savas.x-=150
    iskelet1_savas.y+=80
    iskelet1_savas.x-=60

def iskelet1_vur():
    global slime1_can
    slime1_can-=iskelet1_guc

def iskelet1_geridon():
    iskelet1_savas.pos = (480,90)



def canavar1_yaklas():
    canavar1_savas.x-=150
    canavar1_savas.y+=80
    canavar1_savas.x-=60

def canavar1_vur():
    global slime1_can
    slime1_can-=canavar1_guc

def canavar1_geridon():
    canavar1_savas.pos = (480,90)


def canavar2_yaklas():
    canavar2_savas.x-=150
    canavar2_savas.y+=80
    canavar2_savas.x-=70

def canavar2_vur():
    global slime1_can
    slime1_can-=canavar2_guc

def canavar2_geridon():
    canavar2_savas.pos = (480,90)


def kaktus_yaklas():
    kaktus_savas.x-=150
    kaktus_savas.y+=80
    kaktus_savas.x-=60


def kaktus_vur():
    global slime1_can
    slime1_can-=kaktus_guc


def kaktus_geridon():
    kaktus_savas.pos = (480,90)



def kaktus_boss_yaklas():
    kaktus_boss_savas.x-=150
    kaktus_boss_savas.y+=80
    kaktus_boss_savas.x-=60

def kaktus_boss_vur():
    global slime1_can
    slime1_can-=kaktus_boss_guc

def kaktus_boss_geridon():
    kaktus_boss_savas.pos = (480,90)


def vampir_yaklas():
    vampir_savas.x-=150
    vampir_savas.y+=80
    vampir_savas.x-=60

def vampir_vur():
    global slime1_can
    slime1_can-=vampir_guc

def vampir_geridon():
    vampir_savas.pos = (480,90)


def vampir_boss_yaklas():
    vampir_boss_savas.x-=150
    vampir_boss_savas.y+=80
    vampir_boss_savas.x-=60

def vampir_boss_vur():
    global slime1_can
    slime1_can-=vampir_boss_guc

def vampir_boss_geridon():
    vampir_boss_savas.pos = (480,90)


def orumcek_yaklas():
    orumcek_savas.x-=150
    orumcek_savas.y+=80
    orumcek_savas.x-=60

def orumcek_vur():
    global slime1_can
    slime1_can-=orumcek_guc

def orumcek_geridon():
    orumcek_savas.pos = (480,90)


def orumcek_boss_yaklas():
    orumcek_boss_savas.x-=150
    orumcek_boss_savas.y+=80
    orumcek_boss_savas.x-=60

def orumcek_boss_vur():
    global slime1_can
    slime1_can-=orumcek_boss_guc

def orumcek_boss_geridon():
    orumcek_boss_savas.pos = (480,90)

def iskelet_boss_yaklas():
    iskelet_boss_savas.x-=150
    iskelet_boss_savas.y+=80
    iskelet_boss_savas.x-=60

def iskelet_boss_vur():
    global slime1_can
    slime1_can-=iskelet_boss_guc

def iskelet_boss_geridon():
    iskelet_boss_savas.pos = (480,90)












    








slime1_iskelet1_vur = lambda: slime1_vur(1) # slime1_vur 1 parametresini birlestirir 
slime1_canavar1_vur = lambda: slime1_vur(2)
slime1_canavar2_vur = lambda: slime1_vur(3)
slime1_iskelet2_vur = lambda: slime1_vur(4)

slime1_kaktus_vur = lambda: slime1_vur(5)
slime1_kaktus_boss_vur = lambda: slime1_vur(6)

slime1_vampir_vur = lambda: slime1_vur(7)
slime1_vampir_boss_vur = lambda: slime1_vur(8)

slime1_orumcek_vur = lambda: slime1_vur(9)
slime1_orumcek_boss_vur = lambda: slime1_vur(10)

slime1_agac_vur = lambda: slime1_vur(11)
slime1_agac_boss_vur = lambda: slime1_vur(12)

slime1_iskelet_boss_vur = lambda: slime1_vur(13)






############################################################################################
    
def space(): # savas anında space devamlı basılmaması icin
    global space_durum
    space_durum = False


def seviye_sistemi():
    global slime1_guc, slime1_level, slime1_level_max, gold, kafatasi, slime1_xp, slime1_can

    if slime1_level >= slime1_level_max: # EGER LEVEL MAX LEVELE ULASMISSA
        slime1_guc+=5 # SLİME GUCU ARTSIN
        gold+=15 # GOLD ARTSIN
        slime1_level_max+=10 # MAX LEVEL SINIRI ARTSIN
        slime1_level = 0 # LEVEL SIFIRLANSIN
        slime1_xp+=1 #XP ARTSIN
        kafatasi+=1
        slime1_can+=10



def slime1_takip():
    if slime_1.x > player.x:
        slime_1.x-=2.5
    if slime_1.x < player.x:
        slime_1.x+=2.5 #SLİME IN OYUNCUYU TAKİP ETTİGİ KOD
    if player.y > slime_1.y:
        slime_1.y+=2.5
    if player.y < slime_1.y:
        slime_1.y-=2.5




def klavye():
    global savas_ani
    if not savas_ani:
        if keyboard.w:
            player.y-=3
            player.image = ("up_1")

        if keyboard.d:
            player.x+=3
            player.image = ("right_1")

        if keyboard.a:
            player.x-=3
            player.image = ("left_1")

        if keyboard.s:
            player.y+=3
            player.image = ("down_1")







pgzrun.go()
