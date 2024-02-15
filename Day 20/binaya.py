import pygame
import sys


# Background set:
class Background:

    def _init_(self, width, height):
        self.width = width
        self.height = height
        self.background_img = pygame.image.load("background_image.jpg")
        self.bg_img = pygame.transform.scale(self.background_img, (self.width, self.height))
        self.bg_x = 0
        self.bg_y = 0

    def draw(self, screen):
        screen.blit(self.bg_img, (self.bg_x, self.bg_y))


# start part:
class Start:
    def _init_(self, screen, x, y, width, height, text, font_size=30):
        self.screen = screen
        self.rect = pygame.Rect(x, y, width, height)
        self.color = (0, 0, 255)  # blue color for start button
        self.text = text
        self.font = pygame.font.Font(None, font_size)

    def draw(self, screen):
        pygame.draw.rect(self.screen, self.color, self.rect)
        text_surface = self.font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.rect.center)
        self.screen.blit(text_surface, text_rect)

    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)


# pause part:
class Pause:
    def _init_(self, screen, x, y, width, height, text, font_size=30):
        self.screen = screen
        self.rect = pygame.Rect(x, y, width, height)
        self.color = (255, 0, 0)  # Red color  for pause button
        self.text = text
        self.font = pygame.font.Font(None, font_size)

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        text_surface = self.font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.rect.center)
        self.screen.blit(text_surface, text_rect)

    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)


# Restart part:
class Restart:
    def _init_(self, screen, x, y, width, height, text, font_size=30):
        self.screen = screen
        self.rect = pygame.Rect(x, y, width, height)
        self.color = (255, 255, 0)  # yellow color for restart button
        self.text = text
        self.font = pygame.font.Font(None, font_size)

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        text_surface = self.font.render(self.text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=self.rect.center)
        self.screen.blit(text_surface, text_rect)

    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)


if _name_ == "_main_":
    pygame.init()
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Car Game")
    game = Background(800, 600)

    start = Start(screen, 350, 400, 100, 60, "Start")
    pause = Pause(screen, 200, 400, 100, 60, "Pause")
    restart = Restart(screen, 500, 400, 100, 60, "Restart")


    start.draw(screen)
    pause.draw()
    restart.draw()
    game.draw(screen)

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if start.is_clicked(mouse_pos):
                    print("Start button clicked...")

                elif pause.is_clicked(mouse_pos):
                    print("Pause button is clicked...")

                elif restart.is_clicked(mouse_pos):
                    print("Restart button is clicked...")