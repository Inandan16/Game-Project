# imports libraries / files
from button import button
from settings import *
from level import *
from player import *
from game_data import *
import time

# initialise pygame
pygame.init()
main_clock = pygame.time.Clock()


class Menu:
    # initialise class
    def __init__(self, screen):
        # class attributes
        self.screen = screen
        self.screen_size = screen_size
        self.pixel_font = pygame.font.Font("Assets/ThaleahFat.ttf", 50)
        self.load_level = Level(levels, self.screen)
        self.load_player = Player(100, screen_size[1] - 275)

        # load images
        self.background = pygame.image.load("Assets/Mockup2x.png")
        self.intro_background = pygame.image.load("Assets/background2.png")
        self.level_background = pygame.image.load("Assets/BG1.png")
        self.blank_button_image = pygame.image.load(
            "Assets/EmptyButton.png"
        ).convert_alpha()
        self.small_button_image = pygame.image.load(
            "Assets/SmallEmptyButton.png"
        ).convert_alpha()
        self.back_button_image = pygame.image.load("Assets/Back.png").convert_alpha()

        # button variables
        # parameters: x-coordinate, y-coordinate, image file name, scale
        self.singleplayer_button = button(
            ((screen_size[0] / 2) - 165), 100, self.blank_button_image, 0.5
        )
        self.multiplayer_button = button(
            ((screen_size[0] / 2) - 165), 300, self.blank_button_image, 0.5
        )
        self.options_button = button(
            ((screen_size[0] / 2) - 165), 500, self.blank_button_image, 0.5
        )
        self.quit_button = button(
            ((screen_size[0] / 2) - 165), 700, self.blank_button_image, 0.5
        )

        self.story_mode_button = button(
            ((self.screen_size[0] / 2) - 560),
            ((self.screen_size[1] / 2) - 50),
            self.blank_button_image,
            0.5,
        )
        self.freeplay_button = button(
            ((self.screen_size[0] / 2) + 160),
            ((self.screen_size[1] / 2) - 50),
            self.blank_button_image,
            0.5,
        )
        self.begin_button = button(
            ((self.screen_size[0] / 2) - 200),
            ((self.screen_size[1] / 2) - 50),
            self.blank_button_image,
            0.5,
        )
        self.back_button = button(10, 10, self.back_button_image, 5)
        self.versus_button = button(
            ((self.screen_size[0] / 2) - 560),
            ((self.screen_size[1] / 2) - 50),
            self.blank_button_image,
            0.5,
        )
        self.work_together_button = button(
            ((self.screen_size[0] / 2) + 160),
            ((self.screen_size[1] / 2) - 50),
            self.blank_button_image,
            0.5,
        )

        # button text variables
        # parameters: text, boolean for antialias, colour
        self.singleplayer_text = self.pixel_font.render("Singleplayer", True, (255, 255, 255))
        self.multiplayer_text = self.pixel_font.render("Multiplayer", True, (255, 255, 255))
        self.options_text = self.pixel_font.render("Options", True, (255, 255, 255))
        self.quit_text = self.pixel_font.render("Quit Game", True, (255, 255, 255))
        self.quit_text = self.pixel_font.render("Quit Game", True, (255, 255, 255))
        self.story_mode_text = self.pixel_font.render(
            "Story Mode", True, (255, 255, 255)
        )
        self.freeplay_text = self.pixel_font.render("Freeplay", True, (255, 255, 255))
        self.begin_text = self.pixel_font.render("Begin Game", True, (255, 255, 255))
        self.versus_text = self.pixel_font.render("VS", True, (255, 255, 255))
        self.work_together_text = self.pixel_font.render(
            "Working Together", True, (255, 255, 255)
        )

    # background function
    # loads background onto screen when called
    def set_background(self, image):
        self.screen.blit(
            pygame.transform.scale(image, self.screen_size), (0, 0)
        )

    # intro screen function
    def intro(self):

        # background is loaded in
        self.set_background(self.intro_background)

        # the draw_text function is used to write text on the screen
        draw_text(
            "Loading...",
            self.pixel_font,
            (255, 255, 255),
            screen,
            (screen_size[0] / 2 + 15),
            35,
        )

        pygame.display.update()

        # keeps the intro on screen for 2.25 seconds
        time.sleep(2.25)

    # menu functions
    def main_menu(self):
        running = True
        while running:

            self.set_background(self.background)

            # screen title
            draw_text(
                "Main Menu",
                self.pixel_font,
                (255, 255, 255),
                screen,
                ((pygame.display.Info().current_w / 2) + 15),
                35,
            )

            # button text and draw function from button class
            screen.blit(self.singleplayer_text, (((screen_size[0] / 2) - 125), 145))
            if self.singleplayer_button.draw(screen):
                self.singleplayer()

            screen.blit(self.multiplayer_text, (((screen_size[0] / 2) - 110), 345))
            if self.multiplayer_button.draw(screen):
                self.multiplayer()

            screen.blit(self.options_text, (((screen_size[0] / 2) - 60), 545))
            if self.options_button.draw(screen):
                self.options()

            screen.blit(self.quit_text, (((screen_size[0] / 2) - 75), 745))
            if self.quit_button.draw(screen):
                running = False

            # puts loop through event queue
            for event in pygame.event.get():

                # checks for quit event
                if event.type == pygame.QUIT:
                    running = False

                # checks for key press events and executes corresponding events
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

            # updates the game window to load images
            pygame.display.update()
            main_clock.tick(60)

        pygame.quit()
        sys.exit()

    def singleplayer(self):
        running = True
        while running:

            self.set_background(self.background)

            draw_text(
                "singleplayer",
                self.pixel_font,
                (255, 255, 255),
                self.screen,
                ((pygame.display.Info().current_w / 2) + 15),
                35,
            )

            self.screen.blit(
                self.story_mode_text,
                (((self.screen_size[0] / 2) - 500), (self.screen_size[1] / 2)),
            )
            if self.story_mode_button.draw(self.screen):
                self.singleplayer_story_mode()

            self.screen.blit(
                self.freeplay_text,
                (((self.screen_size[0] / 2) + 250), (self.screen_size[1] / 2)),
            )
            if self.freeplay_button.draw(self.screen):
                self.character_selection()

            if self.back_button.draw(self.screen):
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

    def multiplayer(self):
        running = True
        while running:

            self.set_background(self.background)

            draw_text(
                "multiplayer",
                self.pixel_font,
                (255, 255, 255),
                self.screen,
                ((pygame.display.Info().current_w / 2) + 15),
                35,
            )

            self.screen.blit(
                self.story_mode_text,
                (((self.screen_size[0] / 2) - 500), (self.screen_size[1] / 2)),
            )
            if self.story_mode_button.draw(self.screen):
                self.story_connect()

            self.screen.blit(
                self.freeplay_text,
                (((self.screen_size[0] / 2) + 250), (self.screen_size[1] / 2)),
            )
            if self.freeplay_button.draw(self.screen):
                self.freeplay_connect()

            if self.back_button.draw(self.screen):
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

    def options(self):
        running = True
        while running:

            self.set_background(self.background)

            draw_text(
                "options",
                self.pixel_font,
                (255, 255, 255),
                self.screen,
                ((pygame.display.Info().current_w / 2) + 15),
                35,
            )

            if self.back_button.draw(self.screen):
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

    def singleplayer_story_mode(self):
        running = True
        while running:

            self.set_background(self.background)

            draw_text(
                "Story Mode",
                self.pixel_font,
                (255, 255, 255),
                self.screen,
                ((pygame.display.Info().current_w / 2) + 15),
                35,
            )

            self.screen.blit(
                self.begin_text,
                (((self.screen_size[0] / 2) - 125), (self.screen_size[1] / 2)),
            )

            if self.begin_button.draw(self.screen):
                self.level_screen()

            if self.back_button.draw(self.screen):
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

    def story_connect(self):
        running = True
        while running:

            self.set_background(self.background)

            draw_text(
                "Pick Connection Method",
                self.pixel_font,
                (255, 255, 255),
                self.screen,
                ((pygame.display.Info().current_w / 2) + 15),
                35,
            )

            if self.back_button.draw(self.screen):
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

    def freeplay_connect(self):
        running = True
        while running:

            self.set_background(self.background)

            draw_text(
                "Pick Connection Method",
                self.pixel_font,
                (255, 255, 255),
                self.screen,
                ((pygame.display.Info().current_w / 2) + 15),
                35,
            )

            if self.back_button.draw(self.screen):
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

    def multiplayer_mode(self):
        running = True
        while running:

            self.set_background(self.background)

            draw_text(
                "Pick Multiplayer Mode",
                self.pixel_font,
                (255, 255, 255),
                self.screen,
                ((pygame.display.Info().current_w / 2) + 15),
                35,
            )

            self.screen.blit(
                self.versus_text,
                (((self.screen_size[0] / 2) - 500), (self.screen_size[1] / 2)),
            )
            if self.versus_button.draw(self.screen):
                self.character_selection()

            self.screen.blit(
                self.work_together_text,
                (((self.screen_size[0] / 2) + 250), (self.screen_size[1] / 2)),
            )
            if self.work_together_button.draw(self.screen):
                self.character_selection()

            if self.back_button.draw(self.screen):
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

    def character_selection(self):
        running = True
        while running:

            self.set_background(self.background)

            draw_text(
                "Character Selection",
                self.pixel_font,
                (255, 255, 255),
                self.screen,
                ((pygame.display.Info().current_w / 2) + 15),
                35,
            )

            if self.back_button.draw(self.screen):
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

    def level_screen(self):
        running = True
        while running:

            # loads level background
            self.set_background(self.level_background)

            # loads level
            self.load_level.run()

            # loads player
            self.load_player.update()

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()
            main_clock.tick(60)

