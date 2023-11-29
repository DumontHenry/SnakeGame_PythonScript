# Importing the external libraries we need for this 

from random import randint # random number generator package
import time # Time package 
from pygame.locals import *

import pygame # pygame package that includes objects and functions for python

# Configuration
SCREEN_WIDTH = int(input("Enter screen width: "))
SCREEN_HEIGHT = int(input("Enter screen height: "))
HEAD_IMAGE_PATH = input("Enter full path to the head image:")
BODY_IMAGE_PATH = input("Enter full path to the body image:")
FRUIT_IMAGE_PATH = input("Enter full path to the fruit image:")
USER_PSEUDO = input("Enter player's pseudo: ")
SPEED = int(input("Snake speed 1 to 100: "))

# Main booleans 

playing = True
moveUp = moveDown = moveRight = moveLeft = move_init = False

# Other int variables

step = 23
score = 0
length = 2
speed = SPEED



# Lists to store the coordinates of the snake or the starting position of the game.
# x and y = 0 , snake start in the middle of the screen
x_snake_position = [0]
y_snake_position = [0]


# Increasing the size of the list to potentially have 1000 sections for the snake

for i in range(0,1000):

    x_snake_position.append(-100)
    y_snake_position.append(-100)


# Function to check if the snake hits something like fruits or itself
# Caclulate the cordinates of the snake and the snake new cordinates, then calculate if touch itself or the fruit
def collision(x_coordinates_1,y_coordinates_1,x_coordinates_2,y_coordinates_2, size_snake, size_fruit):
    if ((x_coordinates_1 + size_snake >= x_coordinates_2) or (x_coordinates_1 >= x_coordinates_2)) and x_coordinates_1 <= x_coordinates_2 + size_fruit:
        if ((y_coordinates_1 >= y_coordinates_2) or (y_coordinates_1 + size_snake >= y_coordinates_2)) and y_coordinates_1 <= y_coordinates_2 + size_fruit:
            return True
        return False

# Function to display the player's score during the game loop

def disp_score(score):
    # Increased font size for better visibility
    font = pygame.font.SysFont(None, 50)  # Increased font size
    score_text = font.render("Snake Score: " + str(score), True, (0, 0, 0))
    
    # Adjust position of the score display
    score_text_rect = score_text.get_rect(center=(window_rect.width / 2, 50))
    window.blit(score_text, score_text_rect)

    pseudo_text = font.render("Player: " + USER_PSEUDO, True, (0, 0, 0))
    pseudo_rect = pseudo_text.get_rect(topleft=(10,window_rect.height *0.02 ))  # Positioning on the top left
    window.blit(pseudo_text, pseudo_rect)

pygame.init()

# Creating the main window and giving it a name

window = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
window_rect = window.get_rect()
pygame.display.set_caption("Snake")

# Blitting an image on the main window

cover = pygame.Surface(window.get_size())
cover = cover.convert()
cover.fill((250, 250, 250))
window.blit(cover, (0,0))

# Refreshing the screen to display everything

pygame.display.flip()

# Loading the main images on the game window

head = pygame.image.load(HEAD_IMAGE_PATH).convert_alpha() # The head object
head = pygame.transform.scale(head, (35,35)) # Size the head object

body_part_1 = pygame.image.load(BODY_IMAGE_PATH).convert_alpha() # The body object
body_part_1 = pygame.transform.scale(body_part_1, (25,25)) # Size the body object

fruit = pygame.image.load(FRUIT_IMAGE_PATH).convert_alpha() # The fruit/apple object
fruit = pygame.transform.scale(fruit, (35,35)) # Size the fruit/apple object

# Storing the head and fruit's coordinates in variables

position_1 = head.get_rect()
position_fruit = fruit.get_rect()

# Storing the variables in the list variables created before

x_snake_position[0] = position_1.x
y_snake_position[0] = position_1.y

# Giving random coordinates to the first fruit of the game

position_fruit.x = randint(2,10)*step
position_fruit.y = randint(2,10)*step

# Main loop for the game

