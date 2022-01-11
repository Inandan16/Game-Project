# imports libraries / files
from button import button
from settings import *

# initialise pygame
pygame.init()
main_clock = pygame.time.Clock()


class Menu:
    # initialise class
    def __init__(self, surface):
        # class attributes
        self.screen = surface
        self.screen_size = screen_size
        self.pixel_font = pygame.font.Font("Assets/ThaleahFat.ttf", 50)

        # load images
        self.background = pygame.image.load("Assets/Mockup2x.png").convert_alpha()
        self.intro_background = pygame.image.load(
            "Assets/background2.png"
        ).convert_alpha()
        self.blank_button_image = pygame.image.load(
            "Assets/EmptyButton.png"
        ).convert_alpha()
        self.small_button_image = pygame.image.load(
            "Assets/SmallEmptyButton.png"
        ).convert_alpha()
        self.back_button_image = pygame.image.load("Assets/Back.png").convert_alpha()
        self.restart_button_image = pygame.image.load(
            "Assets/Restart.png"
        ).convert_alpha()

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
        self.restart_button = button(
            (self.screen_size[0] / 2 - 50),
            (self.screen_size[1] / 2),
            self.restart_button_image,
            5,
        )

        # button text variables
        # parameters: text, boolean for antialias, colour
        self.singleplayer_text = self.pixel_font.render(
            "Singleplayer", True, (255, 255, 255)
        )
        self.multiplayer_text = self.pixel_font.render(
            "Multiplayer", True, (255, 255, 255)
        )
        self.options_text = self.pixel_font.render("Options", True, (255, 255, 255))
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
        self.coming_soon = self.pixel_font.render("Coming Soon...", True, (255, 0, 0))

    # background function
    # loads background onto screen when called
    def set_background(self, image):
        self.screen.blit(pygame.transform.scale(image, self.screen_size), (0, 0))

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

        # puts loop through event queue
        for event in pygame.event.get():

            # checks for quit event
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

    def control_popup(self):

        self.set_background(self.intro_background)

        draw_text(
            "Controls are the arrow keys: Left, Right and Up",
            pixel_font,
            (255, 255, 255),
            screen,
            screen_size[0] // 2,
            screen_size[1] // 2,
        )

        # puts loop through event queue
        for event in pygame.event.get():

            # checks for quit event
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

    # menu functions
    def main_menu(self, state):
        if state == 0:
            while True:

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
                    state = self.singleplayer(state)
                    if state != 0:
                        return state

                screen.blit(self.multiplayer_text, (((screen_size[0] / 2) - 110), 345))
                if self.multiplayer_button.draw(screen):
                    self.multiplayer(state)

                screen.blit(self.options_text, (((screen_size[0] / 2) - 60), 545))
                if self.options_button.draw(screen):
                    self.options(state)

                screen.blit(self.quit_text, (((screen_size[0] / 2) - 75), 745))
                if self.quit_button.draw(screen):
                    pygame.quit()
                    sys.exit()

                # puts loop through event queue
                for event in pygame.event.get():

                    # checks for quit event
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                # updates the game window to load images
                pygame.display.update()
                main_clock.tick(fps)

    def singleplayer(self, state):
        if state == 0:
            while True:

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
                    state = self.singleplayer_story_mode(state)
                    if state != 0:
                        return state

                self.screen.blit(
                    self.freeplay_text,
                    (((self.screen_size[0] / 2) + 250), (self.screen_size[1] / 2)),
                )
                if self.freeplay_button.draw(self.screen):
                    self.character_selection(state)

                if self.back_button.draw(self.screen):
                    return state

                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()

                pygame.display.update()
                main_clock.tick(fps)

    def multiplayer(self, state):
        if state == 0:
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
                    self.story_connect(state)

                self.screen.blit(
                    self.freeplay_text,
                    (((self.screen_size[0] / 2) + 250), (self.screen_size[1] / 2)),
                )
                if self.freeplay_button.draw(self.screen):
                    self.freeplay_connect(state)

                if self.back_button.draw(self.screen):
                    running = False

                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()

                pygame.display.update()
                main_clock.tick(fps)

    def options(self, state):
        if state == 0:
            running = True
            while running:

                self.set_background(self.background)
                screen.blit(
                    self.coming_soon,
                    (((self.screen_size[0] / 2) - 125), (self.screen_size[1] / 2)),
                )

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

                pygame.display.update()
                main_clock.tick(fps)

    def singleplayer_story_mode(self, state):
        if state == 0:
            while True:

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
                    state = 1
                    return state

                if self.back_button.draw(self.screen):
                    return state

                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()

                pygame.display.update()
                main_clock.tick(fps)

    def story_connect(self, state):
        if state == 0:
            running = True
            while running:

                self.set_background(self.background)
                screen.blit(
                    self.coming_soon,
                    (((self.screen_size[0] / 2) - 125), (self.screen_size[1] / 2)),
                )

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

                pygame.display.update()
                main_clock.tick(fps)

    def freeplay_connect(self, state):
        if state == 0:
            running = True
            while running:

                self.set_background(self.background)
                screen.blit(
                    self.coming_soon,
                    (((self.screen_size[0] / 2) - 125), (self.screen_size[1] / 2)),
                )

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

                pygame.display.update()
                main_clock.tick(fps)

    def multiplayer_mode(self, state):
        if state == 0:
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
                    self.character_selection(state)

                self.screen.blit(
                    self.work_together_text,
                    (((self.screen_size[0] / 2) + 250), (self.screen_size[1] / 2)),
                )
                if self.work_together_button.draw(self.screen):
                    self.character_selection(state)

                if self.back_button.draw(self.screen):
                    running = False

                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()

                pygame.display.update()
                main_clock.tick(fps)

    def character_selection(self, state):
        if state == 0:
            running = True
            while running:

                self.set_background(self.background)
                screen.blit(
                    self.coming_soon,
                    (((self.screen_size[0] / 2) - 125), (self.screen_size[1] / 2)),
                )

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

                pygame.display.update()
                main_clock.tick(fps)
