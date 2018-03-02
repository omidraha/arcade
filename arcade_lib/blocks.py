import pygame


class Blocks:
    def __init__(self, surface):
        self.surface = surface
        self.windows = (50, 45, 550, 225)
        self.block = 40, 20
        self.color_windows = (0, 255, 0)
        self.color_blocks = (0, 0, 255)
        self.block_img_name = "data/image/block.png"
        self.true_img_name = "data/image/py3.png"
        self.false_img_name = "data/image/py2.png"

        self.block_img = pygame.image.load(self.block_img_name).convert_alpha()
        self.true_img = pygame.image.load(self.true_img_name).convert()
        self.false_img = pygame.image.load(self.false_img_name).convert()

        self.mat_x = ((self.windows[2]) % self.block[0]) / 2.0
        self.mat_y = ((self.windows[3]) % self.block[1]) / 2.0
        self.blocks = []
        self.x_left = int(self.mat_x + self.windows[0])
        self.y_top = int(self.mat_y + self.windows[1])
        self.x_right = int((self.windows[2] + self.windows[0]) - self.mat_x)
        self.y_bottom = int((self.windows[3] + self.windows[1]) - self.mat_y)
        self.cols = (self.x_right - self.x_left) / self.block[0]
        self.rows = (self.y_bottom - self.y_top) / self.block[1]

        for i in range(self.x_left, self.x_right, self.block[0]):
            for j in range(self.y_top, self.y_bottom, self.block[1]):
                self.blocks.append((i, j, self.block[0], self.block[1]))

        self.block_rect = (self.blocks[0][:2], self.blocks[-1][:2])

    def draw(self):
        # pygame.draw.rect(self.surface, self.color_windows, self.windows,0)
        self.surface.blit(self.false_img, self.block_rect)

        for item in self.blocks:
            if item != (-1, -1, -1, -1):
                # pygame.draw.rect(self.surface, self.color_blocks, item,1)
                self.surface.blit(self.block_img, item)
