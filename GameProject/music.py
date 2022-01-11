import PySimpleGUI as psg
import pygame
from pygame.locals import *
pygame.init()
pygame.mixer.pre_init(44100, -16, 2, 4096) #frequency, size, channels, buffersize
pygame.mixer.init()

class music:

    def __init__(self, music):
        self.music = music

    def play(self):
        pygame.mixer.music.load(music)

    def change_volume(volume):
        pygame.mixer.music.set_volume(volume)

    def playing(self):
        return pygame.mixer.music.get_busy()








