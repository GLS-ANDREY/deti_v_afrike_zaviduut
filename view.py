import pygame
display = pygame.display.set_mode([1000, 1000])

cat1 = pygame.image.load("pics/cat1.png")
display.blit(cat1,[500,874])

pygame.display.flip()
