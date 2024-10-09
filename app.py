import pygame
from pygame.locals import *
 
pygame.init()
vec = pygame.math.Vector2  # 2 for two dimensional
 
HEIGHT = 450
WIDTH = 400
ACC = 0.5
FRIC = -0.12
FPS = 60

BACKGROUND = pygame.image.load("Replicate_Bistro.png")
 
FramePerSec = pygame.time.Clock()
 
### Creates a canvas to display everything ###
displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))

displaysurface.blit(BACKGROUND, (HEIGHT, WIDTH))
pygame.display.set_caption("Game")

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    displaysurface.fill((0, 0, 0))  # Fill the screen with a black color
    pygame.display.update()
    FramePerSec.tick(FPS)

pygame.quit()