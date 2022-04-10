import pygame
import sys

screen_size = (1280, 720)


class Block(pygame.sprite.Sprite):
    def __init__(self, number, location):
        super(Block, self).__init__()
        self.number = number
        self.location = location

    def update(self):
        pass


pygame.init()
screen = pygame.display.set_mode(screen_size)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE):
            pygame.quit()
            sys.exit()

    screen.fill('#123456')

    pygame.display.update()
