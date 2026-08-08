#Import libraries and classes
import pygame
from ui.Button import Button

class HomeScreen:
    def __init__(self, screen, background, startImage, optionImage, quitImage): # Screen is the pygame screen which was made with pygame.display
        # Saves all veribales as attributes
        self.screen = screen
        self.background = pygame.image.load(background).convert_alpha()
        self.startImage = startImage
        self.optionImage = optionImage
        self.quitImage = quitImage

    def show(self):
        # Sets the background
        self.screen.blit(self.background, (0, 0))

        # Makes the 3 main buttons
        self.startButton = Button(self.screen, 710, 440, 500, 150, self.startImage)
        self.optionButton = Button(self.screen, 710, 635, 500, 150, self.optionImage)
        self.quitButton = Button(self.screen, 710, 830, 500, 150, self.quitImage)

    def buttonPress(self):
        # Checks if any of the buttons are clicked
        if self.startButton.clicked(pygame.mouse.get_pos(), pygame.mouse.get_pressed()):
            return 'LevelsScreen'

        if self.optionButton.clicked(pygame.mouse.get_pos(), pygame.mouse.get_pressed()):
                    return 'Options'

        if self.quitButton.clicked(pygame.mouse.get_pos(), pygame.mouse.get_pressed()):
                    return 'Quit'