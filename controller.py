import pygame, model, random
proverka_pokaza_sun = False

timer_ubiranie_sun = pygame.event.custom_type()

timer_poivlenie_sun = pygame.event.custom_type()
pygame.time.set_timer(timer_poivlenie_sun, 3000)

smena_napravlenie_tuchki = pygame.event.custom_type()
pygame.time.set_timer(smena_napravlenie_tuchki, 3000)
pygame.key.set_repeat(100)


def allsobitiya():
    global proverka_pokaza_sun
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
        #TODO 1.Солнце нельзя было стартануть пока прошлое не пропало 2.Солнце моэно вызвать в самом начале игры 3. сделать солнце платным
        if a.type == timer_poivlenie_sun:
            proverka_pokaza_sun = True
        if a.type == pygame.KEYDOWN and a.key == pygame.K_RETURN and proverka_pokaza_sun == True:
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