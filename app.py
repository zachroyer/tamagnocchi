import pygame
import sys
from pygame.locals import *
 
pygame.init()
vec = pygame.math.Vector2  # 2 for two dimensional
 
HEIGHT = 450
WIDTH = 400
ACC = 0.5
FRIC = -0.12
FPS = 60

### Loading in the background image ###
IMAGE = pygame.image.load("Replicate_Bistro.png")

### Scaling the background image to fit the initial window size ###
background = pygame.transform.scale(IMAGE, (HEIGHT, WIDTH))
 
FramePerSec = pygame.time.Clock()
 
### Creates a canvas to display everything ###
screen = pygame.display.set_mode((HEIGHT, WIDTH), HWSURFACE|DOUBLEBUF|RESIZABLE)

pygame.display.set_caption("Game")

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == pygame.KEYDOWN and event. key == pygame. K_ESCAPE):
            running = False
        elif event.type == pygame.VIDEORESIZE:
            screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
        # elif event.type == pygame.MOUSEBUTTONDOWN:
            # if event.button == 1: 
            #     print ("Left mouse button pressed") 

    scaledBackground = pygame.transform.scale(IMAGE, screen.get_size())
    screen.blit(scaledBackground, (0,0))
    
    pygame.draw.rect(screen, (200, 0, 0), pygame.Rect(5, 5, 60, 60))

    pygame.display.update()
    FramePerSec.tick(FPS)


pygame.quit()