import pygame, model

pygame.key.set_repeat(100)

def allsobitiya():
    s = pygame.event.get()

    for a in s:
        if a.type == pygame.KEYDOWN and a.key == pygame.K_RIGHT:
            model.kot_pravo()
        if a.type == pygame.KEYDOWN and a.key == pygame.K_LEFT:
            model.kot_levo()
        if a.type == pygame.KEYUP and a.key == pygame.K_q:
            model.visibility = not model.visibility
        if a.type == pygame.QUIT:
            exit()