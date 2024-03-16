import pygame
from HERO import Hero
from FONCTIONS import Fonctions
LARGE = 1080
HAUT = 720

CD = pygame.USEREVENT +1
CD_H_MOVE = pygame.USEREVENT +2


pygame.init()
pygame.display.set_caption("OUI")
screen = pygame.display.set_mode((LARGE, HAUT))
bg = pygame.image.load("SPRITE/MAP.png")


hero = Hero()
jeu = Fonctions(hero)
clock = pygame.time.Clock()

while True:

    screen.blit(bg, (0, 0))
    if hero.hero_alive:
        screen.blit(hero.image, hero.rect)
        hero.move()
    elif not hero.hero_alive:
        hero.kill()
    jeu.grp_unit.draw(screen)
    for unit in jeu.grp_unit:
        unit.move()
    jeu.grp_anim_k.draw(screen)
    for anim in jeu.grp_anim_k:
        anim.anim_kill()
    pygame.display.flip()

    clock.tick(60)

    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
        elif events.type == pygame.KEYDOWN:
            jeu.gestion_input()
        elif events.type == CD:
            if jeu.cd_spawn:
                jeu.cd_spawn = False
        elif events.type == CD_H_MOVE:
            if not hero.update_hero:
                hero.update_hero = True