while (playing == True):
    
    # Collecting all the events

    for event in pygame.event.get(): 
        
        # Checking if the user quits the game
        
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            
            playing = False
     
        # Checking if the user presses a key
        
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP:

                if moveUp == False and move_init == True:#Vérification que la direction soit différente et annonce que les déplacement on débutés
                    if moveDown == True:# Empêchement d'aller dans la direction opposée
                        moveUp == False
                        
                    else:
                        
                        moveDown = moveRight = moveLeft = False #Changement de la variable de déplacement
                        moveUp = move_init = True

            if event.key == pygame.K_DOWN:

                if moveDown == False:# Empêchement d'aller dans la direction opposée
                    if moveUp == True:
                        moveDown == False
                        
                    else:
                        
                        moveRight = moveLeft = moveUp = False #Changement de la variable de déplacement
                        moveDown = move_init = True

            if event.key == pygame.K_RIGHT:

                if moveRight == False: # Empêchement d'aller dans la direction opposée
                    if moveLeft == True:
                        moveRight == False
                        
                    else:
                        
                        moveLeft = moveUp = moveDown = False #Changement de la variable de déplacement
                        moveRight = move_init = True

            if event.key == pygame.K_LEFT:
       
                if moveLeft == False:
                    if moveRight == True:# Empêchement d'aller dans la direction opposée
                        moveLeft == False
                        
                    else:
                        
                        moveRight = moveDown = moveUp = False #Changement de la variable de déplacement
                        moveLeft = move_init = True
                        
    # Blitting the head and the first part of the body

    window.blit(body_part_1, (-5,5))
    window.blit(head, (0,0))

    # Moving each part of the body by giving them new coordinates

    for i in range(length-1,0,-1):

        x_snake_position[i] = x_snake_position[(i-1)]

        y_snake_position[i] = y_snake_position[(i-1)]

    # Filling the window with white to erase the different parts of the snake
    
    cover.fill((250, 250, 250)) 
    
    # Blitting the parts of the snake on the screen
    
    for i in range(1,length):

        cover.blit(body_part_1, (x_snake_position[i], y_snake_position[i]))

    # Moving the snake in a certain direction if the user presses a key
    
    if moveUp:

        y_snake_position[0] = y_snake_position[0] - step 
        window.blit(cover, (0,0)) 
        window.blit(head, (x_snake_position[0], y_snake_position[0]))

    if moveDown:

        y_snake_position[0] = y_snake_position[0] + step
        window.blit(cover, (0,0))
        window.blit(head, (x_snake_position[0], y_snake_position[0]))

    if moveRight:

        x_snake_position[0] = x_snake_position[0] + step
        window.blit(cover, (0,0))
        window.blit(head, (x_snake_position[0], y_snake_position[0]))

    if moveLeft:

        x_snake_position[0] = x_snake_position[0] - step
        window.blit(cover, (0,0))
        window.blit(head, (x_snake_position[0], y_snake_position[0]))

    # Calling the collision function to check if the snake hits the edges of the window

    if x_snake_position[0] < window_rect.left:

        playing = False

    if x_snake_position[0] + 35 > window_rect.right:

        playing = False

    if y_snake_position[0] < window_rect.top:

        playing = False
    
    if y_snake_position[0] + 35 > window_rect.bottom:

        playing = False

    # Calling the collision function to check if the snake hits itself

    if collision(x_snake_position[0], y_snake_position[0], x_snake_position[i], y_snake_position[i],0,0) and (move_init == True):
        
        playing = False

    # Blitting the fruit
    
    window.blit(fruit, position_fruit)

    # Calling the collision function to check if the snake hits the fruit
    
    if collision(x_snake_position[0], y_snake_position[0], position_fruit.x, position_fruit.y,35,25):
        
        # Giving new coordinates to the fruit when the snake eats it

        position_fruit.x = randint(1,20)*step   
        position_fruit.y = randint(1,20)*step
    
        # Giving new coordinates to the fruit if the ones given above are the same as the snake's ones
        
        for j in range(0,length):

            while collision(position_fruit.x, position_fruit.y, x_snake_position[j], y_snake_position[j],35,25):

                position_fruit.x = randint(1,20)*step   
                position_fruit.y = randint(1,20)*step
        
        # Increasing the size of the snake and the score
        
        length = length + 1
        score = score + 1

    # Displaying the score
    
    disp_score(score)
    
    # Flipping to add everything on the board

    pygame.display.flip()

    # Delaying the game to make the snake move fluently
    
    time.sleep (speed / 1000)
    # Exiting the game if the main loop is done

pygame.quit()
exit()