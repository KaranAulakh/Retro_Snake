'''
NOTES

Terminology
	- Blocks: refer to the yellow pills the snake is chasing
	- Walls: refer to walls that are created in the walls game mode


Bugs to Fix
	- When game ends, dead snakes go ahead one extra frame
	- Walls Mode (these are rare and don't happen in gameplay but theoretically can, and should be fixed)
		- Walls can be created right in front of the snake instantly killing the snake
		- Blocks can be placed surronded by walls so that the snake has to die after getting it 
		- Blocks may be created in the walls, rare but maybe, to confirm run game after ensuring the blocks are printing on top of walls

Good Source for Free Music
	- https://opengameart.org/art-search-advanced?field_art_tags_tid=chiptune
'''

import pygame
import Menu
import Game

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


menu = Menu.Menu(font, font_title, font_small, screen)
play = True
option = 0 # Handles return values from menu's to determine where to go next


def choose_difficulity():
	while True:
		option = menu.draw_menu(4, ["Novice", "Intermediate", "Expert", "Back"])
		if option == 1:
			return 0.20
		elif option == 2:
			return 0.15
		elif option == 3:
			return 0.10
		elif option == 4:
			return None


while True :
	play = True
	option = -1
	game_speed = 0.10
	option = menu.draw_menu(4, ["Classic", "Walls", "2 Player Battle", "Controls"])


	# Entering Classic Game mode
	if option == 1:
		game_speed = choose_difficulity()
		if game_speed != None:
			play = True
			while (play):
				play = Game.play_game(menu.screen, menu.font, menu.font_title, menu.font_small, sound_block, game_speed)
		else:
			break

	# Entering Walls Game Mode
	elif option == 2:
		game_speed = choose_difficulity()
		if game_speed != None:
			play = True
			while (play):
				play = Game.play_game_wall(menu.screen, menu.font, menu.font_title, menu.font_small, sound_block, game_speed)
		else:
			break
		

	# Entering 2 Player Game mode
	elif option == 3:
		game_speed = choose_difficulity()
		if game_speed != None:
			play = True
			while (play):
				play = Game.play_game_2player(menu.screen, menu.font, menu.font_title, menu.font_small, sound_block, game_speed)
		else:
			break

	# Entering Controls
	elif option == 4:
		while ( option != 0):
			option = menu.draw_controls()


