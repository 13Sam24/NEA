import pygame
from ui.Button import Button

class LevelsScreen:
    def __init__(self, screen, background, backButtonImage, levelOneImage, levelTwoImage, LevelThreeImage, LevelFourImage): # Taking in the images that are required for the page
        # Saves all veribales as attributes
        self.screen = screen
        self.background = pygame.image.load(background).convert_alpha() # Makes the background the right format for pygame to use
        self.backButtonImage = backButtonImage
        self.levelOneImage = levelOneImage
        self.levelTwoImage = levelTwoImage
        self.levelThreeImage = LevelThreeImage
        self.levelFourImage = LevelFourImage
    
    def show(self): # This is run to show the levels screen
        # Placing the background
        self.screen.blit(self.background, (0, 0))

        # Making the back button
        self.backButton = Button(self.screen, 22.5, 2, 200, 100, self.backButtonImage)

        # Making the other buttons for each of the levels
        self.levelOneButton = Button(self.screen, 22.5, 110, 435, 1000, self.levelOneImage)
        self.levelTwoButton = Button(self.screen, 502.5, 110, 435,1000, self.levelTwoImage)
        self.levelThreeButton = Button(self.screen, 982.5, 110, 435, 1000, self.levelThreeImage)
        self.levelFourButton = Button(self.screen, 1462.5, 110, 435, 1000, self.levelFourImage)
    
    def buttonPress(self):
        # This checks to see if any of the buttons where pressed
        if self.backButton.clicked(pygame.mouse.get_pos(), pygame.mouse.get_pressed()):
            return 'HomeScreen'
        if self.levelOneButton.clicked(pygame.mouse.get_pos(), pygame.mouse.get_pressed()):
            return 'LevelOne'
        if self.levelTwoButton.clicked(pygame.mouse.get_pos(), pygame.mouse.get_pressed()):
            return 'LevelTwo'
        if self.levelThreeButton.clicked(pygame.mouse.get_pos(), pygame.mouse.get_pressed()):
            return 'LevelThree'
        if self.levelFourButton.clicked(pygame.mouse.get_pos(), pygame.mouse.get_pressed()):
            return 'LevelFour'