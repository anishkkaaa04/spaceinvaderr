import pygame
#initialize pygame
pygame.init()

#creating screen
screen = pygame.display.set_mode((800 , 600))

#title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')

#game loop
running = True

while running:
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            running = False



