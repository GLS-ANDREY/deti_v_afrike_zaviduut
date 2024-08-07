import pygame, model, random

timer_ubiranie_sun = pygame.event.custom_type()

smena_napravlenie_tuchki = pygame.event.custom_type()
pygame.time.set_timer(smena_napravlenie_tuchki, 3000)
pygame.key.set_repeat(100)


def allsobitiya():
    s = pygame.event.get()
    for a in s:
        #Таймеры
        if a.type == model.timer_padenie_kapel:
            model.kapli_padaut()
        if a.type == smena_napravlenie_tuchki:
            model.napravlenie_tuchki()

        #Уровень воды
        if a.type == pygame.KEYDOWN and a.key == pygame.K_SPACE:
            model.rect_obman_voda.height = random.randint(100, 900)
            model.viravnivanie()

        #Появление солнца
        if a.type == pygame.KEYDOWN and a.key == pygame.K_RETURN and model.visibility_sun == False and model.popalo_kapel >= 10:
            model.popalo_kapel -= 10
            model.poivlenie_sun()
            model.visibility_sun = True
            pygame.time.set_timer(timer_ubiranie_sun, 3000)
        if a.type == timer_ubiranie_sun:
            model.visibility_sun = False

        #Движение кота
        if a.type == pygame.KEYDOWN and a.key == pygame.K_RIGHT:
            model.pravo()
        if a.type == pygame.KEYDOWN and a.key == pygame.K_LEFT:
            model.levo()

        #Читы - накрутка
        if a.type == pygame.KEYDOWN and a.key == pygame.K_m:
            model.popalo_kapel += 1
        if a.type == pygame.KEYDOWN and a.key == pygame.K_n:
            model.urovenb += 1
        if a.type == pygame.KEYDOWN and a.key == pygame.K_b:
            model.kapli_vilitela -= 1

        #Показ ректов
        if a.type == pygame.KEYUP and a.key == pygame.K_q:
            model.visibility = not model.visibility

        #Закрытие программы на крестик
        if a.type == pygame.QUIT:
            exit()