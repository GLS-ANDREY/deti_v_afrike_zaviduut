import pygame, random

rect_cot = pygame.Rect(500, 874, 167, 126)
rect_umbrella = pygame.Rect(585, 775, 125, 125)
rect_bucket = pygame.Rect(485, 855, 60, 60)
visibility = False


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
