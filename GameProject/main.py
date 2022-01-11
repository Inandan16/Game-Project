# imports files
from settings import *
from game_data import levels
from level import Level
from menu import Menu
from player import Player
import time

# initialise pygame
pygame.mixer.pre_init(200, -8, 1, 2048)  # frequency, size, channels, buffersize
pygame.mixer.init()
pygame.init()
main_clock = pygame.time.Clock()

# game state variables
intro_played = False
game_state = 0
controls_shown = False

# instances of different classes
menu = Menu(screen)
level = Level(levels, current_lvl)
player = Player(100, screen_size[1] - 275, current_lvl)

# load music from folder
pygame.mixer.music.load("Music/GameMusic/StoryOfMaple.mp3")
# plays the music infinitely
pygame.mixer.music.play(-1)

# variable to keep window running
running = True

# loop to keep window running
while running:

    main_clock.tick(fps)

    # runs intro screen
    if not intro_played:
        menu.intro()
        # keeps the intro on screen for 2.25 seconds
        time.sleep(2.25)
        intro_played = True

    # checks game state value and loads screen depending on that
    # -1 = game over / player died
    # 0 = menus
    # 1 = level
    # 2 = progress to next level

    if game_state == 0:
        game_state = menu.main_menu(game_state)

    if game_state == -1:
        if menu.restart_button.draw(screen):
            level.tile_layout = []
            level.exit_sprite.empty()
            level.lava_sprite.empty()
            level.enemy_group.empty()
            level.platform_group.empty()
            level = Level(levels, current_lvl)
            player = Player(100, screen_size[1] - 275, current_lvl)
            score = 0
            game_state = 1

    if game_state == 1:
        if not controls_shown:
            menu.control_popup()
            time.sleep(2.5)
            controls_shown = True
        level.run()
        level.exit_sprite.draw(screen)
        level.lava_sprite.draw(screen)
        level.coin_group.draw(screen)
        level.enemy_group.draw(screen)
        level.enemy_group.update()
        level.platform_group.draw(screen)
        level.platform_group.update()
        game_state = player.update(game_state)

        # shows level clear condition on screen
        if current_lvl > 2 and game_state == 1:
            draw_text(
                "Collect all coins to proceed to the next level!",
                pixel_font,
                (255, 255, 255),
                screen,
                screen_size[0] // 2,
                screen_size[0] // 30,
            )

        # coin collision
        if pygame.sprite.spritecollide(player, level.coin_group, True):
            score += 1
        draw_text(
            "X " + str(score),
            pixel_font,
            (255, 255, 255),
            screen,
            tile_size + 30,
            tile_size - 55,
        )

        # level clear condition
        if current_lvl > 2:
            if len(level.coin_group) != 1 and game_state == 2:
                game_state = 1
                if pygame.sprite.spritecollide(player, level.exit_sprite, False):
                    draw_text(
                        "Collect all coins to proceed",
                        pixel_font,
                        (255, 255, 255),
                        screen,
                        screen_size[0] // 2,
                        screen_size[1] // 2,
                    )

    # progresses to next level
    if game_state == 2:
        current_lvl += 1

        # loads level data and reset all sprite groups and object instances
        if current_lvl <= max_level:
            level.tile_layout = []
            level.exit_sprite.empty()
            level.lava_sprite.empty()
            level.enemy_group.empty()
            level.platform_group.empty()
            level = Level(levels, current_lvl)
            player = Player(100, screen_size[1] - 275, current_lvl)
            game_state = 1
            score = 0

        else:
            draw_text(
                "You completed all the levels!",
                pixel_font,
                (255, 255, 255),
                screen,
                screen_size[0] // 2,
                screen_size[1] // 2,
            )
            pygame.display.update()
            time.sleep(2)
            game_state = 0
            current_lvl = 1
            controls_shown = False
            level = Level(levels, current_lvl)
            player = Player(100, screen_size[1] - 275, current_lvl)

    # puts loop through event queue
    for event in pygame.event.get():

        # checks for quit event
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # updates the game window to load images
    pygame.display.update()
