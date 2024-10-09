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

### 
BACKGROUND = pygame.transform.scale(pygame.image.load("Replicate_Bistro.png"), (HEIGHT, WIDTH))
 
FramePerSec = pygame.time.Clock()
 
### Creates a canvas to display everything ###
displaysurface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

pygame.display.set_caption("Game")

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == pygame.KEYDOWN and event. key == pygame. K_ESCAPE):
            running = False

    displaysurface.blit(BACKGROUND, (0,0))
    pygame.display.update()
    FramePerSec.tick(FPS)

pygame.quit()