import pygame

rect_cot = pygame.Rect(500, 874, 167, 126)
rect_umbrella = pygame.Rect(585, 775, 125, 125)
rect_bucket = pygame.Rect(485, 855, 60, 60)
rect_tuchka = pygame.Rect(50,50,150,120)
visibility = False
perevorot = False  # True - vpravo, False - vlevo
speed_x = 5


def tuchka():
    global speed_x
    rect_tuchka.centerx += speed_x
    if rect_tuchka.right >= 1000:
        speed_x = -speed_x
    if rect_tuchka.left <= 0:
        speed_x = -speed_x

def pravo():
    global perevorot
    perevorot = True
    # перемещение предметов
    rect_cot.x += 20
    rect_umbrella.x += 20
    rect_bucket.x += 20.0
    # граница
    if rect_bucket.x >= 940:
        rect_cot.x = 818
        rect_umbrella.x = 790
        rect_bucket.x = 940
    # переворачивание предметов
    if rect_umbrella.x >= rect_bucket.x:
        rect_umbrella.x -= 250
    if rect_cot.x >= rect_bucket.x:
        rect_cot.x -= 140

def levo():
    global perevorot
    perevorot = False
    # перемещение предметов
    rect_cot.x -= 20
    rect_umbrella.x -= 20
    rect_bucket.x -= 20
    # граница
    if rect_bucket.x <= 0:
        rect_cot.x = 15
        rect_umbrella.x = 100
        rect_bucket.x = 0
    # переворачивание предметов
    if rect_umbrella.x <= rect_bucket.x:
        rect_umbrella.x += 250
    if rect_cot.x <= rect_bucket.x:
        rect_cot.x += 140
