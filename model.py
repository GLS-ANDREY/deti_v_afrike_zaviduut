import pygame

visibility = False
perevorot = False  # True - vpravo, False - vlevo
speed_x_tuchka = 6
speed_y_kaplu = 7
popalo_kapel = 0

# Все ректы

# Кот и его предметы
rect_plot = pygame.Rect(100, 5, 200, 70)
rect_cot = pygame.Rect(rect_plot.x, rect_plot.y, 167, 126)
rect_umbrella = pygame.Rect(185, 675, 125, 125)
rect_bucket = pygame.Rect(80, 750, 60, 60)

# Тучка и капля
rect_tuchka = pygame.Rect(50, 50, 150, 120)
rect_kaplu = pygame.Rect(rect_tuchka.x, rect_tuchka.y, 40, 40)

# Вода
rect_voda = pygame.Rect(0, 870, 1000, 30)
rect_obman_voda = pygame.Rect(0, 900, 1000, 100)


def viravnivanie():
    rect_obman_voda.bottom = 1000
    rect_voda.bottom = rect_obman_voda.top
    rect_plot.bottom = rect_voda.top + 60
    rect_cot.bottom = rect_plot.top + 40
    rect_bucket.y = rect_cot.y - 20
    rect_umbrella.y = rect_cot.y - 100


viravnivanie()


def zapusk():
    kaplu()
    tuchka()
    up_vodi()
    kapli_net()


def up_vodi():
    if rect_kaplu.bottom > rect_obman_voda.top and 21 >= rect_kaplu.bottom - rect_obman_voda.top:
        rect_obman_voda.height += 25
        viravnivanie()


def kapli_net():
    global popalo_kapel
    if rect_kaplu.colliderect(rect_umbrella) or rect_kaplu.colliderect(rect_bucket):
        rect_kaplu.y = 10000000
        popalo_kapel += 1

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
        rect_cot.right = 985
        rect_umbrella.right = 900
        rect_bucket.right = 1000
        rect_plot.right = 1000
    # переворачивание предметов
    if rect_umbrella.x >= rect_bucket.x:
        rect_umbrella.x -= 250
    if rect_cot.x >= rect_bucket.x:
        rect_cot.x -= 140
    rect_plot.x = rect_cot.x


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
        rect_umbrella.x += 250
    if rect_cot.x <= rect_bucket.x:
        rect_cot.x += 140
    rect_plot.x = rect_cot.x
