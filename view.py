import pygame, model

display = pygame.display.set_mode([1000, 1000])
cat1 = pygame.image.load("pics/cat1.png")
umbrella = pygame.image.load("pics/umbrella.png")
bucket = pygame.image.load("pics/bucket.png")
tuchka = pygame.image.load("pics/cloud.png")
transform_tuchka = pygame.transform.scale(tuchka,[model.rect_tuchka.width, model.rect_tuchka.height])
transform_umbrella = pygame.transform.scale(umbrella, [model.rect_umbrella.width, model.rect_umbrella.height])
transform_bucket = pygame.transform.scale(bucket, [model.rect_bucket.width, model.rect_bucket.height])

perevernutiy_kot = pygame.transform.flip(cat1,True,False)
perevernutoe_bucket = pygame.transform.flip(transform_bucket,True,False)
perevernutoe_umbrella = pygame.transform.flip(transform_umbrella, True, False)

def risovanie():
    display.fill([0, 0, 0])
    display.blit(transform_tuchka, model.rect_tuchka)
    if model.visibility == True:
        pygame.draw.rect(display, [255, 0, 9], model.rect_cot, 3)
        pygame.draw.rect(display, [64, 150, 193], model.rect_umbrella, 3)
        pygame.draw.rect(display, [73, 156, 73], model.rect_bucket, 3)
    if model.perevorot == False:
        display.blit(cat1, model.rect_cot)
        display.blit(transform_umbrella, model.rect_umbrella)
        display.blit(transform_bucket, model.rect_bucket)
    if model.perevorot == True:
        display.blit(perevernutiy_kot, model.rect_cot)
        display.blit(perevernutoe_umbrella, model.rect_umbrella)
        display.blit(perevernutoe_bucket, model.rect_bucket)
    pygame.display.flip()