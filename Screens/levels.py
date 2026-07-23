import pygame
from ui.Button import Button

class LevelsScreen:
    def __init__(self, screen, background, levelOneImage, levelTwoImage, LevelThreeImage, LevelFourImage):
        self.screen = screen
        self.background = pygame.image.load(background).convert_alpha()
        self.levelOneImage = levelOneImage
        self.levelTwoImage = levelTwoImage
        self.levelThreeImage = LevelThreeImage
        self.levelFourImage = LevelFourImage
    
    def show(self):
        self.screen.blit(self.background, (0, 0))
        self.levelOneButton = Button(self.screen, 22.5, 80, 435, 1000, self.levelOneImage)
        self.levelTwoButton = Button(self.screen, 502.5, 80, 435,1000, self.levelTwoImage)
        self.levelThreeButton = Button(self.screen, 982.5, 80, 435, 1000, self.levelThreeImage)
        self.levelFourButton = Button(self.screen, 1462.5, 80, 435, 1000, self.levelFourImage)
    
    def buttonPress(self):
        if self.levelOneButton.clicked(pygame.mouse.get_pos(), pygame.mouse.get_pressed()):
            return 'LevelOne'
        if self.levelTwoButton.clicked(pygame.mouse.get_pos(), pygame.mouse.get_pressed()):
            return 'LevelTwo'
        if self.levelThreeButton.clicked(pygame.mouse.get_pos(), pygame.mouse.get_pressed()):
            return 'LevelThree'
        if self.levelFourButton.clicked(pygame.mouse.get_pos(), pygame.mouse.get_pressed()):
            return 'LevelFour'