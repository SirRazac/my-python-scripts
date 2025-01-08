# ------------------------------------------------------------------------------ 
# Import Packages
# ------------------------------------------------------------------------------ 
import pygame

pygame.init()

# Define screen size
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Starting position of snake
snake = [(100, 100), (80, 100), (60, 100)]
BLOCK_SIZE = 20

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Screen with backcolor
    screen.fill((255, 255, 255))  # white

    # Building snake
    for segment in snake:
        pygame.draw.rect(screen, (0, 255, 0), (*segment, BLOCK_SIZE, BLOCK_SIZE))  # green

    pygame.display.flip()
    clock.tick(30)

pygame.quit()