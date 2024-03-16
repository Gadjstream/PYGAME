import pygame
import math
from ANIM_KILL import AnimKillUnit


class Unit(pygame.sprite.Sprite):

    def __init__(self, hero, jeu):
        super().__init__()
        self.hero = hero
        self.jeu = jeu

        self.sprite_sheet = pygame.image.load("SPRITE/UNIT.png")
        self.sprites = {
            "unit": self.get_image(0, 0),
            "kill_1": self.get_image(320, 0),
            "kill_2": self.get_image(640, 0),
            "kill_3": self.get_image(960, 0),
            "kill_4": self.get_image(1280, 0),
        }
        self.image = pygame.image.load("SPRITE/UNIT_BASE.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.image.set_colorkey([0, 0, 0])
        self.rect = self.image.get_rect()
        self.rect.x = 540-25
        self.rect.y = 650
        self.dirx = 0
        self.diry = 0
        self.angle = 0
        
        self.speed = 2

        self.direction()




    def get_image(self, x, y):
        image = pygame.Surface([320, 320])
        image.blit(self.sprite_sheet, (0, 0), (x, y, 320, 320))
        return image

    def direction(self):
        x, y = pygame.mouse.get_pos()
        angle = self.jeu.calculate_angle(x, y, self.rect.x, self.rect.y)
        self.dirx = self.speed * math.cos(angle)
        self.diry = self.speed * math.sin(angle)

    def move(self):
        if not self.jeu.collision(self, self.jeu.grp_hero):
            self.rect.y += self.diry
            self.rect.x += self.dirx
            self.out_screen()
            #self.rotate()
        else:
            self.jeu.grp_unit.remove(self)
            self.jeu.damage(self.hero, 50)
            self.jeu.grp_anim_k.add(AnimKillUnit(self, self.jeu))

    def rotate(self):
        self.angle += 1

        rotated_sprite = pygame.transform.rotate(self.image, self.angle)
        rotated_rect = rotated_sprite.get_rect(center=self.rect.center)
        self.image.blit(rotated_sprite, rotated_rect.topleft)
        """self.angle = self.jeu.calculate_angle(self.hero.rect.x,
                                              self.hero.rect.y,
                                              self.rect.x,
                                              self.rect.y
                                              )
        self.image = pygame.transform.rotate(self.image, self.angle)"""


    def out_screen(self):
        if 720 < self.rect.y < 0 or self.rect.x < 0 or self.rect.x > 720:
            self.jeu.grp_unit.remove(self)

