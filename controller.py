import pygame, model, random

randomniy_type_timerov = pygame.event.custom_type()
pygame.time.set_timer(randomniy_type_timerov, 3000)
pygame.key.set_repeat(100)


def allsobitiya():
    s = pygame.event.get()
    for a in s:

        #Таймеры
        if a.type == model.timer_padenie_kapel:
            model.kapli_padaut()
        if a.type == randomniy_type_timerov:
            rr = random.choice([-1,1])
            model.speed_x_tuchka = rr * model.speed_x_tuchka

        #Уровень воды
        if a.type == pygame.KEYDOWN and a.key == pygame.K_SPACE:
            model.rect_obman_voda.height = random.randint(100, 900)
            model.viravnivanie()

        #Появление солнца
        if a.type == pygame.KEYDOWN and a.key == pygame.K_RETURN:
            model.poivlenie_sun()
            model.visibility_sun = True
            pygame.time.set_timer(randomniy_type_timerov, 3000)
        if a.type == randomniy_type_timerov:
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