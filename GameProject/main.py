# imports files
from settings import *
from game_data import levels
from level import Level
from menu import Menu
from player import Player
import time

# initialise pygame
pygame.mixer.pre_init(44100, -16, 2, 4096)  # frequency, size, channels, buffersize
pygame.mixer.init()
pygame.init()
main_clock = pygame.time.Clock()

# font variable
# loads in a custom font text file
pixel_font = pygame.font.Font("Assets/ThaleahFat.ttf", 50)

# game state variables
intro_played = False
game_state = 1

# alternate name for calling menu function
menu = Menu(screen)
level = Level(levels, screen_size)
player = Player(100, screen_size[1] - 275)

# background image
level_background = pygame.image.load("Assets/BG1.png").convert_alpha()

# load music from folder
pygame.mixer.music.load("Music/GameMusic/StoryOfMaple.mp3")
# plays the music infinitely
# pygame.mixer.music.play(-1)

# variable to keep window running
running = True

# loop to keep window running
while running:

    # runs intro screen
    if not intro_played:
        menu.intro()
        # keeps the intro on screen for 2.25 seconds
        time.sleep(2.25)
        intro_played = True

    # checks menu state value and loads screen depending on that
    # -1 = game over / player died
    # 0 = menus
    # 1 = level
    # 2 = progress to next level

    if game_state == 0:
        game_state = menu.main_menu(game_state)

    elif game_state == 1:
        screen.blit(pygame.transform.scale(level_background, screen_size), (0, 0))
        level.run()
        level.exit_sprite.draw(screen)
        player.update(game_state)

    elif game_state == 2:
        level.level_num += 1

        game_state = 1

    # puts loop through event queue
    for event in pygame.event.get():

        # checks for quit event
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # updates the game window to load images
    pygame.display.update()
    main_clock.tick(fps)
