import pygame
import random


##enemy car
class Enemy_Car:
    def _init_(self):
        self.speed = 7
        self.enemy_car = pygame.image.load("car.png")
        self.enemy = pygame.transform.scale(self.enemy_car, (40, 80))
        self.x = random.randint(120, 670)
        self.y = 0

    def move(self):
        self.y += self.speed
        if self.y > height:
            self.y = 0
            self.x = random.randint(120, 670)

    def draw(self, screen):
        screen.blit(self.enemy, (self.x, self.y))
        self.move()


## for grass
class Grass:
    def _init_(self):
        self.grass = pygame.image.load("grass.jpg")

    def draw(self, screen):
        screen.blit(self.grass, (0, 0))
        screen.blit(self.grass, (700, 0))


#### for track
class Track:
    def _init_(self):
        self.width = 10
        self.height = 600

        self.white_track = pygame.image.load("white_strip.jpg")
        self.white = pygame.transform.scale(self.white_track, (self.width, self.height))
        self.strips = [

        ]

    def draw(self, screen):
        screen.blit(self.white, (100, 0))
        screen.blit(self.white, (700, 0))


## for strip
class Strip:
    def _init_(self, img, coord):
        self.image = pygame.image.load("yellow_strip.png")

    def draw(self, screen):
        screen.blit(self.yellow_strip, (400, 0))
        screen.blit(self.yellow_strip, (400, 150))
        screen.blit(self.yellow_strip, (400, 300))
        screen.blit(self.yellow_strip, (400, 450))





if __name__ == '__main__':
    pygame.init()

    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))

    pygame.display.set_caption("Car Game")

    enemy_car = Enemy_Car()
    grass = Grass()
    track = Track()
    strip = Strip()

    while True:
        screen.fill((128, 128, 128))
        enemy_car.draw(screen)
        grass.draw(screen)
        track.draw(screen)
        strip.draw(screen)
        pygame.display.update()
        pygame.time.Clock().tick(70)