import pygame
import random
import math

from FONCTIONS import Fonctions
class Hero(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.jeu = Fonctions(self)
        self.sprite_sheet = pygame.image.load("SPRITE/HERO.png")
        self.sprites = {
            "hero": self.get_image(0, 0),
            "tire": self.get_image(320, 0),
            "tp1": self.get_image(640, 0),
            "tp2": self.get_image(960, 0),
            "tp3": self.get_image(1280, 0),
        }
        self.image = self.sprites["hero"]
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.image.set_colorkey([0, 0, 0])
        self.rect = self.image.get_rect()
        self.rect.x = 540-25
        self.rect.y = 360-25
        self.angle = 0

        self.update_hero = True
        self.hero_alive = True

        self.hp = 100
        self.hp_max = 100
        self.speed = 1


    def get_image(self, x, y):
        image = pygame.Surface([320, 320])
        image.blit(self.sprite_sheet, (0, 0), (x, y, 320, 320))
        image = pygame.transform.scale(image, (50, 50))
        return image

    def move(self):
        if 50 < self.rect.x < 1030 and 100 < self.rect.y < 500:
            self.rect.y += self.speed * math.cos(self.angle)
            self.rect.x += self.speed * math.sin(self.angle)
        else:
            self.rect.x = 540 - 25
            self.rect.y = 360 - 25
        if self.update_hero:
            self.change_direction()

    def change_direction(self):
        print("change")
        self.update_hero = False
        x = random.randint(0, 1080)
        y = random.randint(0, 720)
        self.angle = self.jeu.calculate_angle(x, y, self.rect.x, self.rect.y)
        i = random.randint(400, 3000)
        pygame.time.set_timer(pygame.USEREVENT+2, i)


