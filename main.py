'''
NOTES

Bugs to Fix
	- When game ends, dead snakes go ahead one extra frame
	- Walls Mode
		- Walls can be created right in front of the snake instantly killing the snake
		- Blocks can be placed surronded by walls so that the snake has to die after getting it 
		- Blocks may be created in the walls, rare but maybe, to confirm run game after ensuring the blocks are printing on top of walls


Next Steps
	- Game Improvements
		- Rewamp graphics, eating fruits, etc.
		- Ability to resize windows
		- Multiple two player game modes
			- Survivor: what we have now
			- Either battle, Snake is able to eat the other snake's tale (agar.io), ends either on max score or time
		- Maybe add different modes
			- Flying fruits, etc. 

	- Full Projects
		- Add to an online website
		- Add to mobile app stores
		- Create AI Snakes
		- Add user and encryption 

Good Source for Free Music
	- https://opengameart.org/art-search-advanced?field_art_tags_tid=chiptune
'''

import pygame
import menu
import game

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BLOCK_SIZE = 40

'''              '''
'''   MAIN MENU  '''
'''              '''

pygame.init()
pygame.display.set_caption('Retro Snake')
font = pygame.font.Font('Files/Rashkey.ttf', 30)
font_title = pygame.font.Font('Files/Rashkey.ttf', 70)
font_small = pygame.font.Font('Files/Rashkey.ttf', 20)
pygame.mixer.music.load("Files/music.wav")
sound_block = pygame.mixer.Sound("Files/point.wav")
sound_block.set_volume(0.15)
pygame.mixer.music.play(-1)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


menu = menu.menu(font, font_title, font_small, screen)
play = True
option = 0 # Handles return values from menu's to determine where to go next



while True :
	play = True
	back = False
	option = -1

	option = menu.draw_menu(4, ["Classic", "Walls", "2 Player Battle", "Controls"])

	# Entering Classic Game mode
	if option == 1 :
		while True :
			option = menu.draw_menu(4, ["Novice", "Intermediate", "Expert", "Back"])
			if option == 1 :
				play = True
				while (play):
					play = game.play_game(menu.screen, menu.font, menu.font_title, menu.font_small, sound_block, 0.20)
			if option == 2 :
				play = True
				while (play):
					play = game.play_game(menu.screen, menu.font, menu.font_title, menu.font_small, sound_block, 0.15)
			if option == 3 :
				play = True
				while (play):
					play = game.play_game(menu.screen, menu.font, menu.font_title, menu.font_small, sound_block, 0.10)
			if option == 4 :
				break

	# Entering Walls Game Mode
	elif option == 2 :
		while True :
			option = menu.draw_menu(4, ["Novice", "Intermediate", "Expert", "Back"])
			if option == 1 :
				play = True
				while (play):
					play = game.play_game_wall(menu.screen, menu.font, menu.font_title, menu.font_small, sound_block, 0.20)
			if option == 2 :
				play = True
				while (play):
					play = game.play_game_wall(menu.screen, menu.font, menu.font_title, menu.font_small, sound_block, 0.15)
			if option == 3 :
				play = True
				while (play):
					play = game.play_game_wall(menu.screen, menu.font, menu.font_title, menu.font_small, sound_block, 0.10)
			if option == 4 :
				break

	# Entering 2 Player Game mode
	elif option == 3 :
		while True :
			option = menu.draw_menu(4, ["Novice", "Intermediate", "Expert", "Back"])
			if option == 1 :
				play = True
				while (play):
					play = game.play_game_2player(menu.screen, menu.font, menu.font_title, menu.font_small, sound_block, 0.20)
			if option == 2 :
				play = True
				while (play):
					play = game.play_game_2player(menu.screen, menu.font, menu.font_title, menu.font_small, sound_block, 0.15)
			if option == 3 :
				play = True
				while (play):
					play = game.play_game_2player(menu.screen, menu.font, menu.font_title, menu.font_small, sound_block, 0.10)
			if option == 4 :
				break

	# Entering Controls
	elif option == 4 :
		while ( option != 0) :
			option = menu.draw_controls()

