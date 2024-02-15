import pygame
import random
import sys
import os


# Player car Class
class PlayerCar:
    def _init_(self):
        self.car_height = 80
        self.car_width = 40
        self.car = pygame.image.load("images/car.png")
        self.carImg = pygame.transform.scale(self.car, (self.car_width, self.car_height))
        self.x = 386
        self.y = 510
        self.speed = 5

    def draw_car(self, gameDisplay):
        gameDisplay.blit(self.carImg, (self.x, self.y))

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.x > 115:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x < 655:
            self.x += self.speed


# Score
class Score:
    def _init_(self, score):
        self.white = (255, 255, 255)
        self.score_x = 10
        self.score_y = 10
        self.count = 0
        self.font = pygame.font.Font(None, 32)
    def draw(self, gameDisplay):
        text = self.font.render("Score: " + str(self.count), True, self.white)
        gameDisplay.blit(text, (self.score_x, self.score_y))


# Sound
class Sound:
    def _init_(self):
        self.crash_sound = os.path.join('Car_crash_sound.mp3')

    def play(self):
        pygame.mixer.music.load(self.crash_sound)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(5)


# Crash
class Crash:
    def _init_(self):
        self.Playercar = PlayerCar()
        self.sound_method = Sound()
        self.crash_width = 40
        self.crash_height = 80
        self.crash_image = pygame.image.load("images/crash.png")
        self.crash_img = pygame.transform.scale(self.crash_image, (self.crash_width, self.crash_height))

    def draw(self):
        gameDisplay.blit(self.crash_img, (self.Playercar.x, self.Playercar.y))
        self.sound_method.play()
        pygame.display.update()
        print("You crashed! Total Score:", score)
        pygame.quit()
        sys.exit()

    def move(self):
        return
        if (
                self.Playercar.x < self.enemy_car_x + 40 and
                self.Playercar.x + 40 > self.enemy_car_x and
                self.Playercar.y < self.enemy_car_y + 80 and
                self.Playercar.y + 80 > self.enemy_car_y):
            self.draw()


if __name__ == '__main__':
    pygame.init()
    display_width = 800
    display_height = 600
    gameDisplay = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption('Car Game')
    car = PlayerCar()
    score = Score()
    crash = Crash()

    while True:
        gameDisplay.fill((128, 128, 128))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        car.move(keys)

        crash.move()
        scoe += 1
        car.draw_car(gameDisplay)
        score.draw(gameDisplay)

        pygame.display.update()