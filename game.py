
'''                   
    ****    GAME	****       

  	Handles all gameplay, runs with a set of helper functions and a seperate method to control
  	the gameplay and logic for each seperate game mode
'''

import pygame
import random
import time
import snake
import sys


# CONST
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BLOCK_SIZE = 40
 
#GAME COLORS
GREEN = (0, 75, 0)
DARK_GREEN = (0, 71, 0)
WHITE = (255, 255, 255)
BLACK = (0, 45, 0)
#SNAKE COLORS
PURPLE = (150, 15, 255)
BRIGHT_PURPLE = (190, 40, 255)
RED = (255, 0, 0)
BRIGHT_RED = (255, 80, 80)
#BLOCK COLORS
YELLOW = (255, 255, 0)
ORANGE = (255, 220, 0)


'''                      '''
'''    HELPER METHODS    '''
'''                      '''

def read_high_score(game_mode):
	with open('Files/score.txt') as file :
		for line in file :
			if str(game_mode) in line : 
				return line[11:]

	return -1 

def write_high_score(game_mode, score):
	# Find the line needed to edit
	with open('Files/score.txt') as file_r :
		line_num = 0
		for line in file_r :
			if str(game_mode) in line : 
				break 
			line_num += 1

	# Load the file in data, line by line
	with open('Files/score.txt') as file_r :	
		data = file_r.readlines()

	# Checks if line was not found, prints error and returns out of function
	if (line_num >= len(data)) :
		print ("Error Line not Found")
		return -1

	# Changes the appropriate line number to the new score and saves it within the file	
	data[line_num] = game_mode + ": "+ str(score) + '\n'
	with open('Files/score.txt', 'w') as file_w : 
		file_w.writelines(data)

	return 0


def draw_text(screen, text, color, font, pos_x, pos_y):
	text = font.render(text, True, color)
	text_rect = text.get_rect(center=(pos_x, pos_y))
	screen.blit(text, text_rect)

def create_block(block_pos, block_swallowed_bool, screen, color_switch, snake):
	spot_taken = True
	x = y = -1

	if (block_swallowed_bool):
		while spot_taken :
			spot_taken = False
			x = random.randint(1, int(SCREEN_WIDTH/BLOCK_SIZE) - 2) * BLOCK_SIZE
			y = random.randint(1, int(SCREEN_HEIGHT/BLOCK_SIZE) - 2) * BLOCK_SIZE

			# Check if the block is in the snake
			for j in range(len(snake.position)):
				if (x == snake.position[j][0] and y == snake.position[j][1]):
					spot_taken = True

		block_pos[0] = x
		block_pos[1] = y
		block_swallowed_bool = False


	if color_switch :
		pygame.draw.circle(screen, YELLOW, [block_pos[0] + BLOCK_SIZE/2, block_pos[1] + BLOCK_SIZE/2], BLOCK_SIZE/2)
	else :
		pygame.draw.circle(screen, ORANGE, [block_pos[0] + BLOCK_SIZE/2, block_pos[1] + BLOCK_SIZE/2], BLOCK_SIZE/2)


	return block_pos;

def create_block_2P(block_pos, block_swallowed_bool, screen, color_switch, snake, snake_two):
	spot_taken = True
	x = y = -1

	if (block_swallowed_bool):
		while spot_taken :
			spot_taken = False
			x = random.randint(1, int(SCREEN_WIDTH/BLOCK_SIZE) - 2) * BLOCK_SIZE
			y = random.randint(1, int(SCREEN_HEIGHT/BLOCK_SIZE) - 2) * BLOCK_SIZE

			# Check if the block is in the snake
			for j in range(len(snake.position)):
				if (x == snake.position[j][0] and y == snake.position[j][1]):
					spot_taken = True

			for j in range(len(snake_two.position)):
				if (x == snake_two.position[j][0] and y == snake_two.position[j][1]):
					spot_taken = True

		block_pos[0] = x
		block_pos[1] = y
		block_swallowed_bool = False


	if color_switch :
		pygame.draw.circle(screen, YELLOW, [block_pos[0] + BLOCK_SIZE/2, block_pos[1] + BLOCK_SIZE/2], BLOCK_SIZE/2)
	else :
		pygame.draw.circle(screen, ORANGE, [block_pos[0] + BLOCK_SIZE/2, block_pos[1] + BLOCK_SIZE/2], BLOCK_SIZE/2)


	return block_pos;

