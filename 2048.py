import pygame
import sys
import numpy as np
from pygame.sprite import Group
from debug import debug

pygame.display.set_caption('2048')
screen_size = (320, 370)
block_size = (60, 60)
num_font = pygame.font.Font('Pixeltype.ttf', 30)
block_locations = [(10, 60), (90, 60), (170, 60), (250, 60), \
                   (10, 140), (90, 140), (170, 140), (250, 140), \
                   (10, 220), (90, 220), (170, 220), (250, 220), \
                   (10, 300), (90, 300), (170, 300), (250, 300)]
# [1 2 3 4]
# [5 6 7 8]
# [9 10 11 12]
# [13 14 15 16]
# 访问列表中的值: 用方括号

array2048_2 = np.array([[0, 0, 0, 0],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0],
                        ])

array2048_1 = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

colors = {0: '#dadbd9', 2: '#ced9bd', 4: '#bbd989', 8: '#aad959', 16: '#78ab20', 32: '#619605', 64: '#cf765b',
          128: '#cc5531', 256: '#cf451b', 512: '#c2360c', 1024: '#8f2100', 2048: '#fce805', \
          4096: '#ad9f02', 8192: '#827700', 16384: '#2b4bff', 32768: '#7033ff', 65536: '#cc0cf2', 131072: '#000000'}


# 访问字典里的值: 把相应的键放入到方括号中

class Block(pygame.sprite.Sprite):
    def __init__(self, groups, sequence, font):
        super(Block, self).__init__(groups)
        self.sequence = sequence
        self.number = 0
        self.font = font

    def update(self, array, colors, block_locations):
        self.number = array[self.sequence]
        self.image = pygame.Surface(block_size)
        self.image.fill(colors[self.number])
        self.rect = self.image.get_rect(topleft=block_locations[self.sequence])


class Number(pygame.sprite.Sprite):
    def __init__(self, groups, sequence, font):
        super(Number, self).__init__(groups)
        self.location = None
        self.number = None
        self.sequence = sequence
        self.font = font


    def update(self, array, block_locations):
        self.number = array[self.sequence]
        self.location = block_locations[self.sequence]
        self.image = self.font.render(str(self.number), False, (0, 0, 0))
        self.rect = self.image.get_rect(topleft=(self.location[0] + 5, self.location[1] + 5))
        # screen.blit(self.number_surface, self.rect)


# group setup
block_sprites = pygame.sprite.Group()
number_sprites = pygame.sprite.Group()
block_list = []
number_list = []
for i in range(16):
    block_list.append(Block(block_sprites, i, num_font))
    number_list.append(Number(number_sprites, i, num_font))

pygame.init()
screen = pygame.display.set_mode(screen_size)


# get_pressed 和 event检测是实现两种不同功能的方式, pygame.KEYDOWN是检测按下事件, 而pygame.key.get_pressed是检测按键长按的
def block_move(array):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and (event.key == pygame.K_w or event.key == pygame.K_UP):
            pass
        if event.type == pygame.KEYDOWN and (event.key == pygame.K_s or event.key == pygame.K_DOWN):
            pass
        if event.type == pygame.KEYDOWN and (event.key == pygame.K_a or event.key == pygame.K_LEFT):
            pass
        if event.type == pygame.KEYDOWN and (event.key == pygame.K_d or event.key == pygame.K_RIGHT):
            pass


def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE):
                pygame.quit()
                sys.exit()

        screen.fill('#123456')

        block_sprites.update(array2048_1, colors, block_locations)
        block_sprites.draw(screen)
        number_sprites.update(array2048_1, block_locations)
        number_sprites.draw(screen)

        pygame.display.update()  # 这一句话必须放在最后面


if __name__ == "__main__":
    main()
