#Libraries being used
import pygame

#Things imported from other .py files I made
from ui.Button import Button
from Screens.home import HomeScreen

pygame.init()

screen = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption('Platformer')
WHITE = (255, 0, 0)
screen.fill(WHITE)

#Initialising the screens as objects
homeScreen = HomeScreen(screen, 'Assets\HomeScreen\Start.png', 'OptionsButton.png', 'Quit.png')

running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

pygame.quit()
