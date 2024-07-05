import pygame, random

pygame.init()

mils_sec_timer = 3000
timer_padenie_kapel = pygame.event.custom_type()
pygame.time.set_timer(timer_padenie_kapel, 3000)


visibility_sun = False
visibility = False
perevorot = False  # True - vpravo, False - vlevo

speed_x_tuchka = 6
speed_y_kaplu = 7

popalo_kapel = 0
kapli_vilitela = 5
urovenb = 1

# Все ректы

# Кот и его предметы
rect_plot = pygame.Rect(100, 5, 200, 70)
rect_cot = pygame.Rect(rect_plot.x, rect_plot.y, 167, 126)
rect_umbrella = pygame.Rect(185, 675, 125, 125)
rect_bucket = pygame.Rect(80, 750, 60, 60)

# Тучка и капля и солнце
rect_tuchka = pygame.Rect(50, 50, 150, 120)
rect_kaplu = pygame.Rect(rect_tuchka.x, rect_tuchka.y, 40, 40)
rect_sun = pygame.Rect(850, 0, 150, 150)

# Вода
rect_voda = pygame.Rect(0, 870, 1000, 30)
rect_obman_voda = pygame.Rect(0, 901, 1000, 100)


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


def uskorenie_kapli():
    global mils_sec_timer
    if urovenb >= 4:
        pygame.time.set_timer(timer_padenie_kapel, 0)
        pygame.time.set_timer(timer_padenie_kapel, mils_sec_timer - 200)
        mils_sec_timer = mils_sec_timer - 200

    if mils_sec_timer == 2000:
        mils_sec_timer += 200


def up_vodi():
    if rect_kaplu.bottom > rect_obman_voda.top and 21 >= rect_kaplu.bottom - rect_obman_voda.top:
        rect_obman_voda.height += 25
        viravnivanie()


def kapli_padaut():
    global kapli_vilitela, speed_x_tuchka, speed_y_kaplu, urovenb, otladka

    rect_kaplu.y = rect_tuchka.centery
    rect_kaplu.x = rect_tuchka.centerx
    kapli_vilitela -= 1

    if kapli_vilitela == 0:
        kapli_vilitela = 5
        speed_y_kaplu += 1
        urovenb += 1
        uskorenie_kapli()

        if speed_x_tuchka > 0:
            speed_x_tuchka += 1
        else:
            speed_x_tuchka -= 1


def kapli_net():
    global popalo_kapel

    if rect_kaplu.colliderect(rect_bucket):
        rect_kaplu.y = 2000000
        popalo_kapel += 1

    elif rect_kaplu.colliderect(rect_umbrella):
        rect_kaplu.y = 2000000


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

def napravlenie_tuchki():
    global speed_x_tuchka
    rr = random.choice([-1, 1])
    speed_x_tuchka = rr * speed_x_tuchka


def poivlenie_sun():
    global speed_x_tuchka, speed_y_kaplu,rect_obman_voda, mils_sec_timer
    #Часть с скоростью тучки
    if speed_x_tuchka > 1:
        speed_x_tuchka -= 1
    if speed_x_tuchka < -1:
        speed_x_tuchka += 1
    #Часть с каплей скорость,частота падения и ограничение
    speed_y_kaplu -= 1
    pygame.time.set_timer(timer_padenie_kapel, 0)
    if mils_sec_timer < 4000:
        mils_sec_timer += 200
    pygame.time.set_timer(timer_padenie_kapel, mils_sec_timer)
    if speed_y_kaplu < 4:
        speed_y_kaplu = 4
    #Часть с испарением воды и ограничением
    rect_obman_voda.height -= 50
    if rect_obman_voda.height <= 100:
        rect_obman_voda.height = 100
    viravnivanie()


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

    # переворачивание предметов
    if rect_umbrella.x >= rect_bucket.x:
        rect_umbrella.x -= 270
    if rect_cot.x >= rect_bucket.x:
        rect_cot.x -= 140
    rect_plot.x = rect_cot.x


def levo():
    global perevorot
    perevorot = False

    # перемещение предметов
    rect_bucket.x -= 35

    # граница
    if rect_bucket.x <= 0:
        rect_bucket.x = 0
    rect_cot.x = rect_bucket.x + 15
    rect_umbrella.x = rect_bucket.x + 100
    rect_plot.x = rect_cot.x
