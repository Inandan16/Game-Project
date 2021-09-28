import pygame, sys
from pygame.locals import *
pygame.init()

main_clock = pygame.time.Clock()

def draw_text(text, font, color, surface, x, y):
    object_text = font.render(text, 1, color)
    text_rect = object_text.get_rect()
    text_rect.midtop = (x, y)
    surface.blit(object_text, text_rect)

class button:
    # initialise class attributes
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    # draws button with collision
    def draw(self, surface):

        # boolean to check if an action should be performed
        action = False

        # gets x and y coordinates of cursor
        mouse = pygame.mouse.get_pos()

        # checks for mouse click when cursor is in collision range
        # changes boolean if mouse pressed and if boolean hasn't been changed
        if self.rect.collidepoint(mouse):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        # changes boolean to false if mouse not pressed
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # draws button on screen
        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action


class menu:
    def __init__(self, screen):
        self.screen = screen
        self.background = pygame.image.load('Assets/Mockup2x.png')
        self.monitor_size = [pygame.display.Info().current_w, pygame.display.Info().current_h]
        self.pixel_font = pygame.font.Font('Assets/ThaleahFat.ttf', 75)
        
    def set_background(self):
        self.screen.blit(pygame.transform.scale(self.background, self.monitor_size), (0, 0))

    # menu functions
    def singleplayer(self):
        running = True
        while running:

            self.set_background()

            draw_text('singleplayer', self.pixel_font, (255, 255, 255), self.screen, ((pygame.display.Info().current_w / 2) + 50),
                      50)

            self.screen.blit(story_mode_text, (((self.monitor_size[0] / 2) - 500), (self.monitor_size[1] / 2)))
            if story_mode_button.draw(self.screen):
                self.singleplayer_story_mode()

            self.screen.blit(freeplay_text, (((self.monitor_size[0] / 2) + 250), (self.monitor_size[1] / 2)))
            if freeplay_button.draw(screen):
                character_selection()

            if back_button.draw(self.screen):
                running = False

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

            pygame.display.update()
            main_clock.tick(60)

    def multiplayer():
        running = True
        while running:

            screen.blit(pygame.transform.scale(background, monitor_size), (0, 0))

            draw_text('multiplayer', pixel_font, (255, 255, 255), screen, ((pygame.display.Info().current_w / 2) + 50),
                      50)

            screen.blit(story_mode_text, (((monitor_size[0] / 2) - 500), (monitor_size[1] / 2)))
            if story_mode_button.draw(screen):
                story_connect()

            screen.blit(freeplay_text, (((monitor_size[0] / 2) + 250), (monitor_size[1] / 2)))
            if freeplay_button.draw(screen):
                freeplay_connect()

            if back_button.draw(screen):
                running = False

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

            pygame.display.update()
            main_clock.tick(60)

    def options():
        running = True
        while running:

            screen.blit(pygame.transform.scale(background, monitor_size), (0, 0))

            draw_text('options', pixel_font, (255, 255, 255), screen, ((pygame.display.Info().current_w / 2) + 50), 50)

            if back_button.draw(screen):
                running = False

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

            pygame.display.update()
            main_clock.tick(60)

    def singleplayer_story_mode():
        running = True
        while running:

            screen.blit(pygame.transform.scale(background, monitor_size), (0, 0))

            draw_text('Story Mode', pixel_font, (255, 255, 255), screen, ((pygame.display.Info().current_w / 2) + 50),
                      50)

            screen.blit(begin_text, (((monitor_size[0] / 2) - 125), (monitor_size[1] / 2)))

            if back_button.draw(screen):
                running = False

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

            pygame.display.update()
            main_clock.tick(60)

    def story_connect():
        running = True
        while running:

            screen.blit(pygame.transform.scale(background, monitor_size), (0, 0))

            draw_text('Pick Connection Method', pixel_font, (255, 255, 255), screen,
                      ((pygame.display.Info().current_w / 2) + 50), 50)

            if back_button.draw(screen):
                running = False

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

            pygame.display.update()
            main_clock.tick(60)

    def freeplay_connect():
        running = True
        while running:

            screen.blit(pygame.transform.scale(background, monitor_size), (0, 0))

            draw_text('Pick Connection Method', pixel_font, (255, 255, 255), screen,
                      ((pygame.display.Info().current_w / 2) + 50), 50)

            if back_button.draw(screen):
                running = False

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

            pygame.display.update()
            main_clock.tick(60)

    def multiplayer_mode():
        running = True
        while running:

            screen.blit(pygame.transform.scale(background, monitor_size), (0, 0))

            draw_text('Pick Multiplayer Mode', pixel_font, (255, 255, 255), screen,
                      ((pygame.display.Info().current_w / 2) + 50), 50)

            screen.blit(versus_text, (((monitor_size[0] / 2) - 500), (monitor_size[1] / 2)))
            if versus_button.draw(screen):
                character_selection()

            screen.blit(work_together_text, (((monitor_size[0] / 2) + 250), (monitor_size[1] / 2)))
            if work_together_button.draw(screen):
                character_selection()

            if back_button.draw(screen):
                running = False

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

            pygame.display.update()
            main_clock.tick(60)

    def character_selection():
        running = True
        while running:

            screen.blit(pygame.transform.scale(background, monitor_size), (0, 0))

            draw_text('Character Selection', pixel_font, (255, 255, 255), screen,
                      ((pygame.display.Info().current_w / 2) + 50), 50)

            if back_button.draw(screen):
                running = False

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

            pygame.display.update()
            main_clock.tick(60)
