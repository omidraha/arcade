import pygame
import blocks, ball, bat
import random


class Arcade:
    frame = 20
    size = width, height = 640, 480
    background_img_name = "data/image/galaxy.png"
    background_img_left = "data/image/col_white_left.png"
    background_img_top = "data/image/col_white_top.png"
    heart_img_name = "data/image/heart.png"
    blocks_explosion_img_name = "data/image/blocks_explosion.png"

    Lives = 3
    Player = "Player One"
    Score = 0
    Level = 1

    def run(self):
        pygame.mixer.pre_init(44100, -16, 2, 4096)
        pygame.init()
        surface = pygame.display.set_mode(self.size, pygame.HWSURFACE, 32)  # pygame.FULLSCREEN
        pygame.display.set_caption("My Arcade Game")

        clock = pygame.time.Clock()

        background_main = pygame.image.load(self.background_img_name).convert()
        background_left = pygame.image.load(self.background_img_left).convert()
        background_right = pygame.transform.rotate(background_left, 180)
        background_top = pygame.image.load(self.background_img_top).convert()

        heart = pygame.image.load(self.heart_img_name).convert_alpha()

        blocks_explosion_img = pygame.image.load(self.blocks_explosion_img_name).convert_alpha()

        font = pygame.font.SysFont(name="arial", size=20, bold=True)

        text_enter = font.render("Press Enter ...", True, (0, 255, 0))
        text_pause = font.render("Pause", True, (0, 255, 0))
        text_lost = font.render("Lost !", True, (0, 255, 0))
        text_win = font.render("Win ! ", True, (0, 255, 0))
        text_game_over = font.render("Game Over ", True, (0, 255, 0))
        text_player = font.render(self.Player, True, (0, 255, 0))
        text_player = pygame.transform.scale(text_player, (100, 20))
        text_player = pygame.transform.rotate(text_player, 90)

        tick_bat = pygame.mixer.Sound('data/sound/bat_tick.ogg')
        tick_blocks = pygame.mixer.Sound('data/sound/blocks_tick.ogg')
        background_music = pygame.mixer.Sound('data/sound/background.oga')

        background_music.set_volume(0.3)
        tick_bat.set_volume(0.5)
        tick_blocks.set_volume(.5)

        background_music.play(-1)

        blocks_obj = blocks.Blocks(surface)
        blocks_obj.draw()

        ball_obj = ball.Ball(surface)

        bat_obj = bat.Bat(surface)

        random.seed()
        randint = random.randint

        ball_dir_x = randint(-1, 1)
        ball_dir_y = 10

        rotate = 0
        angle = .01

        state = "Start"

        blocks_explosion_slide = 0
        blocks_state = "Normal"

        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
            pressed_keys = pygame.key.get_pressed()
            if pressed_keys[pygame.K_RIGHT] and state == "Play":
                bat_obj.drive(1)
            elif pressed_keys[pygame.K_LEFT] and state == "Play":
                bat_obj.drive(-1)

            if pressed_keys[pygame.K_RETURN] or pressed_keys[pygame.K_KP_ENTER]:
                state = "Play"

            if pressed_keys[pygame.K_SPACE] and state == "Play":
                state = "Pause"

            text_lives = font.render(str(self.Lives), True, (0, 255, 0))
            text_score = font.render(str(self.Score), True, (0, 255, 0))
            text_score = pygame.transform.scale(text_score, (10 * (len(str(self.Score)) + 1), 30))
            text_level = font.render("Level 0" + str(self.Level), True, (0, 255, 0))

            rotate += angle
            if rotate >= 20: angle = angle * -1
            if rotate <= 0: angle = angle * -1
            background_rotated = pygame.transform.rotate(background_main, rotate)

            # pygame.draw.rect(surface,(255,0,0),(45,45,600-45,480-45-35),2)

            surface.blit(background_rotated, (0, 0))
            surface.blit(background_top, (0, 0))
            surface.blit(background_left, (0, 0))
            surface.blit(background_right, (600, 0))

            surface.blit(heart, (3, 10 + 280))

            surface.blit(text_lives, (13, 15 + 280))
            surface.blit(text_score, (510, 7))
            surface.blit(text_level, (80, 10))
            surface.blit(text_player, (610, 280))

            if ball_obj.ball_rect.left <= 45:
                ball_dir_x = 1 * abs(ball_dir_x + randint(-1, 1))
                tick_bat.play()
            elif ball_obj.ball_rect.right >= 600:
                ball_dir_x = -1 * abs(ball_dir_x + randint(-1, 1))
                tick_bat.play()
            elif ball_obj.ball_rect.top <= 45:
                ball_dir_y = 1 * abs(ball_dir_y + randint(-1, 1))
                tick_bat.play()
            elif ball_obj.ball_rect.bottom >= 480:
                # ball_dir_y = -1 * abs(ball_dir_y) 
                if self.Lives:
                    self.Lives -= 1
                    state = "Lost"
                    ball_obj.reset()
                    bat_obj.reset()
                    ball_dir_x = randint(-10, 10)
                    ball_dir_y = 10
                else:
                    state = "GameOver"

            if bat_obj.bat_shape_rect.top - 2 <= ball_obj.ball_rect.bottom <= bat_obj.bat_shape_rect.bottom - 10 and \
                    ball_obj.ball_rect.right >= bat_obj.bat_shape_rect.left and \
                    ball_obj.ball_rect.left <= bat_obj.bat_shape_rect.right:

                ball_dir_y = -10
                tick_bat.play()
                offset = ball_obj.ball_rect.center[0] - bat_obj.bat_shape_rect.center[0]
                if offset > 30:
                    ball_dir_x = 8 + randint(-1, 1)
                elif offset > 20:
                    ball_dir_x = 7 + randint(-1, 1)
                elif offset > 10:
                    ball_dir_x = 2 + randint(-1, 1)
                elif offset < -30:
                    ball_dir_x = -8 + randint(-1, 1)
                elif offset < -20:
                    ball_dir_x = -7 + randint(-1, 1)
                elif offset < -10:
                    ball_dir_x = -2 + randint(-1, 1)
                else:
                    ball_dir_x = ball_dir_x + randint(-1, 1)

            index = ball_obj.ball_rect.collidelist(blocks_obj.blocks)
            if index != -1:
                block_out = blocks_obj.blocks[index]
                blocks_obj.blocks[index] = (-1, -1, -1, -1)
                if ball_obj.ball_rect.bottom >= pygame.Rect(block_out).top:
                    ball_dir_y = 1 * abs(ball_dir_y)
                elif ball_obj.ball_rect.top <= pygame.Rect(block_out).bottom:
                    ball_dir_y = -1 * abs(ball_dir_y)

                block_out_left = block_out[0] - blocks_obj.block_rect[0][0]
                block_out_top = block_out[1] - blocks_obj.block_rect[0][1]
                block_out_pos = (block_out_left, block_out_top, blocks_obj.block[0], blocks_obj.block[1])
                block_in = blocks_obj.true_img.subsurface(block_out_pos)
                blocks_obj.false_img.blit(block_in, block_out_pos)

                self.Score += 100
                if blocks_obj.blocks.count((-1, -1, -1, -1)) == len(blocks_obj.blocks):
                    state = "Win"

                blocks_state = "Hitting"
                blocks_explosion_slide = 0

                tick_blocks.play()

            blocks_obj.draw()
            bat_obj.drive(0)

            if blocks_state == "Hitting":
                surface.blit(blocks_explosion_img, block_out, (40 * blocks_explosion_slide, 0, 40, 20))

            blocks_explosion_slide += 1
            if blocks_explosion_slide == 11:
                blocks_state = "Normal"

            if state == "Play":
                ball_obj.draw((ball_dir_x, ball_dir_y))
            else:
                ball_obj.draw((0, 0))

            if state == "Start":
                surface.blit(text_enter, (250, 320))
            elif state == "Pause":
                surface.blit(text_pause, (280, 300))
                surface.blit(text_enter, (250, 320))
            elif state == "Lost":
                surface.blit(text_lost, (280, 300))
                surface.blit(text_enter, (250, 320))
            elif state == "GameOver":
                surface.blit(text_game_over, (280, 300))
            elif state == "Win":
                surface.blit(text_win, (280, 300))

            clock.tick(self.frame)
            pygame.display.flip()


if __name__ == "__main__":
    ar = Arcade()
    ar.run()
