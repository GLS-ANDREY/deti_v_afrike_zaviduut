import pygame, model, random

cn = pygame.event.custom_type()
pygame.time.set_timer(cn, 3000)
pygame.key.set_repeat(100)


def allsobitiya():
    s = pygame.event.get()

    for a in s:
        if a.type == cn:
            rr = random.choice([-1,1])
            model.speed_x_tuchka = rr * model.speed_x_tuchka
        if a.type == pygame.KEYDOWN and a.key == pygame.K_RIGHT:
            model.pravo()
        if a.type == pygame.KEYDOWN and a.key == pygame.K_LEFT:
            model.levo()
        if a.type == pygame.KEYUP and a.key == pygame.K_q:
            model.visibility = not model.visibility
        if a.type == pygame.QUIT:
            exit()
