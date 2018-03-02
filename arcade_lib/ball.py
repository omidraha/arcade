import pygame


class Ball:
    def __init__(self, surface):
        self.surface = surface
        self.org_x = 310
        self.org_y = 415
        self.size = (0, 0, 18, 18)
        self.color_ball = (255, 0, 0)
        self.color_shadow_ball = (0, 0, 0)
        self.ball_img_name = "data/image/ball.png"
        # self.ball_shadow_img_name = "data/image/ball_shadow.png"
        self.ball_shape = pygame.image.load(self.ball_img_name).convert_alpha()
        # self.ball_shape= pygame.Rect(self.size)
        # self.ball_rect = self.ball_shape.move(self.org_x,self.org_y)
        self.ball_rect = self.ball_shape.get_rect().move(self.org_x, self.org_y)

    # self.ball_shadow_shape= pygame.Rect(self.size)
    # self.ball_shadow_shape = pygame.image.load(self.ball_shadow_img_name).convert_alpha()
    # self.ball_shadow_rect = self.ball_shape.move(self.org_x,self.org_y)
    # self.ball_shadow_rect =self.ball_shadow_shape.get_rect().move(self.org_x,self.org_y)

    def draw(self, (x, y)):
        # self.ball_shadow_rect = self.ball_rect
        # pygame.draw.rect(self.surface, self.color_shadow_ball, self.ball_shadow_rect,0)
        # self.surface.blit(self.ball_shadow_shape,(self.ball_shadow_rect))
        self.ball_rect.move_ip((x, y))
        # pygame.draw.rect(self.surface, self.color_ball, self.ball_rect,0)
        self.surface.blit(self.ball_shape, (self.ball_rect))

    def reset(self):
        self.ball_rect = self.ball_shape.get_rect().move(self.org_x, self.org_y)
# pygame.draw.rect(self.surface, self.color_ball, self.ball_rect,0)
