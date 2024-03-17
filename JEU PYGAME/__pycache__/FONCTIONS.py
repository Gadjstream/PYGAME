import math
import pygame
from ANIM_KILL import AnimKillHero
from UNIT import Unit

NUM_USEREVENT = 4
custom_events = [pygame.USEREVENT + i + 1 for i in range(NUM_USEREVENT)]
CD, CD_H_MOVE, CD_FIN, FIN_ANIM_DMG = custom_events

class Fonctions():
    def __init__(self, hero):

        self.is_running = False
        self.menu_game = False

        self.grp_hero = pygame.sprite.Group()
        self.hero = hero
        self.grp_hero.add(self.hero)
        self.grp_unit = pygame.sprite.Group()
        self.grp_anim_k = pygame.sprite.Group()

        self.cd_anim_k = False
        self.cd_spawn = False
        
    def run(self, screen):
        if self.hero.hero_alive:
            screen.blit(self.hero.image, self.hero.rect)
            self.hero.move()
        elif not self.hero.hero_alive:
            self.hero.kill()
        self.grp_unit.draw(screen)
        for unit in self.grp_unit:
            unit.move()
        self.grp_anim_k.draw(screen)
        for anim in self.grp_anim_k:
            anim.anim_kill()

        if not self.cd_spawn:
            self.grp_unit.add(Unit(self.hero, self))
            self.cd_spawn = True
            pygame.time.set_timer(CD, 1000)

        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                pygame.quit()
            elif events.type == pygame.KEYDOWN:
                self.gestion_input()
            elif events.type == CD:
                if self.cd_spawn:
                    self.cd_spawn = False
            elif events.type == CD_H_MOVE:
                if not self.hero.update_hero:
                    self.hero.update_hero = True
            elif events.type == CD_FIN:
                self.is_running = False
                self.menu_game = True
            elif events.type == FIN_ANIM_DMG:
                self.hero.dmg_taken = False
                self.hero.anim_dmg("hero")

    def gestion_input(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_SPACE]:
            if self.is_running:
                self.is_running = False
            elif not self.is_running:
                self.is_running = True

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
            pygame.time.set_timer(CD_FIN, 1000)




