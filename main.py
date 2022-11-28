import pygame  # impordime pygame mooduli
import random  # impordime random mooduli

pygame.init()  # käivitame pygame

# ekraani seaded
ekraanX, ekraanY = 640, 480  # määrame ekraani suuruse muutujad
ekraan = pygame.display.set_mode([ekraanX, ekraanY])  # määrame ekraani suuruse (väärtused muutujatest) ja omistame muutujasse ekraan
pygame.display.set_caption("Ülesanne 4: Objektide animeerimine")  # määrame ekraanie pealkirja
FPS = pygame.time.Clock()  # loome FPS muutuja ja omistame pygame kella väärtuse
taust = pygame.image.load("pildi_failid/bg_rally.jpg")  # muutuljale taust omistame pildifaili väärtuse

# autod
punane_auto = pygame.image.load("pildi_failid/f1_red.png")  # muutuljale punase_auto omistame pildifaili väärtuse
sinine_auto1 = pygame.image.load("pildi_failid/f1_blue.png")  # muutuljale sinine_auto_1 omistame pildifaili väärtuse
sinine_auto2 = pygame.image.load("pildi_failid/f1_blue.png")  # muutuljale sinine_auto_2 omistame pildifaili väärtuse

# autode kiirus, asukoht, punktid
punane_auto_X, punane_auto_Y = 300, 390  # määrame punase auto kordinaadid muutujatesse
sinine_auto1_X, sinine_auto1_Y = 175, random.uniform(50, 350)  # määrame sinise auto 1 kordinaadid muutujatesse, Y kordnaat võetakse suvalsielt vahemikus 50 - 350
sinine_auto2_X, sinine_auto2_Y = 425, random.uniform(50, 350)  # määrame sinise auto 2 kordinaadid muutujatesse, Y kordnaat võetakse suvalsielt vahemikus 50 - 350
kiirus_Y = 2  # määrame muutujale kiirus_Y väärtuse 2
punktid = 0  # määrame muutujale punktid väärtuse 0

# teksti font
font = pygame.font.Font(pygame.font.match_font('Arial'), 25)  # määrame muutujale "font" suuruseks 25 ja fondiks "Arial"

while True:  # nii kaua, kui tsükkel on tõene,
    for syndmus in pygame.event.get():  # sükkli muutujale omistatakse kõik pygame.event.get() väärtused
        if syndmus.type == pygame.QUIT:  # kui tsüklimuutuja syndmus tüüp võrdub pygame.QUIT
            pygame.quit()  # sulgeme pygame
            exit()  # lõpetame programmi

    FPS.tick(60)  # värskendame ekraani 60 korda sekundis
    tekst = font.render("Skoor: " + str(punktid), True, [255, 255, 255])  # omistame muutujale tekst väärtuseks sõne ja muutujast punktid oleva arvu ja värvime selle valgeks

    sinine_auto1_Y += kiirus_Y  # muutjale sinine_auto1_Y lisame muutuja kiirus_Y värtuse
    sinine_auto2_Y += kiirus_Y  # muutjale sinine_auto2_Y lisame muutuja kiirus_Y värtuse

    if sinine_auto1_Y > ekraanY:  # kui muutuja sinine_auto1_Y on suurem kui muutuja ekraanY, siis
        sinine_auto1_Y = random.uniform(-70, -500)  # muutujale sinine_auto1_Y omistame suvalise väärtuse vahemikus -50 ja -300
        punktid += 1  # muutjale punktid liidame juurde 1

    if sinine_auto2_Y > ekraanY:  # kui muutuja sinine_auto2_Y on suurem kui muutuja ekraanY, siis
        sinine_auto2_Y = random.uniform(-70, -500)  # muutujale sinine_auto2_Y omistame suvalise väärtuse vahemikus -50 ja -300
        punktid += 1  # muutjale punktid liidame juurde 1

    # asjade ekraanil kuvamine
    ekraan.blit(taust, [0, 0])  # kuvame ekraanil taustapildi faili kordinaatidega 0,0
    ekraan.blit(punane_auto, [punane_auto_X, punane_auto_Y])  # kuvame ekraanil punase auto mille kordinaadid võetakse muutujast
    ekraan.blit(sinine_auto1, (sinine_auto1_X, sinine_auto1_Y))  # kuvame ekraanil sinise auto 1 mille kordinaadid võetakse muutujast
    ekraan.blit(sinine_auto2, (sinine_auto2_X, sinine_auto2_Y))  # kuvame ekraanil sinise auto 2 mille kordinaadid võetakse muutujast
    ekraan.blit(tekst, [520, 200])  # kuvame ekraanil muutuja tekst väärtuse kordinaatidega 520,200
    pygame.display.flip()  # värskendame tervet ekraani