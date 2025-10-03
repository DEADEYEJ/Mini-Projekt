import math
import pygame
import datetime


pygame.init()
screen = pygame.display.set_mode((900, 600))
hand_surface = pygame.Surface((900, 600), pygame.SRCALPHA)
screen.fill((0, 0, 0))
Colour_R = (255, 0, 0)
Colour_W = (255, 255, 255)
Colour_G = (0, 255, 0)

def Clock_outline():
    for angle in range(0, 360, 30):
        start_point = (450, 300)
        length = 185
        end_x = start_point[0] + length * math.cos(math.radians(angle))
        end_y = start_point[1] + length * math.sin(math.radians(angle))
        end_point = (end_x, end_y)
        pygame.draw.line(screen, Colour_R, start_point, end_point, 1)

    for angle in range(0, 360, 6):
        start_point = (450, 300)
        length = 170
        end_x = start_point[0] + length * math.cos(math.radians(angle))
        end_y = start_point[1] + length * math.sin(math.radians(angle))
        end_point = (end_x, end_y)
        pygame.draw.line(screen, (200, 200, 200), start_point, end_point, 1)

    pygame.draw.circle(screen, (255, 255, 255), (450, 300), 186, 1)
    pygame.draw.circle(screen, (255, 255, 255), (450, 300), 171, 1) # Draws outline for minutes
    pygame.draw.circle(screen, (0, 0, 0), (450, 300), 160, 0) # Circle to hide the lines


def Hands(length, radians, colour):
    start_hour_point = (450, 300)
    length_hour = length
    end_hour_x = start_hour_point[0] + length_hour * math.cos(math.radians(radians))
    end_hour_y = start_hour_point[1] + length_hour * math.sin(math.radians(radians))
    end_hour_point = (end_hour_x, end_hour_y)
    pygame.draw.line(hand_surface, (colour), start_hour_point, end_hour_point, 1)
    screen.blit(hand_surface, (0, 0))


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    current_time = datetime.datetime.now()

    hour = (current_time.hour + current_time.minute / 60) * 30 - 90
    minute = (current_time.minute + current_time.second / 60) * 6 - 90
    second = current_time.second * 6 - 90

    hand_surface.fill((0, 0, 0, 0))  # Clear with transparency

    Clock_outline()
    Hands(150, second, Colour_R)
    Hands(125, minute, Colour_W)
    Hands(75, hour, Colour_W)
    
    pygame.display.flip()



