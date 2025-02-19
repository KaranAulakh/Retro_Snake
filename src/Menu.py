'''                    
    ****   MENU    ****        
                    
	Handles rendering of each menu page
	- A better solution would be to create a button class that can be used to store each button and easily displayed using the menu
 	- The controls also be treated as a button (or multiple) for simplicity
'''

import pygame
import time
import sys

SCREEN_HEIGHT = 600
SCREEN_CENTER_X_POS = 400

BUTTON_LEFT_X_POS = 270
BUTTON_RIGHT_X_POS = 530
BUTTON_WIDTH = 260
BUTTON_HEIGHT = 100

DARK_GREEN = (0, 75, 0)
GREEN = (0, 110, 0)
WHITE = (200, 200, 200)
GRAY = (160, 160, 160)

class Menu: 

	font = None
	font_title = None
	font_small = None
	screen = None
	color_switch = True

	def __init__(self, font, font_title, font_small, screen):
		self.font = font
		self.font_title = font_title
		self.font_small = font_small
		self.screen = screen

	def draw_text(self, screen, text, color, font, pos_x, pos_y):
		text = font.render(text, True, color)
		text_rect = text.get_rect(center=(pos_x, pos_y))
		screen.blit(text, text_rect)

	# X coordinates are same for all buttons, but I need y coordinates and mouse_pos
	def is_mouse_over(self, y, mouse_pos):
		return BUTTON_LEFT_X_POS < mouse_pos[0] < BUTTON_RIGHT_X_POS and y < mouse_pos[1] < y + BUTTON_HEIGHT

	# Use the number of buttons and current button number to determine the y position of the given button
	# Add 15 and an extra option to space down from the title
	def get_button_y_pos(self, button_num, num_options):
		return SCREEN_HEIGHT / (num_options + 1) * (button_num + 1) + 15

	# The title switches between two colors to give it the retro look
	def draw_game_title(self):
		if self.color_switch: 
			self.color_switch = False
			self.draw_text(self.screen, "RETRO SNAKE", GRAY, self.font_title, SCREEN_CENTER_X_POS, 70)	
		else:
			self.color_switch = True	
			self.draw_text(self.screen, "RETRO SNAKE", WHITE, self.font_title, SCREEN_CENTER_X_POS, 70)	

	# Draws all regular menus given the number or buttons to draw and the text for each button
	def draw_menu(self, num_options, options_text):
		while True:
			# Give the processor some rest
			time.sleep(0.008)
			mouse = pygame.mouse.get_pos()
			self.screen.fill(DARK_GREEN)
			self.draw_game_title()

			# Handles events, quit and mouse clicks, tracks what region the mouse clicked on and returns the appropriate int
			for event in pygame.event.get():		
				if event.type == pygame.QUIT:
					sys.exit()

				if event.type == pygame.MOUSEBUTTONDOWN:
					for i in range(num_options):
						if self.is_mouse_over(self.get_button_y_pos(i, num_options), mouse):
							return i + 1

			# Highlights buttons if the mouse is on top of them
			for i in range(num_options):
				if self.is_mouse_over(self.get_button_y_pos(i, num_options), mouse):
					pygame.draw.rect(self.screen, GREEN, (BUTTON_LEFT_X_POS, self.get_button_y_pos(i, num_options), BUTTON_WIDTH, 80), border_radius=15)
					pygame.draw.rect(self.screen, GRAY, (BUTTON_LEFT_X_POS, self.get_button_y_pos(i, num_options), BUTTON_WIDTH, 80), 2, border_radius=15)
	
			# Draws the list of options given through the parameters
			for i in range(len(options_text)):
					self.draw_text(self.screen, options_text[i], WHITE, self.font, SCREEN_CENTER_X_POS, self.get_button_y_pos(i, num_options) + 40)	

			pygame.display.update()

	# Draws the control menu
	def draw_controls(self):
		while True:
			time.sleep(0.008) 
			mouse = pygame.mouse.get_pos()
			self.screen.fill(DARK_GREEN)
			self.draw_game_title()

			# Handles events, quit and mouse functions 
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()

				if event.type == pygame.MOUSEBUTTONDOWN:
					if self.is_mouse_over(495, mouse):
						return 0

			# Highlights the button the cursor is on top of 
			if self.is_mouse_over(495, mouse):
				pygame.draw.rect(self.screen, GREEN, (BUTTON_LEFT_X_POS, 495, BUTTON_WIDTH, 80), border_radius=15)
				pygame.draw.rect(self.screen, GRAY, (BUTTON_LEFT_X_POS, 495, BUTTON_WIDTH, 80), 2, border_radius=15)

			# Draws the rest of the page
			self.draw_text(self.screen, "CONTROLS", WHITE, self.font, SCREEN_CENTER_X_POS, 220)
			self.draw_text(self.screen, 'Player 1 (Red): move with arrow keys', WHITE, self.font_small, SCREEN_CENTER_X_POS, 250)
			self.draw_text(self.screen, 'Player 2 (Purple): move with w, a, s, and d', WHITE, self.font_small, SCREEN_CENTER_X_POS, 280)
			self.draw_text(self.screen, 'Pause at any time using space', WHITE, self.font_small, SCREEN_CENTER_X_POS, 310)
			self.draw_text(self.screen, 'Back', WHITE, self.font, SCREEN_CENTER_X_POS, 535)	

			pygame.display.update()

