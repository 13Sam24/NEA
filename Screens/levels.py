import pygame
from ui.Button import Button

class LevelsScreen:
    def __init__(self, screen, background, backButtonImage, levelOneImage, levelTwoImage, LevelThreeImage, LevelFourImage):
        self.screen = screen
        self.background = pygame.image.load(background).convert_alpha()
        self.backButtonImage = backButtonImage
        self.levelOneImage = levelOneImage
        self.levelTwoImage = levelTwoImage
        self.levelThreeImage = LevelThreeImage
        self.levelFourImage = LevelFourImage
    
    def show(self):
        self.screen.blit(self.background, (0, 0))
        self.backButton = Button(self.screen, 22.5, 2, 200, 100, self.backButtonImage)
        self.levelOneButton = Button(self.screen, 22.5, 110, 435, 1000, self.levelOneImage)
        self.levelTwoButton = Button(self.screen, 502.5, 110, 435,1000, self.levelTwoImage)
        self.levelThreeButton = Button(self.screen, 982.5, 110, 435, 1000, self.levelThreeImage)
        self.levelFourButton = Button(self.screen, 1462.5, 110, 435, 1000, self.levelFourImage)
    
    def buttonPress(self):
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