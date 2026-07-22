#Import libraries and classes
import pygame
from ui.Button import Button

class HomeScreen:
    def __init__(self, screen, startImage, optionImage, quitImage):
        self.screen = screen
        self.startImage = startImage
        self.optionImage = optionImage
        self.quitImage = quitImage

    def show(self):
        self.startButton = Button(self.screen, 710, 440, 500, 150, self.startImage)
        self.optionButton = Button(self.screen, 710, 635, 500, 150, self.optionImage)
        self.quitButton = Button(self.screen, 710, 830, 500, 150, self.quitImage)

    def buttonPress(self):
        if self.startButton.clicked(pygame.mouse.get_pos(), pygame.mouse.get_pressed()) == True:
            return 'LevelsScreen'

        if self.optionButton.clicked(pygame.mouse.get_pos(), pygame.mouse.get_pressed()) == True:
                    return 'Options'

        if self.quitButton.clicked(pygame.mouse.get_pos(), pygame.mouse.get_pressed()) == True:
                    return 'Quit'        

    