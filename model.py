import pygame

rect_cot = pygame.Rect(500, 874, 167, 126)
rect_umbrella = pygame.Rect(585, 775, 125, 125)
rect_bucket = pygame.Rect(485, 855, 60, 60)
visibility = False
perevorot = False#True - vpravo, False - vlevo


def kot_xodit_vpravo():
    rect_cot.x += 20
    rect_umbrella.x += 20
    rect_bucket.x += 20

def kot_xodit_vlevo():
    rect_cot.x -= 20
    rect_umbrella.x -= 20
    rect_bucket.x -= 20
    if rect_bucket.x <= 0:
        rect_cot.x = 15
        rect_umbrella.x = 100
        rect_bucket.x = 0

def perevernutie_predmeti():
    if rect_umbrella.x <= rect_cot.x:
        rect_umbrella.x += 120
    else:
        rect_umbrella.x -= 120
    if rect_bucket.x >= rect_cot.x:
        rect_bucket.x -= 140
    else:
        rect_bucket.x += 140