
'''        
	****	SNAKE	****
	
  	Snake class, one is created through each game mode, default values are used for player one, red snake and opponent needs to be reset
  	- This class seems pretty complete!

'''

import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BLOCK_SIZE = 40
WHITE = (255, 255, 255)
DARK_BLUE = (0, 0, 75)


class snake:
	position = [[400, 320], [400 + BLOCK_SIZE, 320], [400 + (2 * BLOCK_SIZE), 320], [400 + (3 * BLOCK_SIZE), 320]]
	move = 0
	previous_move = 0
	score = 0
	color = WHITE
	secondary_color = WHITE

	def __init__ (self, position, start_direction, color, secondary_color):
		self.position = position
		self.move = self.previous_move = start_direction
		self.color = color
		self.secondary_color = secondary_color

	def move_player(self, block_swallowed_bool, screen):
		head_snake = len(self.position) - 1


		#  Player move index: 0 = right, 1 = down, 2 = left, 3 = up
		if (self.move == 0): # and self.previous_move != 2
				self.position.append([self.position[head_snake][0] + BLOCK_SIZE, self.position[head_snake][1]])
				self.previous_move = 0
		elif (self.move == 1): # and self.previous_move != 3
			self.position.append([self.position[head_snake][0], self.position[head_snake][1] + BLOCK_SIZE])
			self.previous_move = 1
		elif (self.move == 2): # and self.previous_move != 0
			self.position.append([self.position[head_snake][0] - BLOCK_SIZE, self.position[head_snake][1]])
			self.previous_move = 2
		elif (self.move == 3): # and self.previous_move != 1
			self.position.append([self.position[head_snake][0], self.position[head_snake][1] - BLOCK_SIZE])
			self.previous_move = 3

		if (block_swallowed_bool == False):
			del self.position[0]

			for i in range(len(self.position)):
				pygame.draw.rect(screen, self.color, (self.position[i][0], self.position[i][1], BLOCK_SIZE - ((len(self.position) - i)/6), BLOCK_SIZE - ((len(self.position) - i)/6)), border_radius=10)
				pygame.draw.rect(screen, DARK_BLUE, (self.position[i][0], self.position[i][1], BLOCK_SIZE - ((len(self.position) - i)/6), BLOCK_SIZE - ((len(self.position) - i)/6)), 1, border_radius=10)

		else :

			for i in range(len(self.position)):
				pygame.draw.rect(screen, self.secondary_color, (self.position[i][0], self.position[i][1], BLOCK_SIZE - ((len(self.position) - i)/6), BLOCK_SIZE - ((len(self.position) - i)/6)), border_radius=10)
				pygame.draw.rect(screen, DARK_BLUE, (self.position[i][0], self.position[i][1], BLOCK_SIZE - ((len(self.position) - i)/6), BLOCK_SIZE - ((len(self.position) - i)/6)), 1, border_radius=10)

		return self.position


	def collision_manager(self):
		# Collision with screen
		if (self.position[len(self.position)-1][0] <= 0 and self.move == 2 or self.position[len(self.position)-1][0] >= SCREEN_WIDTH - BLOCK_SIZE and self.move == 0
			or self.position[len(self.position)-1][1] <= 0 and self.move == 3 or self.position[len(self.position)-1][1] >= SCREEN_HEIGHT - BLOCK_SIZE and self.move == 1):
			return True


		# Collision with self
		for i in range(len(self.position)-1):
			if (self.position[len(self.position)-1][0] == self.position[i][0] and self.position[len(self.position)-1][1] == self.position[i][1]):
				return True

		return False

	def collision_manager_wall(self, wall):
		# Collision with screen
		if (self.position[len(self.position)-1][0] <= 0 and self.move == 2 or self.position[len(self.position)-1][0] >= SCREEN_WIDTH - BLOCK_SIZE and self.move == 0
			or self.position[len(self.position)-1][1] <= 0 and self.move == 3 or self.position[len(self.position)-1][1] >= SCREEN_HEIGHT - BLOCK_SIZE and self.move == 1):
			return True


		# Collision with self
		for i in range(len(self.position)-1):
			if (self.position[len(self.position)-1][0] == self.position[i][0] and self.position[len(self.position)-1][1] == self.position[i][1]):
				return True

		# Collision with wall
		for j in range(len(wall) - 1):
			if (self.position[len(self.position)-1][0] == wall[j + 1][0] and self.position[len(self.position)-1][1] == wall[j + 1][1]):
				return True

		return False

	def collision_manager_2player(self, snake):


		# Collision with screen
		if (self.position[len(self.position)-1][0] <= 0 and self.move == 2 or self.position[len(self.position)-1][0] >= SCREEN_WIDTH - BLOCK_SIZE and self.move == 0
			or self.position[len(self.position)-1][1] <= 0 and self.move == 3 or self.position[len(self.position)-1][1] >= SCREEN_HEIGHT - BLOCK_SIZE and self.move == 1):
			return True


		# Collision with self
		for i in range(len(self.position)-1):
			if (self.position[len(self.position)-1][0] == self.position[i][0] and self.position[len(self.position)-1][1] == self.position[i][1]):
				return True

		# Collision with other snake
		for j in range(len(snake.position)):
			if (self.position[len(self.position)-1][0] == snake.position[j][0] and self.position[len(self.position)-1][1] == snake.position[j][1]):
				return True

		return False

	def block_swallowed(self, block_pos):
		if (block_pos == self.position[len(self.position)-1]):
			return True

		return False

		
