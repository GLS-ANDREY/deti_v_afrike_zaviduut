import pygame, model, random

ct1 = pygame.event.custom_type()
ct2 = pygame.event.custom_type()
pygame.time.set_timer(ct2, 3000)
pygame.time.set_timer(ct1, 3000)
pygame.key.set_repeat(100)


def allsobitiya():
    s = pygame.event.get()

    for a in s:
        if a.type == ct2:
            model.rect_kaplu.y = model.rect_tuchka.centery
            model.rect_kaplu.x = model.rect_tuchka.centerx
        if a.type == ct1:
            rr = random.choice([-1,1])
            model.speed_x_tuchka = rr * model.speed_x_tuchka
        if a.type == pygame.KEYDOWN and a.key == pygame.K_SPACE:
            model.rect_obman_voda.height = random.randint(100, 1000)
        if a.type == pygame.KEYDOWN and a.key == pygame.K_RIGHT:
            model.pravo()
        if a.type == pygame.KEYDOWN and a.key == pygame.K_LEFT:
            model.levo()
        if a.type == pygame.KEYUP and a.key == pygame.K_q:
            model.visibility = not model.visibility
        if a.type == pygame.QUIT:
            exit()
