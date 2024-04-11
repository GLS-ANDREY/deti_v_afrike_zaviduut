import random, pygame, model

display = pygame.display.set_mode([1000, 1000])
cat1 = pygame.image.load("pics/cat1.png")
umbrella = pygame.image.load("pics/umbrella.png")
bucket = pygame.image.load("pics/bucket.png")
transform_umbrella = pygame.transform.scale(umbrella, [model.rect_umbrella.width, model.rect_umbrella.height])
transform_bucket = pygame.transform.scale(bucket, [model.rect_bucket.width, model.rect_bucket.height])


def visible_predmetov():
    if model.visibility == True:
        pygame.draw.rect(display, [255, 0, 9], model.rect_cot, 3)
        pygame.draw.rect(display, [64, 150, 193], model.rect_umbrella, 3)
        pygame.draw.rect(display, [73, 156, 73], model.rect_bucket, 3)
        pygame.display.flip()
    if model.visibility == False:
        display.fill([0, 0, 0])
        display.blit(cat1, model.rect_cot)
        display.blit(transform_umbrella, model.rect_umbrella)
        display.blit(transform_bucket, model.rect_bucket)
        pygame.display.flip()
