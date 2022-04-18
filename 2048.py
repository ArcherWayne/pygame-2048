import pygame
import sys
import numpy as np

screen_size = (320, 370)
block_size = (60, 60)
block_location = []
array2048 = np.array([[0, 0, 0, 0],
                      [0, 0, 0, 0],
                      [0, 0, 0, 0],
                      [0, 0, 0, 0],
                      ])


# class Block(pygame.sprite.Sprite):
#     def __init__(self, groups, number, location):
#         super(Block, self).__init__(groups)
#         self.number = number
#         self.location = location
#         self.image = pygame.Surface(block_size)
#         self.image.fill('#abcdef')
#         self.rect = self.image.get_rect(topleft=self.location)
#
#
#     def update(self):
#         pass


# group setup
# block_sprites = pygame.sprite.Group()
# block = Block(block_sprites, 2048, (33, 33))

pygame.init()
screen = pygame.display.set_mode(screen_size)

def number_move(): # 要改成press down
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] or keys [pygame.K_UP]: # up
        print('up')
    if keys[pygame.K_s] or keys [pygame.K_DOWN]: # down
        pass
    if keys[pygame.K_a] or keys [pygame.K_LEFT]: # left
        pass
    if keys[pygame.K_d] or keys [pygame.K_RIGHT]: # down
        pass

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE):
                pygame.quit()
                sys.exit()

        screen.fill('#123456')
        # block_sprites.update()
        # block_sprites.draw(screen)
        number_move()

        pygame.display.update()


if __name__ == "__main__":
    main()
