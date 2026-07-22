#Import libraries and classes
import pygame
from ui.Button import Button

class HomeScreen:
    def __init__(self, screen, startImage, optionImage, quitImage):
        self.screen = screen
        self.startImage = startImage
        self.optionImage = optionImage
        self.quitImage = quitImage
        startButton = Button(self.screen, 710, 540, 500, 150, self.startImage)