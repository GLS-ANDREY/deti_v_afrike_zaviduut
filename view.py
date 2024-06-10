import pygame, model


display = pygame.display.set_mode([1000, 1000])
pygame.init()
font = pygame.font.SysFont("arial", 27, True)
russkiy_izik = " капель"

cat1 = pygame.image.load("pics/cat1.png")
umbrella = pygame.image.load("pics/umbrella.png")
bucket = pygame.image.load("pics/bucket.png")
tuchka = pygame.image.load("pics/cloud.png")
kaplu = pygame.image.load("pics/water_drop.png")
voda = pygame.image.load("pics/water.png")
plot = pygame.image.load("pics/raft.png")

transform_plot = pygame.transform.scale(plot,[model.rect_plot.width, model.rect_plot.height])
transform_tuchka = pygame.transform.scale(tuchka,[model.rect_tuchka.width, model.rect_tuchka.height])
transform_umbrella = pygame.transform.scale(umbrella, [model.rect_umbrella.width, model.rect_umbrella.height])
transform_bucket = pygame.transform.scale(bucket, [model.rect_bucket.width, model.rect_bucket.height])
transform_kaplu = pygame.transform.scale(kaplu,[model.rect_kaplu.width, model.rect_kaplu.height])
transform_voda = pygame.transform.scale(voda, [model.rect_voda.width, model.rect_voda.height])

perevernutiy_kot = pygame.transform.flip(cat1,True,False)
perevernutoe_bucket = pygame.transform.flip(transform_bucket,True,False)
perevernutoe_umbrella = pygame.transform.flip(transform_umbrella, True, False)

def risovanie():
    global russkiy_izik
    display.fill([0, 0, 0])
    #Надпись
    if model.popalo_kapel%10 in [0,5,6,7,8,9]:
        russkiy_izik = " капель"
    if model.popalo_kapel%10 in [2,3,4]:
        russkiy_izik = " капли"
    if model.popalo_kapel%10 == 1:
        russkiy_izik = " капля"
    if model.popalo_kapel >= 11 and model.popalo_kapel <= 19:
        russkiy_izik = " капель"

    str_popalo_kapel = str(model.popalo_kapel)
    kol_kapel = font.render(" Попало "+str_popalo_kapel+ russkiy_izik, True, [254, 255, 243])
    display.blit(kol_kapel,[0,0])
    #Тучка
    display.blit(transform_tuchka, model.rect_tuchka)
    #Капля
    display.blit(transform_kaplu, model.rect_kaplu)
    #Вода обман
    pygame.draw.rect(display,[52,144,193], model.rect_obman_voda)
    #Вода
    display.blit(transform_voda, model.rect_voda)
    #Плот
    display.blit(transform_plot, model.rect_plot)


    #Фигурки лево
    if model.perevorot == False:
        display.blit(cat1, model.rect_cot)
        display.blit(transform_umbrella, model.rect_umbrella)
        display.blit(transform_bucket, model.rect_bucket)

    #Фигурки право
    if model.perevorot == True:
        display.blit(perevernutiy_kot, model.rect_cot)
        display.blit(perevernutoe_umbrella, model.rect_umbrella)
        display.blit(perevernutoe_bucket, model.rect_bucket)

    #Ректы
    if model.visibility == True:
        pygame.draw.rect(display, [255, 0, 9], model.rect_cot, 3)
        pygame.draw.rect(display, [64, 150, 193], model.rect_umbrella, 3)
        pygame.draw.rect(display, [73, 156, 73], model.rect_bucket, 3)
        pygame.draw.rect(display, [240, 167, 50], model.rect_tuchka, 3)
        pygame.draw.rect(display, [255, 0, 127], model.rect_obman_voda, 3)
        pygame.draw.rect(display, [255, 185, 173], model.rect_voda, 3)
        pygame.draw.rect(display, [0, 255, 152], model.rect_plot, 3)
        pygame.draw.rect(display, [0, 0, 255], model.rect_kaplu, 3)
    pygame.display.flip()