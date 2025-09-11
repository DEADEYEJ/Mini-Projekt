import math
import sys
import pygame
import datetime


pygame.init()
screen = pygame.display.set_mode((900, 600))
screen.fill((0, 0, 0))


for angle in range(0, 360, 30):
    start_point = (450, 300)
    length = 200
    end_x = start_point[0] + length * math.cos(math.radians(angle))
    end_y = start_point[1] + length * math.sin(math.radians(angle))
    end_point = (end_x, end_y)
    pygame.draw.line(screen, (200, 200, 200), start_point, end_point, 1)

for angle in range(0, 360, 6):
    start_point = (450, 300)
    length = 170
    end_x = start_point[0] + length * math.cos(math.radians(angle))
    end_y = start_point[1] + length * math.sin(math.radians(angle))
    end_point = (end_x, end_y)
    pygame.draw.line(screen, (200, 200, 200), start_point, end_point, 1)



pygame.draw.circle(screen, (0, 50, 0), (450, 300), 160, 0)



pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
