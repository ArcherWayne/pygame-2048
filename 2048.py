# import numpy as np
import pygame
import sys
import random
# from pygame.sprite import Group
# from debug import debug

# 跑来偷偷看源代码的小毛是嘿几把

pygame.init()
pygame.display.set_caption('2048')
clock = pygame.time.Clock()
screen_size = (320, 370)
block_size = (60, 60)
num_font = pygame.font.Font(None, 50)
game_over = num_font.render('game over', True, (255, 255,255))
block_locations = [(10, 60), (90, 60), (170, 60), (250, 60), \
                   (10, 140), (90, 140), (170, 140), (250, 140), \
                   (10, 220), (90, 220), (170, 220), (250, 220), \
                   (10, 300), (90, 300), (170, 300), (250, 300)]

# 访问列表中的值: 用方括号

# array2048_2 = np.array([[0, 0, 0, 0],
#                         [0, 0, 0, 0],
#                         [0, 0, 0, 0],
#                         [0, 0, 0, 0],
#                         ])

# array2048_1 = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
array2048_1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

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
        self.image = self.font.render(str(self.number), True, (0, 0, 0))
        self.rect = self.image.get_rect(center=(self.location[0] + 30, self.location[1] + 30))
        # screen.blit(self.number_surface, self.rect)


def init_array():
    init_list = random.sample(range(15), 4)
    for i_ia in init_list:
        array2048_1[i_ia] = random.choice([2, 2, 4])


def generate_numbers():
    zero_index_list = []
    
    zero_index = 0
    for i_gn in array2048_1:
        if i_gn == 0:
            zero_index_list.append(zero_index)
        zero_index += 1

    if zero_index_list:
        array2048_1[random.choice(zero_index_list)] = random.choice([2, 2, 2, 2, 2, 2, 2, 2, 2, 4])
    else:
        # 此处添加一个检查不能再继续生成的公式
        game_over_flag_list = []
        for y in range(0, 12, 4):
            for x in range(4):
                if array2048_1[x+y] == array2048_1[x+y+4]:
                    # game_over_flag = 0
        for y in range(12, 0 ,-4):
            for x in range(4):
                if array2048_1[x+y] == array2048_1[x+y-4]:
                    # game_over_flag = 0
        for x in range()



            



def show_infomation():
    pass

# group setup
block_sprites = pygame.sprite.Group()
number_sprites = pygame.sprite.Group()
block_list = []
number_list = []
for i in range(16):
    block_list.append(Block(block_sprites, i, num_font))
    number_list.append(Number(number_sprites, i, num_font))

screen = pygame.display.set_mode(screen_size)

init_array()
game_active = True


def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE):
                pygame.quit()
                sys.exit()

            if game_active == True:
                # get_pressed 和 event检测是实现两种不同功能的方式, pygame.KEYDOWN是检测按下事件, 而pygame.key.get_pressed是检测按键长按的
                if event.type == pygame.KEYDOWN and (event.key == pygame.K_w or event.key == pygame.K_UP):
                    # print('w')
                    for x_w in range(4):
                        # print("x_w：{name}".format(name=x_w))
                        for c_w in range(0, 12, 4):
                            # print("c_w：{name}".format(name=c_w))
                            for y_w in range(c_w + 4, 16, 4):
                                # print("y_w：{name}".format(name=y_w))
                                if array2048_1[y_w + x_w] != 0:
                                    if array2048_1[c_w + x_w] == 0:
                                        array2048_1[c_w + x_w] = array2048_1[y_w + x_w]
                                        array2048_1[y_w + x_w] = 0
                                    elif array2048_1[c_w + x_w] == array2048_1[y_w + x_w]:
                                        array2048_1[c_w + x_w] *= 2
                                        array2048_1[y_w + x_w] = 0
                                        break
                                    elif array2048_1[c_w + x_w] != array2048_1[y_w + x_w]:
                                        break
                    generate_numbers()

                if event.type == pygame.KEYDOWN and (event.key == pygame.K_s or event.key == pygame.K_DOWN):  # complete
                    # print('s')
                    for x_s in range(4):
                        for c_s in range(12, 0, -4):
                            for y_s in range(c_s - 4, -4, -4):
                                if array2048_1[y_s + x_s] != 0:
                                    if array2048_1[c_s + x_s] == 0:
                                        array2048_1[c_s + x_s] = array2048_1[y_s + x_s]
                                        array2048_1[y_s + x_s] = 0
                                    elif array2048_1[c_s + x_s] == array2048_1[y_s + x_s]:
                                        array2048_1[c_s + x_s] *= 2
                                        array2048_1[y_s + x_s] = 0
                                        break
                                    elif array2048_1[c_s + x_s] != array2048_1[y_s + x_s]:
                                        break
                    generate_numbers()

                if event.type == pygame.KEYDOWN and (event.key == pygame.K_a or event.key == pygame.K_LEFT):
                    # print('a')
                    for y_a in range(0, 16, 4):
                        # print("y_a：{name}".format(name=y_a))
                        for c_a in range(3):
                            # print("c_a：{name}".format(name=c_a))
                            for x_a in range(c_a + 1, 4):
                                # print("x_a：{name}".format(name=x_a))
                                if array2048_1[x_a + y_a] != 0:
                                    if array2048_1[c_a + y_a] == 0:
                                        array2048_1[c_a + y_a] = array2048_1[x_a + y_a]
                                        array2048_1[x_a + y_a] = 0
                                    elif array2048_1[c_a + y_a] == array2048_1[x_a + y_a]:
                                        array2048_1[c_a + y_a] *= 2
                                        array2048_1[x_a + y_a] = 0
                                        break
                                    elif array2048_1[c_a + y_a] != array2048_1[x_a + y_a]:
                                        break
                    generate_numbers()

                if event.type == pygame.KEYDOWN and (event.key == pygame.K_d or event.key == pygame.K_RIGHT):
                    # print('d')
                    for y_d in range(0, 16, 4):
                        for c_d in range(3, 0, -1):
                            for x_d in range(c_d - 1, -1, -1):
                                if array2048_1[x_d + y_d] != 0:
                                    if array2048_1[c_d + y_d] == 0:
                                        array2048_1[c_d + y_d] = array2048_1[x_d + y_d]
                                        array2048_1[x_d + y_d] = 0
                                    elif array2048_1[c_d + y_d] == array2048_1[x_d + y_d]:
                                        array2048_1[c_d + y_d] *= 2
                                        array2048_1[x_d + y_d] = 0
                                        break
                                    elif array2048_1[c_d + y_d] != array2048_1[x_d + y_d]:
                                        break
                    generate_numbers()
        
        if game_active == True:
            screen.fill('#123456')

            block_sprites.update(array2048_1, colors, block_locations)
            block_sprites.draw(screen)
            number_sprites.update(array2048_1, block_locations)
            number_sprites.draw(screen)

        else:
            block_sprites.empty()
            number_sprites.empty()
            screen.fill('#654321')
            screen.blit(game_over, (160, 185))


        pygame.display.update()  # 这一句话必须放在组绘图和组更新的后面
        clock.tick(60)


if __name__ == "__main__":
    main()
