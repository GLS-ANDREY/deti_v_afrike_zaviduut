import pygame,model

display = pygame.display.set_mode([1000, 1000])
cat1 = pygame.image.load("pics/cat1.png")

display.blit(cat1,model.rect_cot)
def visible_cota():
    if model.visibility == True:
        pygame.draw.rect(display,[255,0,9],model.rect_cot,3)
        pygame.display.flip()

pygame.display.flip()
