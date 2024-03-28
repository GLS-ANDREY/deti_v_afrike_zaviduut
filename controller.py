import pygame, model


def allsobitiya():
    s = pygame.event.get()

    for a in s:
        if a.type == pygame.KEYDOWN and a.key == pygame.K_q:
            model.visibility = True
        if a.type == pygame.QUIT:
            exit()
