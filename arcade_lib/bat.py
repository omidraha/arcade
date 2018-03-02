import pygame


class Bat:
    def __init__(self, surface):
        self.surface = surface
        self.org_x = self.surface.get_width() / 2 - 55
        self.org_y = self.surface.get_height() - 35
        self.width, self.height = (109, 26)
        self.size = (0, 0, self.width, self.height)
        self.border_x, self.border_y = (45, 490)
        self.mov_x, self.mov_y = (self.org_x, self.org_y)
        self.color_bat = (0, 0, 255)
        self.color_bat_shadow = (0, 0, 0)
        self.speed = 15
        self.bat_img_name = "data/image/bat.png"
        # self.bat_shadow_img_name = "data/image/bat_shadow.png"
        # self.bat_shape =  pygame.Rect(self.size)
        self.bat_shape = pygame.image.load(self.bat_img_name).convert_alpha()
        self.bat_shape_rect = pygame.Rect(self.mov_x, self.mov_y, self.width, self.height)

    # self.bat_shadow_shape = pygame.Rect(self.size)
    # self.bat_shadow_shape = pygame.image.load(self.bat_shadow_img_name).convert_alpha()
    # self.bat_shadow_shape_rect  = pygame.Rect(self.mov_x,self.mov_y,self.width,self.height)

    def drive(self, direct):
        # self.bat_shadow_shape_rect = pygame.Rect(self.mov_x,self.mov_y,self.width,self.height)
        # pygame.draw.rect(self.surface,self.color_bat_shadow,(self.bat_shadow_shape_rect))
        # self.surface.blit(self.bat_shadow_shape, (self.bat_shadow_shape_rect))
        self.mov_x += direct * self.speed
        if self.mov_x <= self.border_x:
            self.mov_x = self.border_x
        if self.mov_x >= self.border_y:
            self.mov_x = self.border_y
        self.bat_shape_rect = pygame.Rect(self.mov_x, self.mov_y, self.width, self.height)
        # pygame.draw.rect(self.surface,self.color_bat,(self.bat_shape_rect))
        self.surface.blit(self.bat_shape, self.bat_shape_rect)

    def reset(self):
        self.mov_x = self.org_x
        self.mov_y = self.org_y