def create_block_wall(block_pos, block_swallowed_bool, screen, color_switch, wall, snake):
	spot_taken = True
	x = y = -1

	if (block_swallowed_bool):
		while spot_taken :
			spot_taken = False
			x = random.randint(1, int(SCREEN_WIDTH/BLOCK_SIZE) - 2) * BLOCK_SIZE
			y = random.randint(1, int(SCREEN_HEIGHT/BLOCK_SIZE) - 2) * BLOCK_SIZE

			# Check if block is in a wall
			for j in range(len(wall) - 1):
				if (x == wall[j + 1][0] and y == wall[j + 1][1]):
					spot_taken = True

			# Check if the block is in the snake
			for j in range(len(snake.position)):
				if (x == snake.position[j][0] and y == snake.position[j][1]):
					spot_taken = True

		block_pos[0] = x
		block_pos[1] = y
		block_swallowed_bool = False


	if color_switch :
		pygame.draw.circle(screen, YELLOW, [block_pos[0]+BLOCK_SIZE/2, block_pos[1]+BLOCK_SIZE/2], BLOCK_SIZE/2)
	else :
		pygame.draw.circle(screen, ORANGE, [block_pos[0]+BLOCK_SIZE/2, block_pos[1]+BLOCK_SIZE/2], BLOCK_SIZE/2)


	return block_pos;

def draw_background(screen):
	checker = True

	for x in range(int(SCREEN_WIDTH/BLOCK_SIZE)):
		for y in range (int(SCREEN_HEIGHT/BLOCK_SIZE)):
			if checker:
				pygame.draw.rect(screen, DARK_GREEN, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)) 
				checker = False
			else :
				checker = True

	pygame.draw.lines(screen, WHITE, True, [[BLOCK_SIZE,BLOCK_SIZE], [BLOCK_SIZE, SCREEN_HEIGHT - BLOCK_SIZE - 2], 
			[SCREEN_WIDTH - BLOCK_SIZE - 2, SCREEN_HEIGHT - BLOCK_SIZE - 2], [SCREEN_WIDTH - BLOCK_SIZE - 2, BLOCK_SIZE]], 2)

