import pygame
#Все ректы

#Кот и его предметы
rect_plot = pygame.Rect(100, 5, 200, 70)
rect_cot = pygame.Rect(rect_plot.x, rect_plot.y, 167, 126)
rect_umbrella = pygame.Rect(160, 640, 125, 125)
rect_bucket = pygame.Rect(80, 710, 60, 60)

#Тучка и капля
rect_tuchka = pygame.Rect(50, 50, 150, 120)
rect_kaplu = pygame.Rect(rect_tuchka.x, rect_tuchka.y, 40, 40)

#Вода
rect_voda = pygame.Rect(0, 870, 1000, 30)
rect_obman_voda = pygame.Rect(0, 900, 1000, 100)


def viravnivanie():
    rect_voda.bottom = rect_obman_voda.top
    rect_plot.bottom = rect_voda.top+60
viravnivanie()

visibility = False
perevorot = False  # True - vpravo, False - vlevo
speed_x_tuchka = 6
speed_y_kaplu = 7


def zapusk():
    kaplu()
    tuchka()


def kaplu():
    rect_kaplu.centery += speed_y_kaplu


def tuchka():
    global speed_x_tuchka
    rect_tuchka.centerx += speed_x_tuchka
    if rect_tuchka.right > 1000:
        speed_x_tuchka = -speed_x_tuchka
        rect_tuchka.right = 1000
    if rect_tuchka.left <= 0:
        speed_x_tuchka = -speed_x_tuchka
        rect_tuchka.left = 0


def pravo():
    global perevorot
    perevorot = True
    # перемещение предметов
    rect_cot.x += 35
    rect_umbrella.x += 35
    rect_bucket.x += 35
    rect_plot.x += 35
    # граница
    if rect_bucket.x >= 940:
        rect_cot.x = 818
        rect_umbrella.x = 790
        rect_bucket.x = 940
        rect_plot.x = 800
    # переворачивание предметов
    if rect_umbrella.x >= rect_bucket.x:
        rect_umbrella.x -= 220
    if rect_cot.x >= rect_bucket.x:
        rect_cot.x -= 140
    if rect_cot.x >= rect_bucket.x:
            rect_plot.x -= 140


def levo():
    global perevorot
    perevorot = False

    # перемещение предметов
    rect_cot.x -= 35
    rect_umbrella.x -= 35
    rect_bucket.x -= 35
    rect_plot.x -= 35

    # граница
    if rect_bucket.x <= 0:
        rect_cot.x = 15
        rect_umbrella.x = 100
        rect_bucket.x = 0
        rect_plot.x = 0

    # переворачивание предметов
    if rect_umbrella.x <= rect_bucket.x:
        rect_umbrella.x += 220
    if rect_cot.x <= rect_bucket.x:
        rect_cot.x += 140
    if rect_cot.x <= rect_bucket.x:
            rect_plot.x += 140
