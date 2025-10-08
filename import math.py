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

        end_x_2 = start_point[0] + (length + 15) * math.cos(math.radians(angle)) # draws the second x point to the line
        end_y_2 = start_point[1] + (length + 15) * math.sin(math.radians(angle)) # Does the same for y
        end_point_2 = (end_x_2, end_y_2)

        end_x = start_point[0] + length * math.cos(math.radians(angle)) # draws the first x point to the line
        end_y = start_point[1] + length * math.sin(math.radians(angle)) # does the same but for y
        end_point = (end_x, end_y)
        pygame.draw.line(hand_surface, Colour_R, end_point_2, end_point, 1) # draws the line using the two points

    for angle in range(0, 360, 6):
        start_point = (450, 300)
        length = 170

        end_x_2 = start_point[0] + (length + 15) * math.cos(math.radians(angle)) # does the same as the line 19
        end_y_2 = start_point[1] + (length + 15) * math.sin(math.radians(angle))
        end_point_2 = (end_x_2, end_y_2)

        end_x = start_point[0] + length * math.cos(math.radians(angle))
        end_y = start_point[1] + length * math.sin(math.radians(angle))
        end_point = (end_x, end_y)
        pygame.draw.line(hand_surface, (200, 200, 200), end_point_2, end_point, 1)

    pygame.draw.circle(hand_surface, (Colour_W), (450, 300), 201, 1)
    pygame.draw.circle(hand_surface, (Colour_W), (450, 300), 186, 1) # visual coolness
    pygame.draw.circle(hand_surface, (Colour_W), (450, 300), 171, 1) # Draws outline for minutes


def Hands(length, radians, colour):
    start_hour_point = (450, 300)
    length_hour = length
    end_hour_x = start_hour_point[0] + length_hour * math.cos(math.radians(radians)) # Math for the hand x positions
    end_hour_y = start_hour_point[1] + length_hour * math.sin(math.radians(radians)) # Math for the hand y positions
    end_hour_point = (end_hour_x, end_hour_y)
    pygame.draw.line(hand_surface, (colour), start_hour_point, end_hour_point, 1) # Drawing the hand thingys
    screen.blit(hand_surface, (0, 0))


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    current_time = datetime.datetime.now()

    hour = (current_time.hour + current_time.minute / 60) * 30 - 90 # defines the hour of the day and some math to make it work
    minute = (current_time.minute + current_time.second / 60) * 6 - 90 # samething as line 65 but for minutes
    second = current_time.second * 6 - 90 # same as line 65 but for seconds - Vi minuser 90 så viserne starter i toppen

    hand_surface.fill((0, 0, 0))

    Clock_outline() # draws the outline of the circle
    Hands(150, second, Colour_R) # draws the seconds hand
    Hands(125, minute, Colour_W) # draws the minutes hand
    Hands(75, hour, Colour_W) # draws the hours hand
    
    

    pygame.display.flip() # updates display



