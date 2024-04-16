import pygame, model, random

pygame.key.set_repeat(100)

def allsobitiya():
    s = pygame.event.get()

    for a in s:
        if a.type == pygame.KEYDOWN and a.key == pygame.K_SPACE:
            model.perevorot = not model.perevorot
        if a.type == pygame.KEYDOWN and a.key == pygame.K_q:
            model.visibility = not model.visibility
        if a.type == pygame.KEYDOWN and a.key == pygame.K_RIGHT:
            model.kot_xodit_vpravo()
        if a.type == pygame.KEYDOWN and a.key == pygame.K_LEFT:
            model.kot_xodit_vlevo()
        if a.type == pygame.QUIT:
            exit()