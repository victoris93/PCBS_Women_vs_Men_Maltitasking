# Author: Victoria Shevchenko

"""The present script generates png images and names them based on the task they correspond to. Thus, an image that contains a stimulus with a square frame with two circles inside and which requires you to determine the shape of the frame is named shape_square_2_circles.png. Tasks and responses combined together yield 8 stimuli. Separate function are defined to generate needed shapes given the task and the number of circles within the shape. These functions are further used by other functions which generate and save the imagesin the "Stimuli" folder."""

import os
import pygame 
import math

BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

H = 900
W = 900

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((W, H), pygame.DOUBLEBUF)
screen.fill(BLACK)

STIM_DIR = 'Stimuli/'

def draw_stimulus_field(offset_1, offset_2):
	field_x_corner, field_y_corner = offset_1, offset_2
	field_width, field_height = W - 2 * offset_1, H - 2 * offset_2
	pygame.draw.rect(screen, YELLOW, (field_x_corner, field_y_corner, field_width, field_height), 1)
	pygame.draw.line(screen, YELLOW, (offset_1, H // 2), (W - offset_1, H // 2), 1)

def screen_labels(label1, label2, stimulus_field_offset):
	label_font=pygame.font.SysFont(pygame.font.get_fonts()[0], 40)
	top_label = label_font.render(label1, 1, pygame.Color('YELLOW'))
	screen.blit(top_label, ((W - 20 * len(label1)) // 2, 0))
	bottom_label = label_font.render(label2, 1, pygame.Color('YELLOW'))
	screen.blit(bottom_label, ((W - 20 * len(label2)) // 2, H - stimulus_field_offset))
	
def draw_square(task_type):
	square_left, square_right = ((W - W // 5) // 2), W // 5
	square_bottom = H // 5
	if task_type == "shape":
		square_top = ((H // 2) - H // 5) // 2
	elif task_type == "filling":
		square_top = H - (H // 4 + H // 10)
	pygame.draw.rect(screen, YELLOW, (square_left, square_top, square_right, square_bottom), 7)
	
def draw_diamond(task_type):
		x1 = W // 2
		x2 = W // 2 - W // 5 * math.sin(math.pi/4)
		x3 = W // 2
		x4 = W // 2 + W // 5 * math.sin(math.pi / 4)
		if task_type == "shape":
			y1 = H // 4 - H // 5 * math.sin(math.pi/4)
			y2 = H // 4
			y3 = H // 4 + H // 5 * math.sin(math.pi/4)
			y4 = H // 4
		elif task_type == "filling":
			y1 = H // 2 + (H // 4 - H // 5 * math.sin(math.pi/4))
			y2 = H - H // 4
			y3 = H - H // 4 + H // 5 * math.sin(math.pi/4)
			y4 = H - H // 4
		point_1 = x1, y1
		point_2 = x2, y2
		point_3 = x3, y3
		point_4 = x4, y4
		pygame.draw.polygon(screen, YELLOW, (point_1, point_2, point_3, point_4), 7)

def draw_3_circles(task_type):
		center_x = W // 2
		if task_type == "shape":
			upper_center_y = H // 4 - 50
			middle_center_y = H // 4
			lower_center_y = H // 4 + 50
		elif task_type == "filling":
			upper_center_y = H - H // 4 - 50
			middle_center_y = H - H // 4
			lower_center_y = H - H // 4 + 50
		center_y_coordinates = [upper_center_y, middle_center_y, lower_center_y]
		for center_y in center_y_coordinates:
			pygame.draw.circle(screen, YELLOW, (center_x, center_y), 20)

def draw_2_circles(task_type):
		center_x = W // 2
		if task_type == "shape":
			upper_center_y = H // 4 - 25
			lower_center_y = H // 4 + 25
		elif task_type == "filling":
			upper_center_y = H - H // 4 - 25
			lower_center_y =  H - H // 4 + 25
		center_y_coordinates = [upper_center_y, lower_center_y]
		for center_y in center_y_coordinates:
			pygame.draw.circle(screen, YELLOW, (center_x, center_y), 20)
	
def shape_task(frame, circle_number):
	filename = os.path.join(STIM_DIR,"shape_{}_{}_circles.png".format(frame, circle_number))
	if frame == "square": 
		draw_square("shape")
	elif frame == "diamond": 
		draw_diamond("shape")
	if circle_number == 2:
		draw_2_circles("shape")
	elif  circle_number == 3:
		draw_3_circles("shape")
	pygame.display.flip()
	pygame.image.save(screen, filename)
	
def filling_task(frame, circle_number):
	filename = os.path.join(STIM_DIR, "filling_{}_{}_circles.png".format(frame, circle_number))
	if frame == "square": 
		draw_square("filling")
	elif frame == "diamond": 
		draw_diamond("filling")
	if circle_number == 2:
		draw_2_circles("filling")
	elif  circle_number == 3:
		draw_3_circles("filling")
	pygame.display.flip()
	pygame.image.save(screen, filename)

for task in [shape_task, filling_task]:
	for frame in ["square", "diamond"]: 	
		for circle_number in [2, 3]:
			draw_stimulus_field(50, 50)
			screen_labels("SHAPE", "FILLING", 50)
			task(frame, circle_number)
			screen.fill((0,0,0))
			pygame.display.flip()