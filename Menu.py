

'''                    
    ****   MENU    ****        
                    
	Handles rendering of each menu page
	- In the current usage only one menu object is being created
		- Would it be more helpful to make a page class, and invoke page.render() to showcase it
		- For optimal performance pages can then be creatd and stored in a tree class that point to the next and prev pages
			- For normal gameplay this seems like overkill and unnecessary, however, that seems to be the ideal solution  
'''

import pygame
import time
import sys


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BLOCK_SIZE = 40

DARK_GREEN = (0, 75, 0)
GREEN = (0, 110, 0)
WHITE = (200, 200, 200)
GRAY = (160, 160, 160)

class Menu: 

	font = None
	font_title = None
	font_small = None
	screen = None

	def __init__(self, font, font_title, font_small, screen):
		self.font = font
		self.font_title = font_title
		self.font_small = font_small
		self.screen = screen

	def draw_text(self, screen, text, color, font, pos_x, pos_y):
		text = font.render(text, True, color)
		text_rect = text.get_rect(center=(pos_x, pos_y))
		screen.blit(text, text_rect)

	def draw_menu(self, num_options, options_text):
		color_switch = True

		while True:

			time.sleep(0.008) # Give the processor some rest, can also add a statement to sleep for longer upon unresponsiveness
			mouse = pygame.mouse.get_pos()
			self.screen.fill(DARK_GREEN)


			# Handles events, quit and mouse clicks, tracks what region the mouse clicked on and returns the appropriate int
			for event in pygame.event.get():		
				if event.type == pygame.QUIT:
					sys.exit()

				if event.type == pygame.MOUSEBUTTONDOWN:
					for i in range(num_options):
						if (SCREEN_WIDTH/2 - 130 < mouse[0] < SCREEN_WIDTH/2 + 130 and 
							SCREEN_HEIGHT/(num_options + 1) * (i + 1) + 15 < mouse[1] < SCREEN_HEIGHT/(num_options + 1) * (i + 1) + 95):
							return i + 1

			# Highlights buttons if the mouse is on top of them
			for i in range(num_options):
				if (SCREEN_WIDTH/2 - 130 < mouse[0] < SCREEN_WIDTH/2 + 130 and 
					SCREEN_HEIGHT/(num_options + 1) * (i + 1) + 5 < mouse[1] < SCREEN_HEIGHT/(num_options + 1) * (i + 1) + 105):
					pygame.draw.rect(self.screen, GREEN, (SCREEN_WIDTH/2 - 130, SCREEN_HEIGHT/(num_options + 1) * (i + 1) + 15, 260, 80), border_radius=15)
					pygame.draw.rect(self.screen, GRAY, (SCREEN_WIDTH/2 - 130, SCREEN_HEIGHT/(num_options + 1) * (i + 1) + 15, 260, 80), 2, border_radius=15)

			# Draws the Game Title 
			if color_switch: 
				color_switch = False
				self.draw_text(self.screen, "RETRO SNAKE", GRAY, self.font_title, SCREEN_WIDTH/2, 70)	
			else:
				color_switch = True	
				self.draw_text(self.screen, "RETRO SNAKE", WHITE, self.font_title, SCREEN_WIDTH/2, 70)	
			
			# Draws the list of options given through the parameters
			for i in range(len(options_text)):
					self.draw_text(self.screen, options_text[i], WHITE, self.font, SCREEN_WIDTH/2, SCREEN_HEIGHT/(num_options + 1) * (i + 1) + 55)	

			pygame.display.update()

	# This method does not support changing screen dimensions, will need to fix this when the time comes
	def draw_controls(self):
		color_switch = True

		while True:

			time.sleep(0.008) 
			mouse = pygame.mouse.get_pos()
			self.screen.fill(DARK_GREEN)

			# Handles events, quit and mouse functions 
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()

				if event.type == pygame.MOUSEBUTTONDOWN:
					if (SCREEN_WIDTH/2 - 130 < mouse[0] < SCREEN_WIDTH/2 + 130 and 465 < mouse[1] < 545):
						return 0

			# Highlights the button the cursor is on top of 
			if (SCREEN_WIDTH/2 - 130 < mouse[0] < SCREEN_WIDTH/2 + 130 and 465 < mouse[1] < 545):
				pygame.draw.rect(self.screen, GREEN, (SCREEN_WIDTH/2 - 130, 465, 260, 80), border_radius=15)
				pygame.draw.rect(self.screen, GRAY, (SCREEN_WIDTH/2 - 130, 465, 260, 80), 2, border_radius=15)

			# Draws the Game Title
			if color_switch: 
				color_switch = False
				self.draw_text(self.screen, "RETRO SNAKE", GRAY, self.font_title, SCREEN_WIDTH/2, 70)	
			else:
				color_switch = True	
				self.draw_text(self.screen, "RETRO SNAKE", WHITE, self.font_title, SCREEN_WIDTH/2, 70)

			# Draws the rest of the page
			self.draw_text(self.screen, "CONTROLS", WHITE, self.font, SCREEN_WIDTH/2, 220)
			self.draw_text(self.screen, 'Player 1 (Red): move with arrow keys', WHITE, self.font_small, SCREEN_WIDTH/2, 250)
			self.draw_text(self.screen, 'Player 2 (Purple): move with w, a, s, and d', WHITE, self.font_small, SCREEN_WIDTH/2, 275)
			self.draw_text(self.screen, 'Pause at any time using space', WHITE, self.font_small, SCREEN_WIDTH/2, 300)
			self.draw_text(self.screen, 'Back', WHITE, self.font, SCREEN_WIDTH/2, 505)	

			pygame.display.update()

