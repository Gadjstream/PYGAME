import math
import pygame
from ANIM_KILL import AnimKillHero
from UNIT import Unit

class Fonctions():
    def __init__(self, hero):
        self.grp_hero = pygame.sprite.Group()
        self.hero = hero
        self.grp_hero.add(self.hero)
        self.grp_unit = pygame.sprite.Group()
        self.grp_anim_k = pygame.sprite.Group()

        self.cd_anim_k = False
        self.cd_spawn = False

    def gestion_input(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_DOWN]:
            self.hero.image = self.hero.sprites["tire"]
            self.hero.image.set_colorkey([0, 0, 0])
        elif pressed[pygame.K_SPACE]:
            self.spawn_unit()

    def spawn_unit(self):
        if not self.cd_spawn:
            self.grp_unit.add(Unit(self.hero, self))
            self.cd_spawn = True
            pygame.time.set_timer(pygame.USEREVENT +1, 500)
        else:
            print("wait...")

    def calculate_angle(self, x2, y2, x1, y1):
        dx = x2 - x1
        dy = y2 - y1
        return math.atan2(dy, dx)


    def collision(self, sprite, grp_sprite):
        return pygame.sprite.spritecollide(sprite, grp_sprite, False, pygame.sprite.collide_mask)

    def damage(self, entity, n):
        entity.hp -= n
        print("le hero a perdu " + str(n) + " hp")
        print("hp :", entity.hp)
        if entity.hp <= 0:
            entity.hp = 0
            print("le hero est DED")
            self.hero.hero_alive = False
            self.grp_anim_k.add(AnimKillHero(self.hero, self))



