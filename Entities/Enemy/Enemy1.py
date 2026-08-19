import pygame
class Enemy1:
    def __init__(self, screen, locationX, locationY):
        self.screen = screen
        self.location = (locationX, locationY)
        self.image = pygame.image.load('Assets/Entities/Enemy1.png').convert_alpha()
        self.rect = pygame.Rect(self.location[0], self.location[1], 50, 50)
        self.screen.blit(self.image, self.location)

    def move(self, distance):
        self.location = (self.location[0] - distance, self.location[1])
        self.rect = pygame.Rect(self.location[0], self.location[1], 50, 50)
        self.screen.blit(self.image, self.location)