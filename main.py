# Libraries being used
import pygame

# Things imported from other .py files I made
# from ui.Button import Button
from Screens.home import HomeScreen
from Screens.levels import LevelsScreen

pygame.init()

screen = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption('Platformer')
WHITE = (255, 255, 255)
screen.fill(WHITE)

# Initialising the screens as objects
homeScreen = HomeScreen(screen, 'Assets/HomeScreen/Start.png', 'Assets/HomeScreen/OptionsButton.png', 'Assets/HomeScreen/Quit.png')
levelsScreen = LevelsScreen(screen, 'Assets/LevelsScreen/Background.png', 'Assets/LevelsScreen/Level1.png', 'Assets/LevelsScreen/Level2.png', 'Assets/LevelsScreen/Level3.png', 'Assets/LevelsScreen/Level4.png')

# Setting the start screen to be the home screen
currentScreen = 'HomeScreen'

running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	# Shows the home screen
	if currentScreen == 'HomeScreen':
		homeScreen.show()
		pageSelect = homeScreen.buttonPress()

		if pageSelect == 'LevelsScreen':
			currentScreen = 'LevelsScreen'
		if pageSelect == 'Options':
			currentScreen = 'Options'
		if pageSelect == 'Quit':
			currentScreen = 'Quit'
			running = False
		
	# Shows the levels screen
	if currentScreen == 'LevelsScreen':
		levelsScreen.show()
		pageSelect = levelsScreen.buttonPress()
			

	pygame.display.flip()

pygame.quit()
