#!/usr/bin/env python2

import pygame
import random

WIDTH = 1280
HEIGHT = 720
FPS = 30

# Define Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

## initialize pygame and create window
pygame.init()
pygame.mixer.init()  ## For sound
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Times Tables")
clock = pygame.time.Clock()  ## For syncing the FPS

## group all the sprites together for ease of update

font = pygame.font.SysFont(None, 200)


## Game loop
running = True
numbers_entered = ''
time_table_number = 3
time_table_random = random.randrange(1, 13)
number_flip = random.randrange(0,2)
while running:

	# 1 Process input/events
	clock.tick(FPS)  ## will make the loop run at the same speed all the time
	for event in pygame.event.get():  # gets all the events which have occured till now and keeps tab of them.
		## listening for the the X button at the top
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_KP0:
				numbers_entered+= "0"
			if event.key == pygame.K_KP1:
				numbers_entered+= "1"
			if event.key == pygame.K_KP2:
				numbers_entered+= "2"
			if event.key == pygame.K_KP3:
				numbers_entered+= "3"
			if event.key == pygame.K_KP4:
				numbers_entered+= "4"
			if event.key == pygame.K_KP5:
				numbers_entered+= "5"
			if event.key == pygame.K_KP6:
				numbers_entered+= "6"
			if event.key == pygame.K_KP7:
				numbers_entered+= "7"
			if event.key == pygame.K_KP8:
				numbers_entered+= "8"
			if event.key == pygame.K_KP9:
				numbers_entered+= "9"
			if event.key == pygame.K_BACKSPACE:
				if len(numbers_entered) > 0:

					numbers_entered = numbers_entered[:-1]




	# 2 Update

	if numbers_entered != "":

		if time_table_random * time_table_number == int(numbers_entered):
			time_table_random = random.randrange(1, 12)

			numbers_entered = ""
			if number_flip == 1:
				number_flip = 0
			else:
				number_flip += 1


	# clear numbers entered

	if number_flip == 0:
		multiplication_problem = font.render('{0} X {1} ='.format(time_table_number, time_table_random), True, WHITE)
	else:
		multiplication_problem = font.render('{0} X {1} ='.format(time_table_random, time_table_number), True, WHITE)


	answer_text = font.render(numbers_entered, True, WHITE)


	# 3 Draw/render
	screen.fill(BLACK)

	########################

	screen.blit(multiplication_problem, (325, 300))
	screen.blit(answer_text, (800, 300))
	########################

	## Done after drawing everything to the screen
	pygame.display.flip()

pygame.quit()