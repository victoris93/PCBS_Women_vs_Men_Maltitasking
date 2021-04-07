#! /usr/bin/env python
# Author: Victoria Shevchenko

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

# Field coordinates
def draw_stimulus_field(offset_1, offset_2):
	field_x_corner, field_y_corner = offset_1, offset_2
	field_width, field_height = W - 2 * offset_1, H - 2 * offset_2
	pygame.draw.rect(screen, YELLOW, (field_x_corner, field_y_corner, field_width, field_height), 1)
	pygame.draw.line(screen, YELLOW, (offset_1, H // 2), (W - offset_1, H // 2), 1)
	
draw_stimulus_field(50, 50)

print(len('SHAPE'))

def top_screen_label(label):
	myfont=pygame.font.SysFont(pygame.font.get_fonts()[0], 40)
	line = myfont.render(label, 1, pygame.Color('YELLOW'))
	screen.blit(line, ((W - 20 * len(label)) // 2, 0))

def bottom_screen_label(label):
	myfont=pygame.font.SysFont(pygame.font.get_fonts()[0], 40)
	line = myfont.render(label, 1, pygame.Color('YELLOW'))
	screen.blit(line, ((W - 20 * len(label)) // 2, H - 50)) 


top_screen_label('SHAPE')
bottom_screen_label('FILLING')

# The SHAPE task: 
	
def generate_shape_square_3_circles():
	#The figure: square with 3 circles for the shape task
	square_left, square_top = ((W - W // 5) // 2), (((H // 2) - H // 5) // 2) 
	square_right, square_bottom = W // 5, H // 5
	pygame.draw.rect(screen, YELLOW, (square_left, square_top, square_right, square_bottom), 7)
	pygame.draw.circle(screen, YELLOW, (W // 2, H // 4), 20)
	pygame.draw.circle(screen, YELLOW, (W // 2, H // 4 - 50), 20)	
	pygame.draw.circle(screen, YELLOW, (W // 2, H // 4 + 50), 20)
	pygame.display.flip()
	pygame.image.save(screen, "shape_square_3_circles.png")
	
def generate_shape_square_2_circles():
	#The figure: square with 3 circles for the shape task
	square_left, square_top = ((W - W // 5) // 2), (((H // 2) - H // 5) // 2) 
	square_right, square_bottom = W // 5, H // 5
	pygame.draw.rect(screen, YELLOW, (square_left, square_top, square_right, square_bottom), 7)
	pygame.draw.circle(screen, YELLOW, (W // 2, H // 4 - 25), 20)	
	pygame.draw.circle(screen, YELLOW, (W // 2, H // 4 + 25), 20)
	pygame.display.flip()
	pygame.image.save(screen, "shape_square_2_circles.png")

def generate_shape_diamond_3_circles():
	#The figure: diamond with 3 circles for the shape task
	diamond_point_1 = W // 2, H // 4 - H // 5 * math.sin(math.pi/4)
	diamond_point_2 = W // 2 - W // 5 * math.sin(math.pi/4), H // 4
	diamond_point_3 = W // 2, H // 4 + H // 5 * math.sin(math.pi/4)
	diamond_point_4 = W // 2 + W // 5 * math.sin(math.pi / 4), H // 4
	pygame.draw.polygon(screen, YELLOW, (diamond_point_1, diamond_point_2, diamond_point_3, diamond_point_4), 7)
	pygame.draw.circle(screen, YELLOW, (W // 2, H // 4), 20)
	pygame.draw.circle(screen, YELLOW, (W // 2, H // 4 - 50), 20)	
	pygame.draw.circle(screen, YELLOW, (W // 2, H // 4 + 50), 20)
	pygame.display.flip()
	pygame.image.save(screen, "shape_diamond_3_circles.png")
	
def generate_shape_diamond_2_circles():
	#The figure: diamond with 3 circles for the shape task
	diamond_point_1 = W // 2, H // 4 - H // 5 * math.sin(math.pi/4)
	diamond_point_2 = W // 2 - W // 5 * math.sin(math.pi/4), H // 4
	diamond_point_3 = W // 2, H // 4 + H // 5 * math.sin(math.pi/4)
	diamond_point_4 = W // 2 + W // 5 * math.sin(math.pi / 4), H // 4
	pygame.draw.polygon(screen, YELLOW, (diamond_point_1, diamond_point_2, diamond_point_3, diamond_point_4), 7)
	pygame.draw.circle(screen, YELLOW, (W // 2, H // 4 - 25), 20)	
	pygame.draw.circle(screen, YELLOW, (W // 2, H // 4 + 25), 20)
	pygame.display.flip()
	pygame.image.save(screen, "shape_diamond_2_circles.png")

# The FILLING task: 
def generate_filling_square_3_circles():
	#The figure: square with 3 circles for the shape task
	square_left, square_top = ((W - W // 5) // 2, H - (H // 4 + H // 10))
	square_right, square_bottom = W // 5, H // 5
	pygame.draw.rect(screen, YELLOW, (square_left, square_top, square_right, square_bottom), 7)
	pygame.draw.circle(screen, YELLOW, (W // 2, H - H // 4), 20)
	pygame.draw.circle(screen, YELLOW, (W // 2, H - H // 4 - 50), 20)	
	pygame.draw.circle(screen, YELLOW, (W // 2, H - H // 4 + 50), 20)
	pygame.display.flip()
	pygame.image.save(screen, "filling_square_3_circles.png")
	
def generate_filling_square_2_circles():
	#The figure: square with 3 circles for the shape task
	square_left, square_top = ((W - W // 5) // 2, H - (H // 4 + H // 10))
	square_right, square_bottom = W // 5, H // 5
	pygame.draw.rect(screen, YELLOW, (square_left, square_top, square_right, square_bottom), 7)
	pygame.draw.circle(screen, YELLOW, (W // 2, H - H // 4 - 25), 20)	
	pygame.draw.circle(screen, YELLOW, (W // 2, H - H // 4 + 25), 20)
	pygame.display.flip()
	pygame.image.save(screen, "filling_square_2_circles.png")

def generate_filling_diamond_3_circles():
	#The figure: diamond with 3 circles for the shape task
	diamond_point_1 = W // 2, H // 2 + (H // 4 - H // 5 * math.sin(math.pi/4))
	diamond_point_2 = W // 2 - W // 5 * math.sin(math.pi/4), H - H // 4
	diamond_point_3 = W // 2, H - H // 4 + H // 5 * math.sin(math.pi/4)
	diamond_point_4 = W // 2 + W // 5 * math.sin(math.pi / 4), H - H // 4
	pygame.draw.polygon(screen, YELLOW, (diamond_point_1, diamond_point_2, diamond_point_3, diamond_point_4), 7)
	pygame.draw.circle(screen, YELLOW, (W // 2, H - H // 4), 20)
	pygame.draw.circle(screen, YELLOW, (W // 2, H - H // 4 - 50), 20)	
	pygame.draw.circle(screen, YELLOW, (W // 2, H - H // 4 + 50), 20)
	pygame.display.flip()
	pygame.image.save(screen, "filling_diamond_3_circles.png")
	
def generate_filling_diamond_2_circles():
	#The figure: diamond with 3 circles for the shape task
	diamond_point_1 = W // 2, H // 2 + (H // 4 - H // 5 * math.sin(math.pi/4))
	diamond_point_2 = W // 2 - W // 5 * math.sin(math.pi/4), H - H // 4
	diamond_point_3 = W // 2, H - H // 4 + H // 5 * math.sin(math.pi/4)
	diamond_point_4 = W // 2 + W // 5 * math.sin(math.pi / 4), H - H // 4
	pygame.draw.polygon(screen, YELLOW, (diamond_point_1, diamond_point_2, diamond_point_3, diamond_point_4), 7)
	pygame.draw.circle(screen, YELLOW, (W // 2, H - H // 4 - 25), 20)	
	pygame.draw.circle(screen, YELLOW, (W // 2, H - H // 4 + 25), 20)
	pygame.display.flip()
	pygame.image.save(screen, "filling_diamond_2_circles.png")

generate_shape_square_3_circles()	

done = False
while not done:
        pygame.time.wait(100)
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
