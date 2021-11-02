# imports files
from menu import Menu
from settings import *

# initialise pygame
pygame.mixer.pre_init(44100, -16, 2, 4096)  # frequency, size, channels, buffersize
pygame.mixer.init()
pygame.init()
main_clock = pygame.time.Clock()

# font variable
# loads in a custom font text file
pixel_font = pygame.font.Font("Assets/ThaleahFat.ttf", 50)

# game state variable
game_state = 0

# alternate name for calling menu function
menu_screens = Menu(screen)

# load music from folder
pygame.mixer.music.load("Music/GameMusic/StoryOfMaple.mp3")
# plays the music infinitely
#pygame.mixer.music.play(-1)

# intro condition
intro_played = False

# variable to keep window running
running = True

# loop to keep window running
while running:

    # puts loop through event queue
    for event in pygame.event.get():

        # checks for quit event
        if event.type == pygame.QUIT:
            running = False

        # checks for key press events and executes corresponding events
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

        # condition for the intro
        if not intro_played:
            menu_screens.intro()
            intro_played = True

        menu_screens.main_menu()


    # updates the game window to load images
    pygame.display.update()
    main_clock.tick(60)

pygame.quit()
sys.exit()