def end_screen(screen, font_title, font_small):

	draw_text(screen, 'GAME OVER', WHITE, font_title, SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
	draw_text(screen, 'Press Space Play Again', WHITE, font_small, SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 60)
	draw_text(screen, 'or enter to go back', WHITE, font_small, SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 85)

	pygame.display.update()

	time.sleep(0.5)

	while True:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

			if event.type == pygame.KEYDOWN:
				if (event.key == pygame.K_RETURN):
					return False
				elif (event.key == pygame.K_SPACE):
					return True	

def draw_wall(screen, wall, block_swallowed, snake):

	if (block_swallowed and snake.score % 2 == 1) :
		spot_taken = True
		while spot_taken :
			spot_taken = False
			x = random.randint(1, int(SCREEN_WIDTH/BLOCK_SIZE) - 2) * BLOCK_SIZE
			y = random.randint(1, int(SCREEN_HEIGHT/BLOCK_SIZE) - 2) * BLOCK_SIZE

			# Check if the wall is in the snake
			for j in range(len(snake.position)):
				if (x == snake.position[j][0] and y == snake.position[j][1]):
					spot_taken = True

		wall.append([x, y])

	for i in range(len(wall) - 1):
		pygame.draw.rect(screen, BLACK, (wall[i + 1][0], wall[i + 1][1], BLOCK_SIZE, BLOCK_SIZE), border_radius = 10)
		pygame.draw.rect(screen, WHITE, (wall[i + 1][0], wall[i + 1][1], BLOCK_SIZE, BLOCK_SIZE), 2, border_radius = 10)


'''                            '''
'''    DIFFERENT GAME MODES    '''
'''                            '''

def play_game(screen, font, font_title, font_small, sound_block, speed):

	# VARIABLES USED
	block_pos = [-1,-1]
	pause = False
	block_swallowed_bool = True
	collision = False
	color_switch = True
	player = snake.snake([[3 * BLOCK_SIZE, SCREEN_HEIGHT - 3 * BLOCK_SIZE], [4 * BLOCK_SIZE, SCREEN_HEIGHT - 3 * BLOCK_SIZE], 
						[5 * BLOCK_SIZE, SCREEN_HEIGHT - 3 * BLOCK_SIZE], [6 * BLOCK_SIZE, SCREEN_HEIGHT - 3 * BLOCK_SIZE]],
						0, RED, BRIGHT_RED)
	# FOR TESTING, change so this handles all speed scores, and implement in other game modes as well
	game_mode = "Clas_" + str(format(speed, '.2f'))
	high_score = read_high_score(game_mode)

	while True:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					pause = False

		while not pause:

			screen.fill(GREEN)
			draw_background(screen)
			time.sleep(speed)

			for event in pygame.event.get():
			
				if event.type == pygame.QUIT:
					sys.exit()

				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_RIGHT:
						if player.previous_move != 2 :
							player.move = 0
					elif event.key == pygame.K_DOWN:
						if player.previous_move !=3 :
							player.move = 1
					elif event.key == pygame.K_LEFT:
						if player.previous_move != 0 :	
							player.move = 2
					elif event.key == pygame.K_UP:
						if  player.previous_move != 1 :	
							player.move = 3
					elif event.key == pygame.K_SPACE:
						pause = True

			player.position = player.move_player(block_swallowed_bool, screen)

			if color_switch :
				color_switch = False
			else :
				color_switch = True
				
			block_pos = create_block(block_pos, block_swallowed_bool, screen, color_switch, player)
			block_swallowed_bool = player.block_swallowed(block_pos)
			if (block_swallowed_bool):
				sound_block.play()
				player.score += 1
				if (speed > 0.03):
					speed -= 0.0025
			collision = player.collision_manager()
			if (collision) :
				if (int(high_score) < player.score) :
					write_high_score(game_mode, player.score)
				block_swallowed_bool = True
				player.position = player.move_player(block_swallowed_bool, screen)
				draw_text(screen, 'Score: ' + str(player.score), WHITE, font_small, SCREEN_WIDTH/3, 20)
				draw_text(screen, 'High Score: ' + str(high_score), WHITE, font_small, SCREEN_WIDTH/3 * 2, 20)
				return end_screen(screen, font_title, font_small)
				
			draw_text(screen, 'Score: ' + str(player.score), WHITE, font_small, SCREEN_WIDTH/3, 20)
			draw_text(screen, 'High Score: ' + str(high_score), WHITE, font_small, SCREEN_WIDTH/3 * 2, 20)

			
			pygame.display.update()

def play_game_2player(screen, font, font_title, font_small, sound_block, speed):

	# VARIABLES USED
	block_pos = [-1,-1]
	pause = False
	color_switch = True
	block_swallowed_bool = [True, True]
	collision = [False, False]

	# Set up player start parameters
	player = snake.snake([[3 * BLOCK_SIZE, SCREEN_HEIGHT - 3 * BLOCK_SIZE], [4 * BLOCK_SIZE, SCREEN_HEIGHT - 3 * BLOCK_SIZE], 
						[5 * BLOCK_SIZE, SCREEN_HEIGHT - 3 * BLOCK_SIZE], [6 * BLOCK_SIZE, SCREEN_HEIGHT - 3 * BLOCK_SIZE]],
						0, RED, BRIGHT_RED)

	opponent = snake.snake([[SCREEN_WIDTH - 3 * BLOCK_SIZE, 3 * BLOCK_SIZE],[SCREEN_WIDTH - 4 * BLOCK_SIZE, 3 * BLOCK_SIZE],
							[SCREEN_WIDTH - 5 * BLOCK_SIZE, 3 * BLOCK_SIZE],[SCREEN_WIDTH - 6 * BLOCK_SIZE, 3 * BLOCK_SIZE]],
				     		2, PURPLE, BRIGHT_PURPLE)

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					pause = False

		while not pause:
			time.sleep(speed)
			screen.fill(GREEN)
			draw_background(screen)

			for event in pygame.event.get():
			
				if event.type == pygame.QUIT:
					sys.exit()

				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_RIGHT:
						if player.previous_move != 2:
							player.move = 0
					elif event.key == pygame.K_DOWN:
						if player.previous_move != 3:
							player.move = 1
					elif event.key == pygame.K_LEFT:
						if player.previous_move != 0:	
							player.move = 2
					elif event.key == pygame.K_UP:
						if player.previous_move != 1:	
							player.move = 3
					if event.key == pygame.K_d:
						if opponent.previous_move != 2:
							opponent.move = 0
					elif event.key == pygame.K_s:
						if opponent.previous_move != 3:
							opponent.move = 1
					elif event.key == pygame.K_a:
						if opponent.previous_move != 0:	
							opponent.move = 2
					elif event.key == pygame.K_w:
						if opponent.previous_move != 1:	
							opponent.move = 3
					elif event.key == pygame.K_SPACE:
						pause = True


			player.position = player.move_player(block_swallowed_bool[0], screen)
			opponent.position = opponent.move_player(block_swallowed_bool[1], screen)
			
			# Order of function call is set as such to cause an intentional delay between block generation (mainly to mimic the older game and stay true to it)	
			if color_switch :
				color_switch = False
			else :
				color_switch = True

			if (block_swallowed_bool[0] == True or block_swallowed_bool[1] == True):
				block_pos = create_block_2P(block_pos, True, screen, color_switch, player, opponent)
				sound_block.play()
			else:
				block_pos = create_block_2P(block_pos, False, screen, color_switch, player, opponent)
			block_swallowed_bool[0] = player.block_swallowed(block_pos)
			if (block_swallowed_bool[0]):
				player.score += 1	
			block_swallowed_bool[1] = opponent.block_swallowed(block_pos)
			if (block_swallowed_bool[1]):
				opponent.score += 1

			collision[0] = player.collision_manager_2player(opponent)
			collision[1] = opponent.collision_manager_2player(player)

			if (collision[0] == True or collision[1] == True):
				if (collision[0]):
					opponent.score += 5
				if (collision[1]):
					player.score += 5
				block_swallowed_bool = [True, True]
				player.position = player.move_player(block_swallowed_bool, screen)
				opponent.position = opponent.move_player(block_swallowed_bool, screen)
				draw_text(screen, 'Score: ' + str(player.score), WHITE, font_small, SCREEN_WIDTH/3, 20)
				pygame.draw.rect(screen, player.color, (SCREEN_WIDTH/3 - 60, 3, 120, 34), 2, border_radius=15)
				draw_text(screen, 'Score: ' + str(opponent.score), WHITE, font_small, SCREEN_WIDTH/3*2, 20)
				pygame.draw.rect(screen, opponent.color, (SCREEN_WIDTH/3 * 2 - 60, 3, 120, 34), 2, border_radius=15)
				return end_screen(screen, font_title, font_small)
				
			draw_text(screen, 'Score: ' + str(player.score), WHITE, font_small, SCREEN_WIDTH/3, 20)
			pygame.draw.rect(screen, player.color, (SCREEN_WIDTH/3 - 60, 3, 120, 34), 2, border_radius=15)
			draw_text(screen, 'Score: ' + str(opponent.score), WHITE, font_small, SCREEN_WIDTH/3*2, 20)
			pygame.draw.rect(screen, opponent.color, (SCREEN_WIDTH/3 * 2 - 60, 3, 120, 34), 2, border_radius=15)
			
			pygame.display.update()

def play_game_wall(screen, font, font_title, font_small, sound_block, speed):

	# VARIABLES USED
	block_pos = [-1,-1]
	wall = [[]]
	pause = False
	block_swallowed_bool = True
	collision = False
	color_switch = True
	player = snake.snake([[3 * BLOCK_SIZE, SCREEN_HEIGHT - 3 * BLOCK_SIZE], [4 * BLOCK_SIZE, SCREEN_HEIGHT - 3 * BLOCK_SIZE],
						[5 * BLOCK_SIZE, SCREEN_HEIGHT - 3 * BLOCK_SIZE], [6 * BLOCK_SIZE, SCREEN_HEIGHT - 3 * BLOCK_SIZE]],
						0, RED, BRIGHT_RED)
	game_mode = "Wall_" + str(format(speed, '.2f'))
	high_score = read_high_score(game_mode)

	while True:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					pause = False

		while not pause:

			time.sleep(speed)
			screen.fill(GREEN)
			draw_background(screen)

			for event in pygame.event.get():

				if event.type == pygame.QUIT:
					sys.exit()

				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_RIGHT:
						if player.previous_move != 2 :
							player.move = 0
					elif event.key == pygame.K_DOWN:
						if player.previous_move !=3 :
							player.move = 1
					elif event.key == pygame.K_LEFT:
						if player.previous_move != 0 :
							player.move = 2
					elif event.key == pygame.K_UP:
						if  player.previous_move != 1 :
							player.move = 3
					elif event.key == pygame.K_SPACE:
						pause = True

			player.position = player.move_player(block_swallowed_bool, screen)

			if color_switch :
				color_switch = False
			else :
				color_switch = True


			block_pos = create_block_wall(block_pos, block_swallowed_bool, screen, color_switch, wall, player)
			draw_wall(screen, wall, block_swallowed_bool, player)
			
			block_swallowed_bool = player.block_swallowed(block_pos)
			if (block_swallowed_bool):
				sound_block.play()
				player.score += 1
				if (speed > 0.03):
					speed -= 0.0025


			collision = player.collision_manager_wall(wall)
			if (collision):
				block_swallowed_bool = True
				if (int(high_score) < player.score) :
					write_high_score(game_mode, player.score)
				player.position = player.move_player(block_swallowed_bool, screen)
				draw_text(screen, 'Score: ' + str(player.score), WHITE, font_small, SCREEN_WIDTH/3, 20)
				draw_text(screen, 'High Score: ' + str(high_score), WHITE, font_small, SCREEN_WIDTH/3 * 2, 20)
				return end_screen(screen, font_title, font_small)

			draw_text(screen, 'Score: ' + str(player.score), WHITE, font_small, SCREEN_WIDTH/3, 20)
			draw_text(screen, 'High Score: ' + str(high_score), WHITE, font_small, SCREEN_WIDTH/3 * 2, 20)

			pygame.display.update()

# NOT YET USED, WORKS TO CONTROL SNAKE BUT IS VERY DUMB 
def play_game_auto(screen, font, font_title, font_small, sound_block, speed):

	# VARIABLES USED
	block_pos = [-1,-1]
	pause = False
	block_swallowed_bool = True
	collision = False
	color_switch = True
	player = snake.snake([[3 * BLOCK_SIZE, SCREEN_HEIGHT - 3 * BLOCK_SIZE], [4 * BLOCK_SIZE, SCREEN_HEIGHT - 3 * BLOCK_SIZE],
						[5 * BLOCK_SIZE, SCREEN_HEIGHT - 3 * BLOCK_SIZE], [6 * BLOCK_SIZE, SCREEN_HEIGHT - 3 * BLOCK_SIZE]],
						0, RED, BRIGHT_RED)

	while True:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					pause = False

		while not pause:

			time.sleep(speed)
			screen.fill(GREEN)
			draw_border(screen)

			for event in pygame.event.get():

				if event.type == pygame.QUIT:
					sys.exit()


			player.move = player.get_move(block_pos)
			player.position = player.move_player(block_swallowed_bool, screen)

			if color_switch :
				color_switch = False
			else :
				color_switch = True

			block_pos = create_block(block_pos, block_swallowed_bool, screen, color_switch)
			block_swallowed_bool = player.block_swallowed(block_pos)
			if (block_swallowed_bool):
				sound_block.play()
				player.score += 1
				if (speed > 0.03):
					speed -= 0.0025
			collision = player.collision_manager()
			if (collision):
				block_swallowed_bool = True
				player.position = player.move_player(block_swallowed_bool, screen)
				draw_text(screen, 'Score: ' + str(player.score), WHITE, font_small, SCREEN_WIDTH/2, 20)
				return end_screen(screen, font_title, font_small)

			draw_text(screen, 'Score: ' + str(player.score), WHITE, font_small, SCREEN_WIDTH/2, 20)

			pygame.display.update()

