import pygame
import sys
import numpy

screen_size = (320, 370)
block_size = (60, 60)
block_location = []

class Block(pygame.sprite.Sprite):
    def __init__(self, groups, number, location):
        super(Block, self).__init__(groups)
        self.number = number
        self.location = location
        self.image = pygame.Surface(block_size)
        self.image.fill('#abcdef')
        self.rect = self.image.get_rect(topleft=self.location)


    def update(self):
        pass


# group setup
block_sprites = pygame.sprite.Group()
block = Block(block_sprites, 2048, (33, 33))

pygame.init()
screen = pygame.display.set_mode(screen_size)



def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE):
                pygame.quit()
                sys.exit()

        screen.fill('#123456')
        block_sprites.update()
        block_sprites.draw(screen)

        pygame.display.update()


if __name__ == "__main__":
    main()
