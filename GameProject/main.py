# imports the pygame library
import pygame, sys
from pygame.locals import *
from numpy import *
import pgu
import time
from menu import button

# initialise pygame
pygame.mixer.pre_init(44100, -16, 2, 4096) #frequency, size, channels, buffersize
pygame.mixer.init()
pygame.init()
main_clock = pygame.time.Clock()

# font variable
pixel_font = pygame.font.Font('Assets/ThaleahFat.ttf', 75)

# text function
def draw_text(text, font, color, surface, x, y):
    object_text = font.render(text, 1, color)
    text_rect = object_text.get_rect()
    text_rect.midtop = (x, y)
    surface.blit(object_text, text_rect)


# get monitor resolution display
monitor_size = [pygame.display.Info().current_w, pygame.display.Info().current_h]

# window dimensions and caption
screen = pygame.display.set_mode(monitor_size, HWSURFACE | DOUBLEBUF | FULLSCREEN)
pygame.display.set_caption("Game")

# load images
background = pygame.image.load('Assets/Mockup2x.png')
intro_background = pygame.image.load('Assets/background2.png')
blank_button_image = pygame.image.load('Assets/EmptyButton.png').convert_alpha()
small_button_image = pygame.image.load('Assets/SmallEmptyButton.png').convert_alpha()
back_button_image = pygame.image.load('Assets/Back.png').convert_alpha()

# load sound


# load and play music
pygame.mixer.music.load('Music/GameMusic/StoryOfMaple.mp3')
pygame.mixer.music.play(-1)

# button variables
singleplayer_button = button(((monitor_size[0] / 2) - 200), 200, blank_button_image, 0.65)
multiplayer_button = button(((monitor_size[0] / 2) - 200), 400, blank_button_image, 0.65)
options_button = button(((monitor_size[0] / 2) - 200), 600, blank_button_image, 0.65)
quit_button = button(((monitor_size[0] / 2) - 200), 800, blank_button_image, 0.65)
story_mode_button = button(((monitor_size[0] / 2) - 560), ((monitor_size[1] / 2) - 50), blank_button_image, 0.65)
freeplay_button = button(((monitor_size[0] / 2) + 160), ((monitor_size[1] / 2) - 50), blank_button_image, 0.65)
begin_button = button(((monitor_size[0] / 2) - 200), ((monitor_size[1] / 2) - 50), blank_button_image, 0.65)
back_button = button(10, 10, back_button_image, 5)
versus_button = button(((monitor_size[0] / 2) - 560), ((monitor_size[1] / 2) - 50), blank_button_image, 0.65)
work_together_button = button(((monitor_size[0] / 2) + 160), ((monitor_size[1] / 2) - 50), blank_button_image, 0.65)

# button text variables
singleplayer_text = pixel_font.render('Singleplayer', True, (255, 255, 255))
mulitplayer_text = pixel_font.render('Multiplayer', True, (255, 255, 255))
options_text = pixel_font.render('Options', True, (255, 255, 255))
quit_text = pixel_font.render('Quit Game', True, (255, 255, 255))
story_mode_text = pixel_font.render('Story Mode', True, (255, 255, 255))
freeplay_text = pixel_font.render('Freeplay', True, (255, 255, 255))
begin_text = pixel_font.render('Begin Game', True, (255, 255, 255))
versus_text = pixel_font.render('VS', True, (255, 255, 255))
work_together_text = pixel_font.render('Working Together', True, (255, 255, 255))

# menu functions
def singleplayer():
    running = True
    while running:

        screen.blit(pygame.transform.scale(background, monitor_size), (0, 0))

        draw_text('singleplayer', pixel_font, (255, 255, 255), screen, ((pygame.display.Info().current_w / 2) + 50), 50)

        screen.blit(story_mode_text, (((monitor_size[0] / 2) - 500), (monitor_size[1] / 2)))
        if story_mode_button.draw(screen):
            singleplayer_story_mode()

        screen.blit(freeplay_text,(((monitor_size[0] / 2) + 250), (monitor_size[1] / 2)))
        if freeplay_button.draw(screen):
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


def multiplayer():
    running = True
    while running:

        screen.blit(pygame.transform.scale(background, monitor_size), (0, 0))

        draw_text('multiplayer', pixel_font, (255, 255, 255), screen, ((pygame.display.Info().current_w / 2) + 50), 50)

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

        draw_text('Story Mode', pixel_font, (255, 255, 255), screen, ((pygame.display.Info().current_w / 2) + 50), 50)

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

        draw_text('Pick Connection Method', pixel_font, (255, 255, 255), screen, ((pygame.display.Info().current_w / 2) + 50), 50)

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

        draw_text('Pick Connection Method', pixel_font, (255, 255, 255), screen, ((pygame.display.Info().current_w / 2) + 50), 50)

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

        draw_text('Pick Multiplayer Mode', pixel_font, (255, 255, 255), screen, ((pygame.display.Info().current_w / 2) + 50), 50)

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

        draw_text('Character Selection', pixel_font, (255, 255, 255), screen, ((pygame.display.Info().current_w / 2) + 50), 50)

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


# Loading screen function
def intro():
    screen.blit(pygame.transform.scale(intro_background, monitor_size), (0, 0))
    draw_text('Loading...', pixel_font, (255, 255, 255), screen, (pygame.display.Info().current_w / 2) + 50, 50)
    pygame.display.update()
    time.sleep(2.25)


# variable whether it is fullscreen or not
fullscreen = False

# Loading screen before main menu
intro()

# variable to keep window running
main_menu = True

# loop to keep window running
while main_menu:

    # adds images to the game window
    screen.blit(pygame.transform.scale(background, monitor_size), (0, 0))

    # screen title
    draw_text('Main Menu', pixel_font, (255, 255, 255), screen, ((pygame.display.Info().current_w / 2) + 35), 100)

    # button text and draw function from button class
    screen.blit(singleplayer_text, (((monitor_size[0] / 2) - 175), 250))
    if singleplayer_button.draw(screen):
        singleplayer()

    screen.blit(mulitplayer_text, (((monitor_size[0] / 2) - 150), 450))
    if multiplayer_button.draw(screen):
        multiplayer()

    screen.blit(options_text, (((monitor_size[0] / 2) - 80), 650))
    if options_button.draw(screen):
        options()

    screen.blit(quit_text, (((monitor_size[0] / 2) - 100), 850))
    if quit_button.draw(screen):
        pygame.quit()

    # click variable
    click = False

    # puts loop through event queue
    for event in pygame.event.get():

        # checks for quit event
        if event.type == pygame.QUIT:
            active_window = False

        # checks for key press events and executes corresponding events
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

    # updates the game window to load images
    pygame.display.update()
    main_clock.tick(60)
